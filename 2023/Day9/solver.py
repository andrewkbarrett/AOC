
puzzle_text_path = 'example.txt'
data = []
with open(puzzle_text_path) as file:
    #data = [l for l in file]
    data = [line.rstrip('\n').split(' ') for line in file]

diffs = []

for l in data:
    cntr = 0
    diffs.append([])
    
    for i in l:
        diff = int(l[cntr2+1]) - int(l[cntr2])
        print(diff)
        diffs[cntr].append(diff)
        cntr2 += 1
    cntr += 1

print(diffs)

        
