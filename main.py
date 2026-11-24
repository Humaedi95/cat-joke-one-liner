"""Cat Joke One-Liner.

Writes a single original one-line joke about cats to /output/entry.txt
(or $OUTPUT_PATH when set). The joke is exactly one line, 1-200 chars.
"""

import os

JOKE = "My cat knocked my glass off the table, watched it shatter, then glared at me like I'd done it."

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    line = JOKE.strip()
    assert "\n" not in line, "joke must be a single line"
    assert 1 <= len(line) <= 200, "joke must be 1-200 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
