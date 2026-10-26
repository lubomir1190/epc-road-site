const cfg = window.SITE_CONTENT || {};
const offers = window.OFFERS || {};

// Discount/condition numbers from offers.js; the HTML holds the same values as fallback
document.querySelectorAll("[data-offer]").forEach(el => {
  const value = offers[el.dataset.offer];
  if (value !== undefined) el.textContent = value;
});
if (offers.vipDiscount !== undefined) {
  document.documentElement.style.setProperty("--vip-discount-label", `"${offers.vipDiscount}%"`);
}
// data-offer-if="a b": shown only when all flags are true; data-offer-unless="c": hidden when any is true
document.querySelectorAll("[data-offer-if], [data-offer-unless]").forEach(el => {
  const ifKeys = (el.dataset.offerIf || "").split(" ").filter(Boolean);
  const unlessKeys = (el.dataset.offerUnless || "").split(" ").filter(Boolean);
  el.hidden = !ifKeys.every(key => offers[key]) || unlessKeys.some(key => offers[key]);
});

document.querySelectorAll("[data-phone-text]").forEach(el => {
  el.textContent = cfg.phoneDisplay || el.textContent;
});

document.querySelectorAll("[data-phone-link]").forEach(el => {
  el.href = `tel:${cfg.phoneHref || "+359877360333"}`;
});

const partnersGrid = document.getElementById("partnersGrid");
if (partnersGrid && Array.isArray(cfg.partners)) {
  partnersGrid.innerHTML = cfg.partners.map(partner => {
    const tag = partner.url && partner.url !== "#" ? "a" : "div";
    const href = tag === "a" ? ` href="${partner.url}" target="_blank" rel="noopener"` : "";
    return `
      <${tag} class="partner-card${partner.highlight ? " is-highlight" : ""} reveal"${href}>
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

const galleryMoreBtn = document.getElementById("galleryMoreBtn");
galleryMoreBtn?.addEventListener("click", () => {
  document.querySelectorAll(".gallery-extra").forEach(img => img.classList.remove("gallery-extra"));
  galleryMoreBtn.remove();
});

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

// Booking widget (Calendly or Cal.com, picked from the bookingUrl host) —
// the script loads only when the section nears the viewport
const bookingWidget = document.getElementById("bookingWidget");
const bookingFallback = document.getElementById("bookingFallback");

function loadBookingWidget() {
  const url = new URL(cfg.bookingUrl);
  if (url.hostname.endsWith("cal.com")) loadCalComWidget(url);
  else loadCalendlyWidget(url);
}

function loadCalComWidget(url) {
  bookingWidget.classList.add("booking-widget--auto");
  // Official Cal.com embed loader: queues calls on window.Cal until embed.js arrives
  (function (C, A, L) {
    const p = (a, ar) => { a.q.push(ar); };
    const d = C.document;
    C.Cal = C.Cal || function () {
      const cal = C.Cal;
      const ar = arguments;
      if (!cal.loaded) {
        cal.ns = {};
        cal.q = cal.q || [];
        d.head.appendChild(d.createElement("script")).src = A;
        cal.loaded = true;
      }
      if (ar[0] === L) {
        const api = function () { p(api, arguments); };
        const namespace = ar[1];
        api.q = api.q || [];
        if (typeof namespace === "string") {
          cal.ns[namespace] = cal.ns[namespace] || api;
          p(cal.ns[namespace], ar);
          p(cal, ["initNamespace", namespace]);
        } else p(cal, ar);
        return;
      }
      p(cal, ar);
    };
  })(window, "https://app.cal.com/embed/embed.js", "init");

  window.Cal("init", "booking", { origin: "https://app.cal.com" });
  window.Cal.ns.booking("inline", {
    elementOrSelector: "#bookingWidget",
    calLink: url.pathname.replace(/^\/|\/$/g, ""),
    config: { theme: "dark", layout: "month_view" },
  });
  window.Cal.ns.booking("ui", {
    theme: "dark",
    cssVarsPerTheme: { dark: { "cal-brand": "#f4c430" } },
    layout: "month_view",
  });
}

function loadCalendlyWidget(url) {
  url.searchParams.set("hide_gdpr_banner", "1");
  url.searchParams.set("background_color", "111111");
  url.searchParams.set("text_color", "f8f8f8");
  url.searchParams.set("primary_color", "f4c430");

  const script = document.createElement("script");
  script.src = "https://assets.calendly.com/assets/external/widget.js";
  script.async = true;
  script.onload = () => {
    window.Calendly.initInlineWidget({ url: url.toString(), parentElement: bookingWidget });
  };
  document.head.appendChild(script);
}

if (bookingWidget && cfg.bookingUrl) {
  bookingFallback.hidden = true;
  const bookingObserver = new IntersectionObserver((entries) => {
    if (entries.some(entry => entry.isIntersecting)) {
      bookingObserver.disconnect();
      loadBookingWidget();
    }
  }, { rootMargin: "400px 0px" });
  bookingObserver.observe(bookingWidget);
} else {
  bookingWidget?.remove();
}
