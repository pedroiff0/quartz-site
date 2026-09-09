(function() {
  const container = document.getElementById('three-bg-container');
  if (!container) return;
  
  let animationId = 0;
  let renderer, scene, camera, galaxy, stars, sun, glow;
  
  function isDark() {
    return document.documentElement.getAttribute('saved-theme') === 'dark' ||
           document.documentElement.dataset.theme === 'dark';
  }
  
  function init() {
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.z = 5;
    
    renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    container.appendChild(renderer.domElement);
    
    // Stars
    const starsGeo = new THREE.BufferGeometry();
    const sPos = new Float32Array(3000 * 3);
    const sCol = new Float32Array(3000 * 3);
    for (let i = 0; i < 3000; i++) {
      sPos[i*3] = (Math.random()-0.5)*200;
      sPos[i*3+1] = (Math.random()-0.5)*200;
      sPos[i*3+2] = (Math.random()-0.5)*200;
      const b = Math.random()*0.5+0.5;
      sCol[i*3] = b; sCol[i*3+1] = b; sCol[i*3+2] = b;
    }
    starsGeo.setAttribute('position', new THREE.BufferAttribute(sPos, 3));
    starsGeo.setAttribute('color', new THREE.BufferAttribute(sCol, 3));
    stars = new THREE.Points(starsGeo, new THREE.PointsMaterial({ size: 0.15, vertexColors: true, transparent: true, opacity: 0.8 }));
    scene.add(stars);
    
    // Galaxy
    const gGeo = new THREE.BufferGeometry();
    const gPos = new Float32Array(50000 * 3);
    const gCol = new Float32Array(50000 * 3);
    const arms = 4;
    for (let i = 0; i < 50000; i++) {
      const r = Math.random() * 8;
      const armAngle = ((i % arms) / arms) * Math.PI * 2;
      const spinAngle = r * 0.5;
      const rand = (Math.random() - 0.5) * 0.3;
      gPos[i*3] = Math.cos(armAngle + spinAngle) * r + rand;
      gPos[i*3+1] = (Math.random()-0.5) * 0.1 * (1-r/8);
      gPos[i*3+2] = Math.sin(armAngle + spinAngle) * r + rand;
      const t = r/8;
      if (Math.random() > 0.7) {
        gCol[i*3] = 1.0; gCol[i*3+1] = 0.85; gCol[i*3+2] = 0.4;
      } else {
        gCol[i*3] = 0.4 + (1-t)*0.4;
        gCol[i*3+1] = 0.5 + (1-t)*0.3;
        gCol[i*3+2] = 0.8 + (1-t)*0.2;
      }
    }
    gGeo.setAttribute('position', new THREE.BufferAttribute(gPos, 3));
    gGeo.setAttribute('color', new THREE.BufferAttribute(gCol, 3));
    galaxy = new THREE.Points(gGeo, new THREE.PointsMaterial({ size: 0.05, vertexColors: true, transparent: true, opacity: 0.6, blending: THREE.AdditiveBlending }));
    galaxy.rotation.x = Math.PI / 3;
    scene.add(galaxy);
    
    // Sun
    const sunGeo = new THREE.SphereGeometry(2, 64, 64);
    const sunMat = new THREE.ShaderMaterial({
      uniforms: { time: { value: 0 } },
      vertexShader: 'varying vec2 vUv;varying vec3 vNormal;void main(){vUv=uv;vNormal=normal;gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.0);}',
      fragmentShader: 'uniform float time;varying vec2 vUv;varying vec3 vNormal;vec3 mod289(vec3 x){return x-floor(x*(1.0/289.0))*289.0;}vec4 mod289(vec4 x){return x-floor(x*(1.0/289.0))*289.0;}vec4 permute(vec4 x){return mod289(((x*34.0)+1.0)*x);}vec4 taylorInvSqrt(vec4 r){return 1.79284291400159-0.85373472095314*r;}float snoise(vec3 v){const vec2 C=vec2(1.0/6.0,1.0/3.0);const vec4 D=vec4(0.0,0.5,1.0,2.0);vec3 i=floor(v+dot(v,C.yyy));vec3 x0=v-i+dot(i,C.xxx);vec3 g=step(x0.yzx,x0.xyz);vec3 l=1.0-g;vec3 i1=min(g.xyz,l.zxy);vec3 i2=max(g.xyz,l.zxy);vec3 x1=x0-i1+C.xxx;vec3 x2=x0-i2+C.yyy;vec3 x3=x0-D.yyy;i=mod289(i);vec4 p=permute(permute(permute(i.z+vec4(0.0,i1.z,i2.z,1.0))+i.y+vec4(0.0,i1.y,i2.y,1.0))+i.x+vec4(0.0,i1.x,i2.x,1.0));float n_=0.142857142857;vec3 ns=n_*D.wyz-D.xzx;vec4 j=p-49.0*floor(p*ns.z*ns.z);vec4 x_=floor(j*ns.z);vec4 y_=floor(j-7.0*x_);vec4 x=x_*ns.x+ns.yyyy;vec4 y=y_*ns.x+ns.yyyy;vec4 h=1.0-abs(x)-abs(y);vec4 b0=vec4(x.xy,y.xy);vec4 b1=vec4(x.zw,y.zw);vec4 s0=floor(b0)*2.0+1.0;vec4 s1=floor(b1)*2.0+1.0;vec4 sh=-step(h,vec4(0.0));vec4 a0=b0.xzyw+s0.xzyw*sh.xxyy;vec4 a1=b1.xzyw+s1.xzyw*sh.zzww;vec3 p0=vec3(a0.xy,h.x);vec3 p1=vec3(a0.zw,h.y);vec3 p2=vec3(a1.xy,h.z);vec3 p3=vec3(a1.zw,h.w);vec4 norm=taylorInvSqrt(vec4(dot(p0,p0),dot(p1,p1),dot(p2,p2),dot(p3,p3)));p0*=norm.x;p1*=norm.y;p2*=norm.z;p3*=norm.w;vec4 m=max(0.6-vec4(dot(x0,x0),dot(x1,x1),dot(x2,x2),dot(x3,x3)),0.0);m=m*m;return 42.0*dot(m*m,vec4(dot(p0,x0),dot(p1,x1),dot(p2,x2),dot(p3,x3)));}void main(){float noise=snoise(vec3(vUv.xy*4.0,time*0.3));noise+=snoise(vec3(vUv.xy*8.0,time*0.5))*0.5;noise+=snoise(vec3(vUv.xy*16.0,time*0.7))*0.25;vec3 c1=vec3(1.0,0.55,0.1);vec3 c2=vec3(1.0,0.9,0.4);vec3 c3=vec3(1.0,0.3,0.0);vec3 color=mix(c3,c1,smoothstep(-0.5,0.0,noise));color=mix(color,c2,smoothstep(0.0,0.5,noise));float fresnel=pow(1.0-abs(dot(vNormal,vec3(0.0,0.0,1.0))),2.0);color=mix(color,vec3(1.0,0.9,0.7),fresnel*0.5);gl_FragColor=vec4(color,1.0);}'
    });
    sun = new THREE.Mesh(sunGeo, sunMat);
    sun.visible = false;
    scene.add(sun);
    
    // Glow
    const glowGeo = new THREE.SphereGeometry(2.3, 32, 32);
    const glowMat = new THREE.ShaderMaterial({
      uniforms: {},
      vertexShader: 'varying float intensity;void main(){vec3 vN=normalize(normalMatrix*normal);vec3 vE=normalize(normalMatrix*vec3(0.0,0.0,1.0));intensity=pow(0.7-dot(vN,vE),2.0);gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.0);}',
      fragmentShader: 'varying float intensity;void main(){vec3 glow=vec3(1.0,0.7,0.2)*intensity;gl_FragColor=vec4(glow,intensity*0.5);}',
      side: THREE.FrontSide,
      blending: THREE.AdditiveBlending,
      transparent: true
    });
    glow = new THREE.Mesh(glowGeo, glowMat);
    glow.visible = false;
    scene.add(glow);
    
    const clock = new THREE.Clock();
    function animate() {
      const delta = clock.getDelta();
      const elapsed = clock.getElapsedTime();
      if (galaxy) galaxy.rotation.z += delta * 0.05;
      if (stars) { stars.rotation.y += delta * 0.01; stars.rotation.x += delta * 0.005; }
      if (sun && sun.visible) { sunMat.uniforms.time.value = elapsed; sun.rotation.y += delta * 0.1; }
      if (glow && glow.visible) glow.rotation.y += delta * 0.1;
      const dark = isDark();
      if (galaxy) galaxy.visible = dark;
      if (sun) sun.visible = !dark;
      if (glow) glow.visible = !dark;
      renderer.render(scene, camera);
      animationId = requestAnimationFrame(animate);
    }
    animate();
    
    window.addEventListener('resize', () => {
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(window.innerWidth, window.innerHeight);
    });
  }
  
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
