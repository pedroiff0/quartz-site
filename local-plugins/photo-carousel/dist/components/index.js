import { h } from "preact";
import fs from "node:fs";
import path from "node:path";
import { slugifyFilePath, resolveRelative } from "@quartz-community/utils/path";

const IMAGE_RE = /\.(jpe?g|png|webp|gif|avif)$/i;

function normalizeSlug(s) {
  return String(s || "").toLowerCase().replace(/[^a-z0-9]/g, "");
}

function findPhotoDir(folder) {
  const cwd = process.cwd();
  const candidates = [
    path.join(cwd, "content", "resource", "meta", "imagens", "photos", folder),
    path.join(cwd, "content", "assets", "photos", folder),
    path.join(cwd, "content", "resource", "midia", folder),
  ];
  for (const c of candidates) {
    if (fs.existsSync(c) && fs.statSync(c).isDirectory()) {
      return c;
    }
  }

  const midiaBase = path.join(cwd, "content", "resource", "midia");
  if (fs.existsSync(midiaBase)) {
    const normTarget = normalizeSlug(folder);
    try {
      const years = fs.readdirSync(midiaBase);
      for (const y of years) {
        const yDir = path.join(midiaBase, y);
        if (fs.statSync(yDir).isDirectory()) {
          const events = fs.readdirSync(yDir);
          for (const ev of events) {
            const evDir = path.join(yDir, ev);
            if (fs.statSync(evDir).isDirectory()) {
              const normEv = normalizeSlug(ev);
              if (ev === folder || normEv === normTarget || normTarget.includes(normEv) || normEv.includes(normTarget)) {
                return evDir;
              }
            }
          }
        }
      }
    } catch {
      // ignore
    }
  }
  return null;
}

function listPhotos(folder) {
  const dir = findPhotoDir(folder);
  if (!dir) return [];
  try {
    const files = fs
      .readdirSync(dir)
      .filter((f) => IMAGE_RE.test(f))
      .sort();
    const contentDir = path.join(process.cwd(), "content");
    return files.map((f) => {
      const relPath = path.relative(contentDir, path.join(dir, f));
      return {
        file: f,
        url: "/" + slugifyFilePath(relPath),
      };
    });
  } catch {
    return [];
  }
}

function slide(href, imgSrc, alt, caption) {
  return h(
    "a",
    { href, class: "carousel-slide carousel-card" },
    imgSrc ? h("img", { src: imgSrc, alt, loading: "lazy", decoding: "async" }) : null,
    caption ? h("div", { class: "slide-caption" }, caption) : null,
  );
}

