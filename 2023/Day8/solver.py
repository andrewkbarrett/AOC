
puzzle_text_path = 'input.txt'
data = []

with open(puzzle_text_path) as file:
    data = [line.rstrip('\n') for line in file]

direction = [x for x in data[0]]

points = {}

for lin in data[2:]:
    s1 = lin.split('=')
    #print(s1[0].strip())
    tup = s1[1].replace(')','').replace('(','').split(',')
    points[s1[0].strip()] =  [tup[0].strip(),tup[1].strip()]


maxpoints = len(direction)
cntr = 1
Key = 'AAA'
NextKey = ''
moveCount = 0
print(points)
while True:
    
    if cntr > maxpoints:
        cntr = 1
    
    d = direction[cntr-1]
    print(d)
    sett = points[Key]
    print(sett)
    if d == 'R':
        Key = sett[1]
        print(Key)
        moveCount += 1
    if d == 'L':
        Key = sett[0]
        print(Key)
        moveCount += 1
    if Key == 'ZZZ':
        break
    cntr += 1
print(moveCount)

