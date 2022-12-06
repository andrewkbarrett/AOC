puzzle_text_path = 'input.txt'
data = []

with open(puzzle_text_path) as file: 
	data = [line.rstrip('\n') for line in file]
def checkBatch(arry):
    num_values = len(set(arry))
    if num_values == 4:
        return True
    else:
        return False

currentbatch = []
cntr = 0

for let in data[0]:
    if cntr < 5:
        currentbatch.append(let)
        cntr += 1
    #print(currentbatch)
    elif cntr >= 4:
        currentbatch.pop(0)
        currentbatch.append(let)
        x = checkBatch(currentbatch)
        if x == True:
            print(currentbatch)
            print(f"found! {cntr}")
            break
        
        cntr += 1


