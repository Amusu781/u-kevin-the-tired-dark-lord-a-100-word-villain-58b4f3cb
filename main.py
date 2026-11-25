"""The Tired Dark Lord -- entry program.

Writes one villain monologue (about 100 words, under 600 characters) to
OUTPUT_DIR/entry.txt. Standard library only, no network, same bytes every run.
"""

import os

MONOLOGUE = (
    "So. You've come for the Ninefold Crown. Put it... no, by the door is fine. "
    "Do you know what holding six provinces takes? Ledgers. Grain counts. "
    "A necromancer who wants Thursdays off. I salted the fields of Varrow myself. "
    "Took a week. Then they wanted them unsalted. My dragon sends his regrets; "
    "he's sulking under the stairs again. Sit, hero. Sit. The prophecy "
    "says we duel at dawn, and it is dawn, and the kettle's just gone. "
    "Draw your blade. Slowly. Slower. Perfect. Now hold it right there while "
    "I close my eyes and plot your doom."
)

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")


def main():
    # Gate: UTF-8 text of 1 to 600 characters, not only white space.
    assert MONOLOGUE.strip() and 1 <= len(MONOLOGUE) <= 600, "monologue fails the gate"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(MONOLOGUE)


if __name__ == "__main__":
    main()
