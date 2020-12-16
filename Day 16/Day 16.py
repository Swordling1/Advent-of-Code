from pathlib import Path
import copy

raw = Path('Day 16\input.txt').read_text()
#raw = Path('Day 16\\test.txt').read_text()
raw = raw.strip()
raw = raw.split("\n\n")

length = len(raw)
