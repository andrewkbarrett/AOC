import re

#puzzle_text_path = 'example.txt'
#puzzle_text_path = 'example2.txt'
puzzle_text_path = 'input.txt'

def testgame(t,d):
    h=1
    winners = 0
    while h <= t:
        distran = (t-h) * h
        if distran > d and (t-h) < t:
             print(f"winner: dist={distran}, holdtime={h}, time={t-h}" )
             winners += 1
        h+=1
    return winners


with open(puzzle_text_path) as file: 
	data = [l for l in [line.rstrip('\n') for line in file]]

time = re.split(r"\s+(?=[0-9])",data[0])
dist = re.split(r"\s+(?=[0-9])",data[1])

time.remove('Time:')
dist.remove('Distance:')

#time = list(map(int,[l.strip() for l in data[0].split(':')[1].strip().split('  ')]))
#dist = list(map(int,[l.strip() for l in data[1].split(':')[1].strip().split('  ')]))
combo = list(zip(map(int,time),map(int,dist)))
print(combo)
wins = []
for t,d in combo:
    wins.append(testgame(t,d))
total = 1
for x in wins:
     total *= x

print(total)