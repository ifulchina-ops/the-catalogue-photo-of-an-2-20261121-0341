"""Pocket Black Hole — catalogue photo entry.

Copies the pre-rendered catalogue photograph (entry.png, painted locally
with PIL before packaging) to /output/entry.png. Pure standard library:
no third-party imports, no network, no fonts needed at runtime.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUT = os.path.join(OUT_DIR, "entry.png")


def main():
    # The asset is bundled in the repo; the sandbox only copies it out.
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, OUT)
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
