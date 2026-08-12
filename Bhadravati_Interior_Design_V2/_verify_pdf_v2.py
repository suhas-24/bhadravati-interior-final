#!/usr/bin/env python3
"""Verify Bhadravati_Interior_Design_V2.pdf is a valid, readable PDF."""
from __future__ import annotations

import sys
from pathlib import Path

PDF = Path(__file__).resolve().parent / "Bhadravati_Interior_Design_V2.pdf"


def main() -> int:
    if not PDF.is_file():
        print(f"FAIL: missing {PDF}", file=sys.stderr)
        return 1

    raw = PDF.read_bytes()
    if not raw.startswith(b"%PDF-"):
        print("FAIL: missing %PDF- header", file=sys.stderr)
        return 1
    if b"%%EOF" not in raw[-1024:]:
        print("FAIL: missing %%EOF trailer", file=sys.stderr)
        return 1

    from pypdf import PdfReader

    reader = PdfReader(str(PDF))
    if reader.is_encrypted:
        print("FAIL: PDF is encrypted", file=sys.stderr)
        return 1
    n = len(reader.pages)
    if n < 1:
        print("FAIL: page count is 0", file=sys.stderr)
        return 1

    page1 = reader.pages[0]
    text = page1.extract_text() or ""
    if "BHADRAVATI" not in text.upper():
        print(f"FAIL: page 1 text unexpected ({text[:120]!r})", file=sys.stderr)
        return 1

    print(f"OK: {PDF}")
    print(f"  size_bytes={PDF.stat().st_size}")
    print(f"  pages={n}")
    print(f"  encrypted={reader.is_encrypted}")
    print(f"  page1_chars={len(text)}")
    print(f"  page1_preview={text[:160]!r}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
