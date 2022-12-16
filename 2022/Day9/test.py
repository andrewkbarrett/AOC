
def DistancebetweenCoords(coord1, coord2):
    diffx = 0
    diffy = 0
    if coord1[0] == coord2[0] and coord1[0] == coord2[0]:
        diffx = 0
        diffy = 0
    elif coord1[0] == coord2[0] and coord1[1] != coord2[1]:
        diffy = coord1[1] - coord2[1]
    elif coord1[1] == coord2[1] and coord1[0] != coord2[0]:
        diffx = coord1[0] - coord2[0]
    elif coord1[0] != coord2[0] and coord1[0] != coord2[0]:
        diffy = coord1[1] - coord2[1]
        diffx = coord1[0] - coord2[0]
    return [diffx,diffy]


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
            y2 -= 1
            tailmovements.append([x2,y2])
        elif x1 < x2 and (y2-y1 <= 1 ):
            #tail is above head
            pass #tail is still within 1 unit from head - just diagonally. 
        elif x1 < x2 and (y2-y1 > 1 ):
            #Now tail needs to move down to the x plane to match head and increment 1
            x2 -=1
            y2 -=1
            tailmovements.append([x2,y2])
        elif x1 > x2 and (y2-y1 <= 1 ):
            #tail is below head
            pass #tail is still within 1 unit from head - just diagonally. 
        elif x1 > x2 and (y2-y1 > 1 ):
            #Now tail needs to move up to the x plane to match head and increment 1
            x2 +=1
            y2 -=1
            tailmovements.append([x2,y2])
    return([x1,y1],[x2,y2], tailmovements)  

def movedown(coord1,coord2,steps):
    x1 = coord1[0]
    y1 = coord1[1]
    x2 = coord2[0]
    y2 = coord2[1]

    tailmovements = []

    for step in range(steps):
        #head moves
        x1 -= 1

        #tail moves or doesn't
        if y1 == y2:
            #head/tail on same plan, just move
            x2 -= 1
            tailmovements.append([x2,y2])
        elif y1 < y2 and (x1-x2 <= 1 ):
            #tail is right of head
            pass #tail is still within 1 unit from head - just diagonally. 

        elif y1 < y2 and (x1-x2 > 1 ):
            #Now tail needs to move left to the y plane to match head and increment 1
            print("tail is right of head, needs to move")
            y2 -=1
            x2 -=1
            tailmovements.append([x2,y2])
        elif y1 > y2 and (x1-x2 <= 1 ):
            #tail is left of head
            pass #tail is still within 1 unit from head - just diagonally. 
        elif y1 > y2 and (x1-x2 > 1 ):
            #Now tail needs to right to the y plane to match head and increment 1
            print("tail is left of head, needs to move")
            y2 +=1
            x2 -=1
            tailmovements.append([x2,y2])
    return([x1,y1],[x2,y2], tailmovements)  


coords1 = [5,4]
coords2 = [6,4]

newpack = movedown(coords1,coords2,3)

print(newpack)
"""
possible pos for move right
tail X can be
x > - tail is above head
x<  tail is below head
x = tail is on the same plane
if head is moved right 1 pos - where it was adjacent previous, if above, x decrements and y +
                                                               if below, x increments and y +
                                                               if same, y +
"""
