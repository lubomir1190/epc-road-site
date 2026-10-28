# EPC / Зет Хаш Дизайн – Пътна помощ 24/7

Статичен сайт за GitHub Pages.

## Редакция
- Услуги, цени и партньори: `assets/content.js`
- Стилове: `assets/styles.css`
- Основен HTML: `index.html`
- Страници за услуги и райони (`/repatrak-sofia/`, `/en/tow-truck-sofia/` и т.н.): текстовете са в `tools/pages_bg.py` и `tools/pages_en.py`.
  След промяна там или в `assets/offers.js` пусни `python3 tools/build_pages.py` — генерираните страници не се редактират на ръка.
  Нова страница се добавя и на двата езика (английската с `key` = slug-а на българската), в `docs/sitemap.xml` и във футъра на `docs/index.html` и `docs/en/index.html`.
- Снимки: качвай ги като `.webp` (до ~1280 px широки), не като големи PNG/JPG.

## Социални мрежи
В `index.html` намери Instagram / Facebook / TikTok линковете и замени `#` с реалните URL адреси.

## GitHub Pages
Качи файловете в repository → Settings → Pages → Deploy from branch → main / root.
