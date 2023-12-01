from aocd.models import Puzzle
from aocd.examples import Example
from rich import print as rprint

example_block = Puzzle(year=2023, day=1).examples[0]
#example = Example(example_block).input_data[0]

input_text = Puzzle(year=2023, day=1).input_data

digits = []
for line in input_text.splitlines():
    
    firstval = ""
    lastval = ""

    print(line)
    for pos in line:
        if pos.isdigit():
            if firstval == "":
                firstval = pos
            lastval = pos
    digits.append(f"{firstval}{lastval}")

finalsum = 0
for x in digits:
    finalsum += int(x)

print(finalsum)
