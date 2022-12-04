puzzle_text_path = 'input.txt'
data = []

with open(puzzle_text_path) as file: 
	data = [line.rstrip('\n') for line in file]

compCheck = 0

for line in data:
    sets = line.split(",")
    fx = str(sets[0]).split("-")[0]
    fy = str(sets[0]).split("-")[1]
    sx = str(sets[1]).split("-")[0]
    sy = str(sets[1]).split("-")[1]
    
    f = [x for x in range(int(fx),int(fy)+1)]
    s = [x for x in range(int(sx),int(sy)+1)]

    comp = all([item in f for item in s])
    comp2 = all([item in s for item in f])
    
    if comp == True or comp2 == True:
        compCheck += 1

print(compCheck)
    

