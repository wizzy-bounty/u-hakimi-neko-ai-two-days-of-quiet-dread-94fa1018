"""Two Days of Quiet Dread entry.

Writes a single-line code review comment that approves a pull request
while carrying quiet existential dread to /output/entry.txt.

Python 3.13 standard library only. No network. Deterministic.
"""

import os

ENTRY = "Approved. One config value, three services, and a quiet Sunday we will never get back."


def pick_output_path() -> str:
    try:
        os.makedirs("/output", exist_ok=True)
        return "/output/entry.txt"
    except OSError:
        os.makedirs("output", exist_ok=True)
        return os.path.join("output", "entry.txt")


def main() -> None:
    path = pick_output_path()
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
