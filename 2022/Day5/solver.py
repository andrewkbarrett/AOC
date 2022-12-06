import re
puzzle_text_path = 'input.txt'
data = []

with open(puzzle_text_path) as file: 
	data = [line.rstrip('\n') for line in file]

def remove_items(test_list, item):
    # using list comprehension to perform the task
    res = [i for i in test_list if i != item]
    return res

cargodict = {}

for line in data:
    
    if len(line) == 0:
        break

    totpos = int((len(line) +1 ) / 4)
    
    cntr = 0
    while (cntr < totpos):

        if cargodict.get(cntr+1):
            currentVal = cargodict[cntr+1]
            currentVal.append(line[(cntr*4)+1])
            cargodict.update({cntr+1: currentVal})
        else:
            cargodict.update({cntr+1: [line[(cntr*4)+1]]})
        cntr += 1

for key,value in cargodict.items():
    nl = list(value)
    nl.pop()
    if (' ' in nl):
        nl = remove_items(nl,' ')
    cargodict[key] = nl
    
    

for x in data:
    if x[:4] == "move":
        stacktotouch = int(x[x.index("from ")+5:x.index(" to")])
        Howmanytomove = int(x[x.index("move ")+5:x.index(" from")])
        stacktoaddto = int(x[x.index("to ")+3:])

        movestack = []
        fromstack = cargodict[stacktotouch]
        tostack = cargodict[stacktoaddto]

        while (Howmanytomove > 0):
            n = []
            n.append(fromstack.pop(0))
            movestack = n+movestack
            #movestack.append()
            Howmanytomove -= 1
        newEle = movestack+tostack
        #tostack = movestack.extend(tostack)
        
        cargodict.update({stacktotouch: fromstack})
        cargodict.update({stacktoaddto: newEle})

finallist = ""
for key,value in cargodict.items():
    let = list(value)[0]
    finallist += let
print(finallist)
