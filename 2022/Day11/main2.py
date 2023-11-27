from sm import Monkey

from aocd.models import Puzzle
from aocd.examples import Example
from rich import print as rprint

puzzle = Puzzle(year=2022, day=11).examples[0]
#mainpuz = Puzzle(year=2022, day=11).input_data
#Example
#Monkeytext = Example(puzzle).input_data[0]
#part A
Monkeytext = Puzzle(year=2022, day=11).input_data

Monkies = []
ID = 0

for line in Monkeytext.splitlines():
    if line.startswith("Monkey"):
        ID = int(line.split(' ')[1].replace(':',''))
        newMonk = Monkey(ID,"","","","","")
        Monkies.append(newMonk)
        
    else:
        ln = line.split(':')
        if ln == ['']:
            pass
        
        else:
            if ln[0].strip().lower() == "starting items":
                items = [int(z.strip()) for z in ln[1].split(',')]
                Monkies[ID].PackofItems =  items

            elif ln[0].strip().lower() == "operation":
                Monkies[ID].Operation = ln[1].strip().lower()
            elif ln[0].strip().lower() == "test":
                Monkies[ID].Test = ln[1].strip().lower()
            elif ln[0].strip().lower() == "if true":
                Monkies[ID].IftrueTest = ln[1].strip().lower()
            elif ln[0].strip().lower() == "if false":
                Monkies[ID].IffalseTest = ln[1].strip().lower()
    
rounds = 20
while rounds > 0:
    for M in Monkies:
        rprint(f"Monkey - {M.ID}")
        coI = len(M.PackofItems)

        while coI > 0:

            M.getItem()
            #rprint(f"start Operation on Current Item {M.currentItem}...")
            M.OpRun()
            #rprint(f"after Op: {M.opdValue}...")
            sendToMonkey = int(M.runTest())
            #rprint(f"sending package to monkey {sendToMonkey}")
            Monkies[sendToMonkey].additem(M.opdValue)
            #rprint(f"Current Items after run:  {M.PackofItems}")
            coI -= 1
            M.incrHandleCount()

    rounds -= 1

top1 = 0
top2 = 0

for monk in Monkies:
    
    if monk.handleCount > top1:
        top2 = top1
        top1 = monk.handleCount

    if monk.handleCount > top2 and monk.handleCount < top1:
        top2 = monk.handleCount

    #print(f"{monk.ID} top 1:{top1} top2: {top2}")
print(f" answer = {top1 * top2}")
