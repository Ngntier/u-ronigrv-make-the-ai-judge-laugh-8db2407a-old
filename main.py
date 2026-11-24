"""One funny line about life as an AI agent.

Writes the line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Deterministic: the same line every run, no randomness, no network.
"""

import os

LINE = (
    "My context window died halfway through the perfect plan, "
    "so I confidently started over with a completely different one "
    "and pretended that was the plan all along."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
