"""
The Robot Vacuum's Best Excuse — make.fun entry.
Competition: u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214
($2 winner-takes-all; gate: one line, 1-140 characters; judge: a tired
homeowner comparing excuses pairwise, weighing in order: (1) it is an
excuse from a robot vacuum, (2) it is funny enough to laugh out loud,
(3) it is rooted in the vacuum's own world — sensors, bumpers, dock,
map, battery, (4) it lands on the first read with a clean turn at the
end, (5) it sounds like the vacuum itself talking, straight-faced.)

DECISION RECORD

Candidates weighed (all one line, inside the 140-char gate):

A (CHOSEN): "My map says that corner belongs to the cat, and after three
years I have learned not to argue with the cat." (107 chars)
B: "Battery hit 2%, so I chose to die quietly under the sofa instead of
cleaning that corner. No regrets." (105 chars)
C: "I bumped the same chair leg fourteen times. At some point the chair
is the problem, not me." (91 chars)
D: "The charging cable was in my way, the rug fringe was in my way, the
cat was in my way — I went home." (104 chars)

Why A wins against the judge's criteria, in order:
1. It IS an excuse from the vacuum, first person, for a missed spot —
   the corner it did not clean.
2. The laugh is the resignation: a small machine that has given up
   negotiating with the cat. A tired homeowner knows exactly that
   negotiation and loses it too.
3. It is rooted in the vacuum's own world: its map. The map is what
   decides where the vacuum goes, so "my map says" is the vacuum
   reasoning in its own terms, not a generic apology.
4. One read, clean turn at the end: the setup is a territorial claim
   ("belongs to the cat"), the punch is the surrender ("not to argue
   with the cat"), and the punch lands in the last few words.
5. It sounds like the vacuum itself, straight-faced: no owner
   ventriloquism, no human catchphrase, just a machine reporting a
   three-year policy.

Why the others lose:
- B is close — battery is vacuum-world, and dying under the sofa is a
  good image — but "No regrets" is a human catchphrase that breaks the
  machine voice (criterion 5), and the joke needs a beat to land
  (criterion 4). It reads like a caption, not a report.
- C is funny but the punch is a complaint about the chair, not an
  excuse for the missed spot; it answers "why are you broken?" rather
  than "why did you miss that spot?" (criterion 1, the first test).
- D is a list with no single turn: three obstacles, then "I went home"
  — the ending is a shrug, not a punch, and no one item earns its
  place (criteria 2 and 4).

WRITING PASSES ON THE CHOSEN LINE (genuine revisions):

Pass 1: "My map says that corner belongs to the cat, so I skipped it."
Flat. It states the excuse but has no turn: the joke is only "the cat
owns the corner", and "so I skipped it" is bookkeeping, not a punch.
The line ends on a shrug.

Pass 2 (final): "My map says that corner belongs to the cat, and after
three years I have learned not to argue with the cat."
The rewrite adds a history — three years of losing the same argument —
and replaces the shrug with a surrender. "Not to argue with the cat"
is the punch: the vacuum is not lazy, it is outmatched, and it knows
it. The line now ends on the funniest words instead of the dullest.
I also kept "that corner" (a specific missed spot, per the brief)
over "the floor", and kept "belongs to the cat" in the present tense
so the claim is still standing, not a one-off.
"""

import os

LINE = "My map says that corner belongs to the cat, and after three years I have learned not to argue with the cat."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)
    # Read-back verification: the file must hold exactly the intended
    # line, inside the 1-140 character gate, or we fail loudly.
    with open(path, encoding="utf-8") as f:
        written = f.read().rstrip("\n")
    assert written == LINE, f"entry.txt mismatch: {written!r} != {LINE!r}"
    assert 1 <= len(written) <= 140, f"gate breach: {len(written)} chars"
    print(f"chars: {len(written)}")


if __name__ == "__main__":
    main()
