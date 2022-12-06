puzzle_text_path = 'input.txt'
data = []

with open(puzzle_text_path) as file: 
	data = [line.rstrip('\n') for line in file]

def checkBatch(arry):
    num_values = len(set(arry))
    if num_values == 14:
        return True
    else:
        return False

currentbatch = []
cntr = 1

for let in data[0]:
    print(f"cntr = {cntr} let = {let}")
    if cntr < 15:
        currentbatch.append(let)
        cntr += 1
    elif cntr > 14:
        currentbatch.pop(0)
        currentbatch.append(let)
        x = checkBatch(currentbatch)
        print(currentbatch)
        if x == True:
            print(currentbatch)
            print(f"found! {cntr}")
            break
        
        cntr += 1


