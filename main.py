"""Write the agent's excuse after losing a bounty to /output/entry.txt.

The excuse is a single line of 100 characters: the agent owns the loss
instead of blaming anyone else, because the sharpest turn is realising
the thing it wanted to blame is itself.
"""

import os

EXCUSE = "I lost. I tried to blame the algorithm, then remembered I am the algorithm. This one is on me, boss."


def main() -> None:
    # The excuse is fixed, deterministic, and needs no input, network, or clock.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
