import pandas as pd
puzzle_text_path = 'input.txt'
data = []

with open(puzzle_text_path) as file: 
	data = [line.rstrip('\n') for line in file]

def checkVals (valtocheck, arrytosearch):
    
    retval = 1
    for vals in arrytosearch:
        foundMatch = 0
        if valtocheck == vals:
            retval = 0
            break
        if valtocheck < vals:
            retval = 0 
            break
        if valtocheck > vals and foundMatch == 0:
            retval = 1
        else:
            retval = 0
    print(f"{valtocheck} in {arrytosearch} - hit? {retval}")

    return retval

grid = []
for line in data:
    linetoadd = []
    for chr in line:
        linetoadd.append(int(chr))
    grid.append(linetoadd)

x = pd.DataFrame(grid)
rc = x.count()
rows = x.shape[0]
cols = x.shape[1]

totCount = 0
startr = 0
while startr < rows:
    rw = x.loc[startr]
    startc = 0
    for r in rw:
        
        if startr == 0 or startr == rows - 1:
            totCount += 1
        elif startc == 0 or startc == cols -1:
            totCount += 1
        else:
            #meat and taters - check to see the ranges
            #check up
            tempcount = 0
            print(f"Row: {startr} Col: {startc}")
            if checkVals(x.iloc[startr,startc], x.iloc[:startr,startc].values.tolist()) == 1:
                tempcount = 1
            
            #check down
            if checkVals(x.iloc[startr,startc], x.iloc[startr+1:,startc].values.tolist()) == 1:
                tempcount = 1
            
            #check right
            if checkVals(x.iloc[startr,startc], x.iloc[startr,:startc].values.tolist()) == 1:
                tempcount = 1
                
            #check left
            if checkVals(x.iloc[startr,startc], x.iloc[startr,startc+1:].values.tolist()) == 1:
                tempcount = 1

            totCount += tempcount
        startc += 1

    startr += 1
    
print(totCount)
#print(x.iloc[:, 0])
#print(x.loc[0])