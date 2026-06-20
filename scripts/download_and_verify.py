from __future__ import annotations

import argparse
import hashlib
import tarfile
import urllib.request
from pathlib import Path


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def download(url: str, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url) as response, output.open("wb") as f:
        total = response.headers.get("Content-Length")
        total_int = int(total) if total and total.isdigit() else 0
        done = 0
        while True:
            chunk = response.read(1024 * 1024)
            if not chunk:
                break
            f.write(chunk)
            done += len(chunk)
            if total_int:
                print(f"\rdownloaded {done / total_int * 100:5.1f}%", end="", flush=True)
        if total_int:
            print()


def main() -> None:
    parser = argparse.ArgumentParser(description="Download and verify a TinyJudou release asset.")
    parser.add_argument("--url", required=True, help="GitHub Release asset URL.")
    parser.add_argument("--sha256", required=True, help="Expected SHA256 hex digest.")
    parser.add_argument("--output", required=True, help="Output tar.gz path.")
    parser.add_argument("--extract-dir", default="", help="Optional directory to extract into.")
    args = parser.parse_args()

    output = Path(args.output)
    if not output.exists():
        download(args.url, output)

    actual = sha256_file(output)
    if actual.lower() != args.sha256.lower():
        raise SystemExit(f"SHA256 mismatch: expected {args.sha256}, got {actual}")
    print(f"verified: {output} sha256={actual}")

    if args.extract_dir:
        extract_dir = Path(args.extract_dir)
        extract_dir.mkdir(parents=True, exist_ok=True)
        with tarfile.open(output, "r:gz") as tf:
            tf.extractall(extract_dir)
        print(f"extracted to: {extract_dir}")


if __name__ == "__main__":
    main()
