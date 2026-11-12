"""Cutest-picture-01 entry: copy art.png to the output directory as entry.png.

Standard library only. Run with MAKEFUN_OUTPUT_DIR set (default /output).
"""
import os
import shutil
from pathlib import Path

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
OUT_DIR.mkdir(parents=True, exist_ok=True)

src = HERE / "art.png"
with src.open("rb") as f:
    if f.read(8) != PNG_MAGIC:
        raise ValueError("art.png is not a PNG file")

tmp = OUT_DIR / "entry.png.tmp"
shutil.copyfile(src, tmp)
os.replace(tmp, OUT_DIR / "entry.png")
