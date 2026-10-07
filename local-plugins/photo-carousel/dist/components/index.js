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
    { href, class: "carousel-slide" },
    imgSrc ? h("img", { src: imgSrc, alt, loading: "lazy" }) : null,
    caption ? h("div", { class: "slide-caption" }, caption) : null,
  );
}

// Carrossel: avanca sozinho (autoplay), com botoes anterior/proximo nas bordas.
// Sem zoom automatico por hover; os slides continuam sendo links normais.
// Roda contra todo `.media-carousel` da pagina (inclusive os escritos a mao em markdown).
const CAROUSEL_ZOOM_SCRIPT = `
function quartzCarouselSetup() {
  var INTERVAL = 3500;
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
    var prevBtn = mkBtn("carousel-edge-prev", "Anterior", "\u2039");
    var nextBtn = mkBtn("carousel-edge-next", "Pr\u00f3ximo", "\u203a");

    function step(dir) {
      var slides = car.querySelectorAll(".carousel-slide");
      if (!slides.length) return;
      var gap = parseFloat(getComputedStyle(car).columnGap) || 16;
      var w = slides[0].getBoundingClientRect().width + gap;
      var max = car.scrollWidth - car.clientWidth;
      if (max <= 4) return;
      if (dir > 0 && car.scrollLeft >= max - 4) car.scrollTo({ left: 0, behavior: "smooth" });
      else if (dir < 0 && car.scrollLeft <= 4) car.scrollTo({ left: max, behavior: "smooth" });
      else car.scrollBy({ left: dir * w, behavior: "smooth" });
    }

    var paused = false;
    var timer = setInterval(function () {
      if (!car.isConnected) { clearInterval(timer); return; }
      if (paused || document.hidden) return;
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
function quartzCarouselInit() { placeCarouselAfterNav(); quartzCarouselSetup(); placeCarouselAfterNav(); }
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
            { href: p.url, class: "carousel-slide", target: "_blank", rel: "noopener" },
            h("img", { src: p.url, alt: title, loading: "lazy" }),
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
