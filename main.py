from pathlib import Path

files = Path().glob("*.txt")
lines_count = 0

for file in files:
    with open(file) as fp:
        for line in fp:
            if not line.strip():
                continue
            lines_count += 1

print(lines_count)
