"""PDF Rotate — Rotate pages in a PDF by 90 or 180 degrees and save a new file."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='pdf_rotate',
        description='Rotate pages in a PDF by 90 or 180 degrees and save a new file.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('PDF Rotate')
    print('Fix a scan that came in sideways.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