// Carrossel: avanca sozinho (autoplay), com botoes anterior/proximo nas bordas.
// Fotos (modo 1): clique abre um lightbox grande (foto inteira, setas, Esc, deslize); sem JS o link abre a foto.
// Cartoes de evento (modo 2): seguem como links para a nota.
// Roda contra todo `.media-carousel` da pagina (inclusive os escritos a mao em markdown).
const CAROUSEL_ZOOM_SCRIPT = `
var quartzLb = window.__quartzCarouselLb || (window.__quartzCarouselLb = { el: null, img: null, count: null, items: [], i: 0, opener: null, open: false });

function quartzLbBuild() {
  if (quartzLb.el) return;
  var el = document.createElement("div");
  el.className = "carousel-lightbox";
  el.setAttribute("role", "dialog");
  el.setAttribute("aria-modal", "true");
  el.setAttribute("aria-label", "Foto ampliada");
  function btn(cls, label, glyph, fn) {
    var b = document.createElement("button");
    b.type = "button";
    b.className = "carousel-lightbox-btn " + cls;
    b.setAttribute("aria-label", label);
    b.textContent = glyph;
    b.addEventListener("click", function (e) { e.stopPropagation(); fn(); });
    el.appendChild(b);
    return b;
  }
  quartzLb.close = btn("carousel-lightbox-close", "Fechar", "\\u00d7", quartzLbClose);
  quartzLb.prev = btn("carousel-lightbox-prev", "Foto anterior", "\\u2039", function () { quartzLbGo(-1); });
  quartzLb.next = btn("carousel-lightbox-next", "Pr\\u00f3xima foto", "\\u203a", function () { quartzLbGo(1); });
  var img = document.createElement("img");
  img.alt = "";
  img.draggable = false;
  el.appendChild(img);
  var cnt = document.createElement("div");
  cnt.className = "carousel-lightbox-count";
  cnt.setAttribute("aria-live", "polite");
  el.appendChild(cnt);
  el.addEventListener("click", function () { quartzLbClose(); });
  var x0 = null;
  el.addEventListener("touchstart", function (e) { x0 = e.touches.length === 1 ? e.touches[0].clientX : null; }, { passive: true });
  el.addEventListener("touchend", function (e) {
    if (x0 === null) return;
    var dx = e.changedTouches[0].clientX - x0;
    x0 = null;
    if (Math.abs(dx) > 50) quartzLbGo(dx < 0 ? 1 : -1);
  }, { passive: true });
  document.addEventListener("keydown", function (e) {
    if (!quartzLb.open) return;
    if (e.key === "Escape") { e.preventDefault(); quartzLbClose(); }
    else if (e.key === "ArrowLeft") { e.preventDefault(); quartzLbGo(-1); }
    else if (e.key === "ArrowRight") { e.preventDefault(); quartzLbGo(1); }
    else if (e.key === "Tab") {
      var f = [quartzLb.close, quartzLb.prev, quartzLb.next].filter(function (b) { return b.style.display !== "none"; });
      var k = f.indexOf(document.activeElement);
      e.preventDefault();
      f[(k + (e.shiftKey ? f.length - 1 : 1)) % f.length].focus();
    }
  });
  document.body.appendChild(el);
  quartzLb.el = el;
  quartzLb.img = img;
  quartzLb.count = cnt;
}

function quartzLbShow() {
  var it = quartzLb.items[quartzLb.i];
  quartzLb.img.src = it.href;
  quartzLb.img.alt = it.alt;
  var multi = quartzLb.items.length > 1;
  quartzLb.prev.style.display = multi ? "" : "none";
  quartzLb.next.style.display = multi ? "" : "none";
  quartzLb.count.textContent = multi ? (quartzLb.i + 1) + " / " + quartzLb.items.length : "";
}

function quartzLbGo(d) {
  var n = quartzLb.items.length;
  if (n < 2) return;
  quartzLb.i = (quartzLb.i + d + n) % n;
  quartzLbShow();
}

function quartzLbOpen(items, i, opener) {
  quartzLbBuild();
  quartzLb.items = items;
  quartzLb.i = i;
  quartzLb.opener = opener;
  quartzLbShow();
  quartzLb.el.classList.add("open");
  document.body.classList.add("carousel-lightbox-open");
  quartzLb.open = true;
  quartzLb.close.focus();
}

function quartzLbClose() {
  if (!quartzLb.open) return;
  quartzLb.open = false;
  quartzLb.el.classList.remove("open");
  document.body.classList.remove("carousel-lightbox-open");
  var o = quartzLb.opener;
  var it = quartzLb.items[quartzLb.i];
  if (o && o.isConnected) {
    if (it && it.slide && it.slide.isConnected) {
      var car = it.slide.parentNode;
      var r = it.slide.getBoundingClientRect(), c = car.getBoundingClientRect();
      car.scrollTo({ left: car.scrollLeft + (r.left - c.left) - (car.clientWidth - r.width) / 2, behavior: "auto" });
      it.slide.focus({ preventScroll: true });
    } else o.focus({ preventScroll: true });
  }
}

function quartzCarouselSetup() {
  var INTERVAL = 3500;
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  document.querySelectorAll(".media-carousel").forEach(function (car) {
    if (car.dataset.carouselBound === "true") return;
    car.dataset.carouselBound = "true";

    var wrap = document.createElement("div");
    wrap.className = "carousel-nav-wrap";
    car.parentNode.insertBefore(wrap, car);
    wrap.appendChild(car);

    function mkBtn(cls, label, glyph) {
      var b = document.createElement("button");
      b.type = "button";
      b.className = "carousel-edge " + cls;
      b.setAttribute("aria-label", label);
      b.textContent = glyph;
      wrap.appendChild(b);
      return b;
    }
    var prevBtn = mkBtn("carousel-edge-prev", "Anterior", "\\u2039");
    var nextBtn = mkBtn("carousel-edge-next", "Pr\\u00f3ximo", "\\u203a");

    function slides() { return Array.prototype.slice.call(car.querySelectorAll(".carousel-slide")); }
    function centerOf(s) {
      var r = s.getBoundingClientRect(), c = car.getBoundingClientRect();
      return car.scrollLeft + (r.left - c.left) + r.width / 2;
    }
    function nearest() {
      var mid = car.scrollLeft + car.clientWidth / 2, best = 0, bd = Infinity;
      slides().forEach(function (s, i) { var d = Math.abs(centerOf(s) - mid); if (d < bd) { bd = d; best = i; } });
      return best;
    }
    function goTo(i) {
      var ss = slides();
      if (!ss[i]) return;
      car.scrollTo({ left: Math.max(0, centerOf(ss[i]) - car.clientWidth / 2), behavior: reduce ? "auto" : "smooth" });
    }
    function step(dir) {
      var n = slides().length;
      if (n < 2 || car.scrollWidth - car.clientWidth <= 4) return;
      var max = car.scrollWidth - car.clientWidth, i = nearest() + dir;
      if (dir > 0 && (i >= n || car.scrollLeft >= max - 4)) i = 0;
      else if (dir < 0 && (i < 0 || car.scrollLeft <= 4)) i = n - 1;
      goTo(i);
    }

    var paused = false;
    var timer = reduce ? null : setInterval(function () {
      if (!car.isConnected) { clearInterval(timer); return; }
      if (paused || document.hidden || quartzLb.open) return;
      step(1);
    }, INTERVAL);

    prevBtn.addEventListener("click", function (e) { e.preventDefault(); e.stopPropagation(); step(-1); });
    nextBtn.addEventListener("click", function (e) { e.preventDefault(); e.stopPropagation(); step(1); });
    wrap.addEventListener("mouseenter", function () { paused = true; });
    wrap.addEventListener("mouseleave", function () { paused = false; });
    wrap.addEventListener("focusin", function () { paused = true; });
    wrap.addEventListener("focusout", function () { paused = false; });
    wrap.addEventListener("touchstart", function () { paused = true; }, { passive: true });
    wrap.addEventListener("touchend", function () { setTimeout(function () { paused = false; }, 4000); }, { passive: true });

    car.addEventListener("click", function (e) {
      var a = e.target.closest ? e.target.closest(".carousel-slide[data-zoom]") : null;
      if (!a || !car.contains(a)) return;
      if (e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
      e.preventDefault();
      var zs = slides().filter(function (s) { return s.hasAttribute("data-zoom"); });
      var items = zs.map(function (s) {
        var im = s.querySelector("img");
        return { href: s.getAttribute("href"), alt: im ? im.alt : "", slide: s };
      });
      quartzLbOpen(items, zs.indexOf(a), a);
    });
  });
}

// O carrossel e renderizado no cabecalho (apos Criado/Modificado); quando a nota tem nav-*, ele vai para logo abaixo da nav.
function placeCarouselAfterNav() {
  var nav = document.querySelector("article .academic-nav-container");
  document.querySelectorAll(".page-header > .media-carousel, .page-header > .carousel-nav-wrap").forEach(function (c) {
    if (nav) nav.insertAdjacentElement("afterend", c);
    c.setAttribute("data-placed", "1");
  });
}
function quartzCarouselInit() { quartzLbClose(); placeCarouselAfterNav(); quartzCarouselSetup(); placeCarouselAfterNav(); }
document.addEventListener("nav", quartzCarouselInit);
document.addEventListener("render", quartzCarouselInit);
quartzCarouselInit();
`;

