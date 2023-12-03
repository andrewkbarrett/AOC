from rich import print as rprint

puzzle_text_path = 'example.txt'
#puzzle_text_path = 'example2.txt'
#puzzle_text_path = 'input.txt'

def get_neightbors(r, c,grid):
    neighbors = []
    for dis_r, dis_c in ([-1, 0], [1, 0], [0, -1], [0, 1],[1,-1],[-1,-1],[1,1],[-1,1]):
        r1, c1 = r + dis_r, c + dis_c
        if (c1 > -1 and c1 < len(grid[r])+1) and (r1 > -1 and r1 < len(grid)):
            
            if grid[r1][c1].isnumeric():
                #hit! 
                neighbors.append([r1,c1])
      
    return neighbors

def get_numbers(lofcoords,grid):
    
    numbers = []
    for coords in lofcoords:
        #left - start of line
        if coords[1] == 0:
            tempnumber = ""
            rightwalkCoord = coords[1]
            while True:
                tempnumber = tempnumber+str(grid[coords[0]][rightwalkCoord])
                rightwalkCoord += 1
                if not grid[coords[0]][rightwalkCoord].isnumeric():
                    numbers.append(int(tempnumber))
                    break
        #right - end of line
        elif coords[1] == len(grid[coords[0]]):
            tempnumber = ""
            leftwalkCoord = coords[1]
            while True:
                tempnumber = str(grid[coords[0]][leftwalkCoord])+tempnumber
                leftwalkCoord -= 1
                if not grid[coords[0]][leftwalkCoord].isnumeric():
                    numbers.append(int(tempnumber))
                    break
        else:
            tempnumber = ""
            rightwalkCoord = coords[1]
            leftwalkCoord = coords[1]
            #walkright until . or end of line
            while True:
                tempnumber = tempnumber+str(grid[coords[0]][rightwalkCoord])
                rightwalkCoord += 1
                if rightwalkCoord > len(grid[coords[0]])-1:
                    break
                #print(len(grid[coords[0]]), rightwalkCoord)
                if (not grid[coords[0]][rightwalkCoord].isnumeric()):
                    break
            #walkleft until . or start of line
            while True:
                if tempnumber == "":
                    tempnumber = str(grid[coords[0]][leftwalkCoord])+tempnumber
                leftwalkCoord -= 1
                
                if not grid[coords[0]][leftwalkCoord].isnumeric() or leftwalkCoord < 0:
                    break
                else:
                    tempnumber = str(grid[coords[0]][leftwalkCoord])+tempnumber
            if int(tempnumber) not in numbers:
                numbers.append(int(tempnumber))
    return numbers
     

with open(puzzle_text_path) as file: 
	data = [l for l in [line.rstrip('\n') for line in file]]

data2 = [[l for l in line] for line in data]

arr = 0
hits = []
for line in data2:
    pos = 0
    for char in line:
        if (char != "." and not char.isnumeric()):
              hits.append(get_neightbors(arr,pos,data2))
        pos += 1
    arr += 1

finalSum = 0
for setofCoords in hits:
    numbers = get_numbers(setofCoords,data2)
    print(numbers)
    finalSum += sum(numbers)
print(finalSum)