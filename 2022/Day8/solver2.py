import pandas as pd
puzzle_text_path = 'input.txt'
data = []

with open(puzzle_text_path) as file: 
	data = [line.rstrip('\n') for line in file]

def checkScore (valtocheck, arrytosearch):
    retval = 0
    for vals in arrytosearch:
        if valtocheck > vals:
            retval += 1
        if valtocheck == vals:
            retval += 1
            break
        if valtocheck < vals:
            retval +=1 
            break
   
    #print(f"{valtocheck} in {arrytosearch} - hit? {retval}")

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

MaxScore = 0
startr = 0
while startr < rows:
    rw = x.loc[startr]
    startc = 0
    for r in rw:
        if startr == 0 or startr == rows - 1:
            pass
        elif startc == 0 or startc == cols -1:
            pass
        else:
            #check up
            #UpCount = checkScore(x.iloc[startr,startc], x.iloc[:startr,startc].values.tolist(), "up")
            UpArray = x.iloc[:startr,startc].values.tolist()
            UpArray.reverse()
            UpCount = checkScore(x.iloc[startr,startc],UpArray)
            print(f"UP sr/sc{startr}/{startc} - array {UpArray} - for val {x.iloc[startr,startc]} - Score {UpCount}")

            #check down
            #DownCount = checkScore(x.iloc[startr,startc], x.iloc[startr+1:,startc].values.tolist(), "down")
            DownArray = x.iloc[startr+1:,startc].values.tolist()
            DownCount = checkScore(x.iloc[startr,startc], DownArray)
            print(f"DOWN sr/sc{startr}/{startc} - array {DownArray} - for val {x.iloc[startr,startc]} - Score {DownCount}")

            #check right
            RightArray = x.iloc[startr,startc+1:].values.tolist()
            RightCount = checkScore(x.iloc[startr,startc], RightArray)
            print(f"Right sr/sc{startr}/{startc} - array {RightArray} - for val {x.iloc[startr,startc]} - Score {RightCount}")

            #check left
            LeftArray = x.iloc[startr,:startc].values.tolist()
            LeftArray.reverse()
            LeftCount = checkScore(x.iloc[startr,startc], LeftArray)
            print(f"Left sr/sc{startr}/{startc} - array {LeftArray} - for val {x.iloc[startr,startc]} - Score {LeftCount}")
            
            score = UpCount * LeftCount * DownCount * RightCount
            print(f"Row: {startr} Col: {startc} - score {UpCount, LeftCount, DownCount, RightCount}")
            
            if score > MaxScore:
                MaxScore = score
        startc += 1
        
    startr += 1
    
    
print(MaxScore)
#print(x.iloc[:, 0])
#print(x.loc[0])