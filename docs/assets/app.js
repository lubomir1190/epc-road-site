const cfg = window.SITE_CONTENT || {};

document.querySelectorAll("[data-phone-text]").forEach(el => {
  el.textContent = cfg.phoneDisplay || el.textContent;
});

document.querySelectorAll("[data-phone-link]").forEach(el => {
  el.href = `tel:${cfg.phoneHref || "+359877360333"}`;
});

const servicesGrid = document.getElementById("servicesGrid");
if (servicesGrid && Array.isArray(cfg.services)) {
  servicesGrid.innerHTML = cfg.services.map(item => `
    <article class="service-card reveal">
      <div class="service-icon">${item.icon}</div>
      <h3>${item.title}</h3>
      <p>${item.text}</p>
      <strong>${item.price}</strong>
    </article>
  `).join("");
}

const partnersGrid = document.getElementById("partnersGrid");
if (partnersGrid && Array.isArray(cfg.partners)) {
  partnersGrid.innerHTML = cfg.partners.map(partner => {
    const tag = partner.url && partner.url !== "#" ? "a" : "div";
    const href = tag === "a" ? ` href="${partner.url}" target="_blank" rel="noopener"` : "";
    return `
      <${tag} class="partner-card reveal"${href}>
        <img src="${partner.image}" alt="${partner.name}" loading="lazy">
        <span>${partner.name}</span>
      </${tag}>
    `;
  }).join("");
}

document.getElementById("year").textContent = new Date().getFullYear();

const btn = document.querySelector(".menu-toggle");
const nav = document.querySelector(".nav");

btn?.addEventListener("click", () => {
  const open = nav.classList.toggle("open");
  btn.setAttribute("aria-expanded", String(open));
});

document.querySelectorAll(".nav a").forEach(a => {
  a.addEventListener("click", () => {
    nav.classList.remove("open");
    btn?.setAttribute("aria-expanded", "false");
  });
});

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add("visible");
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });

document.querySelectorAll(".reveal").forEach(el => observer.observe(el));

// Gallery lightbox
const thumbs = Array.from(document.querySelectorAll(".gallery-thumb"));
const lightbox = document.getElementById("lightbox");
const lightboxImg = lightbox?.querySelector(".lightbox-img");
let currentIndex = 0;

function openLightbox(index) {
  currentIndex = index;
  lightboxImg.src = thumbs[currentIndex].src;
  lightboxImg.alt = thumbs[currentIndex].alt;
  lightbox.classList.add("open");
  document.body.style.overflow = "hidden";
}

function closeLightbox() {
  lightbox.classList.remove("open");
  document.body.style.overflow = "";
}

function showNext() {
  currentIndex = (currentIndex + 1) % thumbs.length;
  lightboxImg.src = thumbs[currentIndex].src;
}

function showPrev() {
  currentIndex = (currentIndex - 1 + thumbs.length) % thumbs.length;
  lightboxImg.src = thumbs[currentIndex].src;
}

thumbs.forEach((img, i) => img.addEventListener("click", () => openLightbox(i)));
lightbox?.querySelector(".lightbox-close").addEventListener("click", closeLightbox);
lightbox?.querySelector(".lightbox-next").addEventListener("click", showNext);
lightbox?.querySelector(".lightbox-prev").addEventListener("click", showPrev);
lightbox?.addEventListener("click", e => { if (e.target === lightbox) closeLightbox(); });
document.addEventListener("keydown", e => {
  if (!lightbox?.classList.contains("open")) return;
  if (e.key === "Escape") closeLightbox();
  if (e.key === "ArrowRight") showNext();
  if (e.key === "ArrowLeft") showPrev();
});
