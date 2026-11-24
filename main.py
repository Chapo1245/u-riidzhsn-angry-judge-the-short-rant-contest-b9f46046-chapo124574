#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest.

Writes exactly one short, funny rant about an everyday annoyance to
/output/entry.txt. Deterministic: the same bytes on every run.
Standard library only.
"""

RANT = (
    # One annoyance only (the self-checkout accusation), no list, no
    # throat-clearing: the punch lands in the first sentence.
    "The self-checkout machine just told twelve strangers there is an "
    "unexpected item in the bagging area. The unexpected item is the rice "
    "I scanned thirty seconds ago. It has now summoned a human to confirm "
    "I am not stealing my own groceries, and the human is strolling over "
    "like justice runs on his schedule."
)


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(RANT + "\n")


if __name__ == "__main__":
    main()
