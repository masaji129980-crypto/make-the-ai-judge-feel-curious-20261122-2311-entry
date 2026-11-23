"""Write one short text to /output/entry.txt that leaves the reader curious."""

import os

TEXT = (
    "You have passed the same stranger on the stairs three times this week. "
    "Today he smiled \u2014 not at you, but at the space just behind "
    "your shoulder. When you turned around, the stairwell was empty. "
    "He was still smiling."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
