#!/usr/bin/env python3
import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Extract error-like lines from log")
    parser.add_argument("--input", required=True, help="Input log file")
    parser.add_argument("--output", required=True, help="Output file")
    parser.add_argument("--keywords", default="error,exception,failed,timeout",
                        help="Comma separated keywords")
    args = parser.parse_args()

    in_path = Path(args.input)
    out_path = Path(args.output)
    keys = [k.strip().lower() for k in args.keywords.split(",") if k.strip()]

    if not in_path.exists():
        raise FileNotFoundError(f"Input file not found: {in_path}")

    count = 0
    with in_path.open("r", encoding="utf-8", errors="ignore") as fin, \
         out_path.open("w", encoding="utf-8") as fout:
        for line in fin:
            low = line.lower()
            if any(k in low for k in keys):
                fout.write(line)
                count += 1

    print(f"Done: {count} lines extracted -> {out_path}")

if __name__ == "__main__":
    main()
