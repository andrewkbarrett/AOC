puzzle_text_path = 'input.txt'
data = []

with open(puzzle_text_path) as file: 
	data = [line.rstrip('\n') for line in file]

fulldirectory = {"/": ["",0,0]}

curr_dir = "/"

for line in data:
    chewLine = line.split(" ")
    #print(f"curr dir = {curr_dir}")

    if chewLine[0] == '$':
        #usercommand
        if chewLine[1] == "cd":
            if chewLine[2] == '..':
                #remove out the last dir
                #curr_dir = curr_dir[:curr_dir.index("/",len(curr_dir)-4)]
                if curr_dir == "/":
                    print("Can't go past / ")
                    break
                #move back to parent
                curr_dir = fulldirectory[curr_dir][0] #value in array is root, filecount, sum

            if chewLine[2] != '..':
                #print(chewLine[2])
                if chewLine[2] != '/':
                    dir = f"{curr_dir}{chewLine[2]}/"
                    if (dir not in fulldirectory):
                        fulldirectory.update({dir: [curr_dir,0,0]})

                    curr_dir = dir
                
    elif chewLine[0].isnumeric():
        newfile = int(chewLine[0])
        #tmpset = curr_dir.copy()
        tmpdir = curr_dir
        
        while(tmpdir != ""):
            dir_a = fulldirectory[tmpdir]
            next_dir = fulldirectory[tmpdir][0]
            fc = int(dir_a[1]) + 1
            fs = int(dir_a[2]) + newfile
            
            fulldirectory.update({tmpdir: [next_dir,fc,fs] })
            tmpdir = next_dir
summr = 0
totroot = 70000000 - fulldirectory["/"][2]
listmin = []
for drrc in fulldirectory:
    tst = fulldirectory[drrc][2]
    if totroot + tst >= 30000000 and fulldirectory[drrc] != "/":
        listmin.append(fulldirectory[drrc][2])
#print(fulldirectory)
#print(summr)
print(sorted(listmin))