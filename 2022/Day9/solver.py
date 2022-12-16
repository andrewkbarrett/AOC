puzzle_text_path = 'input.txt'
data = []


def movedown(coord1,coord2,steps):
    x1 = coord1[0]
    y1 = coord1[1]
    x2 = coord2[0]
    y2 = coord2[1]

    tailmovements = []
    #x1 -= 1
    for step in range(steps):
        #head moves
        x1 -= 1

        #tail moves or doesn't
        if y1 == y2:
            #head/tail on same plan, just move
            #only move if the head moves more than 1 away from the tail
            if abs(x2-x1) > 1:
                x2 -= 1
                tailmovements.append((x2,y2))
        elif y1 < y2 and (abs(x1-x2) <= 1 ):
            #tail is right of head
            pass #tail is still within 1 unit from head - just diagonally. 

        elif y1 < y2 and (abs(x1-x2) > 1 ):
            #Now tail needs to move left to the y plane to match head and increment 1
            y2 -=1
            x2 -=1
            tailmovements.append((x2,y2))
        elif y1 > y2 and (abs(x1-x2) <= 1 ):
            #tail is left of head
            pass #tail is still within 1 unit from head - just diagonally. 
        elif y1 > y2 and (abs(x1-x2) > 1 ):
            #Now tail needs to right to the y plane to match head and increment 1
            y2 +=1
            x2 -=1
            tailmovements.append((x2,y2))
    return([x1,y1],[x2,y2], tailmovements)  
   
        
def moveup(coord1,coord2,steps):
    x1 = coord1[0]
    y1 = coord1[1]
    x2 = coord2[0]
    y2 = coord2[1]

    tailmovements = []
    for step in range(steps):
        #head moves
        x1 += 1

        #tail moves or doesn't
        if y1 == y2:
            #head/tail on same plan, just move
            #if and only if, the movement takes the tail > 1 away from the head
            if abs(x2-x1) > 1:
                x2 += 1
                tailmovements.append((x2,y2))
        elif y1 < y2 and (abs(x1-x2) <= 1 ):
            #tail is right of head
            pass #tail is still within 1 unit from head - just diagonally. 

        elif y1 < y2 and (abs(x1-x2) > 1 ):
            #Now tail needs to move left to the y plane to match head and increment 1
            #print("tail is right of head, needs to move")
            y2 -=1
            x2 +=1
            tailmovements.append((x2,y2))
        elif y1 > y2 and (abs(x1-x2) <= 1 ):
            #tail is left of head
            pass #tail is still within 1 unit from head - just diagonally. 
        elif y1 > y2 and (abs(x1-x2) > 1 ):
            #Now tail needs to right to the y plane to match head and increment 1
            #print("tail is left of head, needs to move")
            y2 +=1
            x2 +=1
            tailmovements.append((x2,y2))
    return([x1,y1],[x2,y2], tailmovements)  

def moveright(coord1,coord2,steps):
    x1 = coord1[0]
    y1 = coord1[1]
    x2 = coord2[0]
    y2 = coord2[1]

    tailmovements = []

    for step in range(steps):
        #head moves
        y1 += 1
        
        #tail moves or doesn't
        if x1 == x2:
            #head/tail on same plan, just move
            if abs(y2-y1) > 1:
                y2+= 1
                tailmovements.append((x2,y2))
        elif x1 < x2 and (abs(y1-y2) <= 1 ):
            #tail is above head
            pass #tail is still within 1 unit from head - just diagonally. 
        elif x1 < x2 and (abs(y1-y2) > 1 ):
            #Now tail needs to move down to the x plane to match head and increment 1
            x2 -=1
            y2 +=1
            tailmovements.append((x2,y2))
        elif x1 > x2 and (abs(y1-y2) <= 1 ):
            #tail is below head
            pass #tail is still within 1 unit from head - just diagonally. 
        elif x1 > x2 and (abs(y1-y2) > 1 ):
            #Now tail needs to move up to the x plane to match head and increment 1
            x2 +=1
            y2 +=1
            tailmovements.append((x2,y2))
    return([x1,y1],[x2,y2], tailmovements)  

def moveleft(coord1,coord2,steps):
    x1 = coord1[0]
    y1 = coord1[1]
    x2 = coord2[0]
    y2 = coord2[1]

    tailmovements = []

    for step in range(steps):
        #head moves
        y1 -= 1

        #tail moves or doesn't
        if x1 == x2:
            #head/tail on same plan, just move
            if abs(y2-y1) > 1:
                y2 -= 1
                tailmovements.append((x2,y2))
        elif x1 < x2 and (abs(y2-y1) <= 1 ):
            #tail is above head
            pass #tail is still within 1 unit from head - just diagonally. 
        elif x1 < x2 and (abs(y2-y1) > 1 ):
            #Now tail needs to move down to the x plane to match head and increment 1
            x2 -=1
            y2 -=1
            tailmovements.append((x2,y2))
        elif x1 > x2 and (abs(y2-y1) <= 1 ):
            #tail is below head
            pass #tail is still within 1 unit from head - just diagonally. 
        elif x1 > x2 and (abs(y2-y1) > 1 ):
            #Now tail needs to move up to the x plane to match head and increment 1
            x2 +=1
            y2 -=1
            tailmovements.append((x2,y2))
    return([x1,y1],[x2,y2], tailmovements)  

  
with open(puzzle_text_path) as file: 
	data = [line.rstrip('\n') for line in file]
    
moves = [x.split(' ') for x in data]
head = [0,0]
tail = [0,0]
tt = [(0,0)]

for move in moves:
    
    if move[0] == 'R':
        mc = int(move[1])
        newpack = moveright(head,tail,mc)
        head = newpack[0]
        tail = newpack[1]
        nv = tt + newpack[2]
        tt = nv

    if move[0] == 'U':
        mc = int(move[1])
        newpack = moveup(head,tail,mc)
        head = newpack[0]
        tail = newpack[1]
        nv = tt + newpack[2]
        tt = nv

    #moving left across the y-axis - x will stay the same
    if move[0] == 'L':
        mc = int(move[1])
        newpack = moveleft(head,tail,mc)
        head = newpack[0]
        tail = newpack[1]
        nv = tt + newpack[2]
        tt = nv
   
    if move[0] == 'D':
        mc = int(move[1])
        newpack = movedown(head,tail,mc)
        head = newpack[0]
        tail = newpack[1]
        nv = tt + newpack[2]
        tt = nv


dtt = []

for x in tt:
    if x not in dtt:
        dtt.append(x)

print(len(dtt))