function PhotoCarouselConstructor() {
  const PhotoCarousel = (props) => {
    const fileData = props?.fileData ?? {};
    const frontmatter = fileData.frontmatter ?? {};
    const folder = frontmatter.photoFolder;

    // Mode 1: this note itself declares a photoFolder — show every photo in it,
    // opening the full-size image directly (existing single-event behaviour).
    if (folder && typeof folder === "string") {
      const photos = listPhotos(folder);
      if (photos.length === 0) return null;
      const title = typeof frontmatter.title === "string" ? frontmatter.title : "";
      return h(
        "div",
        { class: "media-carousel" },
        photos.map((p) => {
          return h(
            "a",
            { href: p.url, class: "carousel-slide", "data-zoom": "1", "data-router-ignore": "", target: "_blank", rel: "noopener" },
            h("img", { src: p.url, alt: title, loading: "lazy", decoding: "async" }),
          );
        }),
      );
    }

    // Mode 2: this is a folder-index note (e.g. media/index.md, media/2025/index.md).
    // Gather every descendant note that DOES declare a photoFolder and build one
    // slide per event, linking to the note and using its first photo as thumbnail.
    // New event notes need zero manual carousel edits — they just show up here
    // once published, and start showing a real photo the moment one is added.
    const slug = fileData.slug;
    if (!slug || slug === "index" || !slug.endsWith("/index")) return null;

    const prefix = slug.slice(0, -"/index".length);
    // Scope the gallery to the "media" section specifically (any language) —
    // otherwise a broad index page like the homepage would also match, since
    // it technically sits above every media note in the slug tree too.
    if (!prefix.split("/").includes("media")) return null;

    const allFiles = props?.allFiles ?? [];
    const children = allFiles.filter((f) => {
      const s = f.slug;
      if (!s || !s.startsWith(prefix + "/")) return false;
      const childFolder = f.frontmatter?.photoFolder;
      return typeof childFolder === "string" && childFolder.length > 0;
    });
    if (children.length === 0) return null;

    children.sort((a, b) => {
      const da = a.frontmatter?.created ? new Date(a.frontmatter.created).getTime() : 0;
      const db = b.frontmatter?.created ? new Date(b.frontmatter.created).getTime() : 0;
      return da - db;
    });

    return h(
      "div",
      { class: "media-carousel" },
      children.map((child) => {
        const childFolder = child.frontmatter.photoFolder;
        const title = typeof child.frontmatter?.title === "string" ? child.frontmatter.title : "";
        const photos = listPhotos(childFolder);
        const imgSrc = photos.length > 0 ? photos[0].url : null;
        const href = resolveRelative(slug, child.slug);
        return slide(href, imgSrc, title, title);
      }),
    );
  };
  PhotoCarousel.afterDOMLoaded = CAROUSEL_ZOOM_SCRIPT;
  PhotoCarousel.isPhotoCarousel = true;
  return PhotoCarousel;
}

export { PhotoCarouselConstructor as PhotoCarousel };
