from rich import print as rprint

def getMinMax(line):
    numbers = [('one','1'),('two','2'),('three','3'),('four','4'),('five','5'),('six','6'),('seven','7'),('eight','8'),('nine','9')]
    positions = []

    for num in numbers:
        pos = 0
        startfrom = 0
        
        while pos > -1:
            pos = line.find(num[0],startfrom)

            if pos != -1:
                positions.append((pos,int(num[1])))
                startfrom = pos+1
        
        pos2 = 0
        startfrom2 = 0
        
        while pos2 > -1:
            pos2 = line.find(num[1],startfrom2)
            
            if pos2 != -1:
                positions.append((pos2,int(num[1])))
                startfrom2 = pos2+1

        if len(positions) == 1:
            positions.append(positions[0])
            
    minpos = (0,0)
    maxpos = (0,0)
    for p in positions:
        if (minpos == (0,0)):
            minpos = p
        elif (p[0] < minpos[0]):
            minpos = p

        if (maxpos == (0,0)):
            maxpos = p
        elif (p[0] > maxpos[0]):
            maxpos = p
    return((minpos[1],maxpos[1]))

#puzzle_text_path = 'example3.txt'
puzzle_text_path = 'input.txt'

with open(puzzle_text_path) as file: 
	data = [line.rstrip('\n') for line in file]

digits = []

for line in data:
    
    points = getMinMax(line)
    digits.append(str(points[0])+str(points[1]))

finalsum = sum(int(x) for x in digits)
print(digits)
print(finalsum)
