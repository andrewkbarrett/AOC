puzzle_text_path = 'example.txt'
data = []

with open(puzzle_text_path) as file: 
	data = [line.rstrip('\n') for line in file]

open = ['<','{','[','(']
closed = ['>','}',']',')']

def giveOpenpair(ch):
    if ch == "]":
        return "["
    if ch == "}":
        return "{"
    if ch == ">":
        return "<"
    if ch == ")":
        return "("

for line in data:
    chpos = 0
    ol = []     
    for ch in line:
        chpos += 1
        
        if [s for s in open if ch in open]:
            ol.append(ch)
            #d[ch]["open"] = d[ch]["open"] +1
        if [s for s in closed if ch in closed]:
            if ol[-1] == giveOpenpair(ch):
                ol.pop()
            if ol[-1] != giveOpenpair(ch):
                print(f"{line} - {ch} - error!")
                break
            #d[giveOpenpair(ch)]["closed"] = d[giveOpenpair(ch)]["closed"]+1
            
            #curCount = d.get(giveOpenpair(ch))
            #if curCount == 0:
            #    print(f"char char - {ch}")
            #print(sum([s for s in open if giveOpenpair(ch) in open]))
            #if sum([s for s in open if giveOpenpair(ch) in open]) % 2 != 0:
            #    print(f" {ch} - error!")
    