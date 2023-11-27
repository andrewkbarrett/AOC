from aocd.models import Puzzle
from aocd.examples import Example
from rich import print as rprint

puzzle = Puzzle(year=2022, day=11).examples[0]
Monkeytext = Example(puzzle).input_data[0]

x = {"Monkies": {}}

Monkey = ""
for line in Monkeytext.splitlines():
    if line.startswith("Monkey"):
        Monkey = line[-2:8]
        x["Monkies"][Monkey] = {}

    else:
        
        ln = line.split(':')
        if ln == ['']:
            pass
        else:
            x["Monkies"][Monkey][f"{ln[0]}".strip()] = ln[1].strip()


for monkey in x["Monkies"]:
    rprint(x['Monkies'][monkey]['Operation'])


