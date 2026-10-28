"""Общи константи за генератора на страници (tools/build_pages.py)."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SITE = "https://www.epc24.bg"
PHONE = "0877 360 333"
PHONE_HREF = "+359877360333"

# Числата за отстъпки и условия идват от offers.js, за да са същите като на началната страница
_offers = (DOCS / "assets/offers.js").read_text()
def _offer(key):
    return int(re.search(rf"^\s*{key}:\s*(\d+)", _offers, re.M).group(1))
D = _offer("plannedDiscount")
KG = _offer("maxWeightKg")
H = _offer("minNoticeHours")
PLANNED_SOFIA = round(60 * (100 - D) / 100)

# Линкът за онлайн резервация — от content.js (на английските страници водим директно към него)
BOOKING_URL = re.search(r'bookingUrl:\s*"([^"]*)"', (DOCS / "assets/content.js").read_text()).group(1)
