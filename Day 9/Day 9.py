from pathlib import Path
import copy

raw = Path('Day 8\input.txt').read_text()
#raw = Path('Day 8\\test.txt').read_text()
raw = raw.strip()
raw = raw.split("\n")

length = len(raw)
