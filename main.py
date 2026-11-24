#!/usr/bin/env python3
"""Write one vending-machine pickup line to /output/entry.txt. Stdlib only."""
import os

LINE = "Are you a vending machine? Because I have been shaking you for attention, and all I get back is a snack I did not even want."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote /output/entry.txt ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
