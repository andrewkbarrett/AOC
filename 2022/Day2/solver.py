puzzle_text_path = 'input.txt'
data = []

with open(puzzle_text_path) as file: 
	data = [line.rstrip('\n') for line in file]
"""
A=Rock
B=Paper
C=Scissors

X=ROCK
Y=Paper
Z=Scissors

(1 for Rock, 2 for Paper, and 3 for Scissors) 
plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
"""
def calcWinPoints(elf,me):
	if (elf == "A" and me == "X") or (elf == "B" and me == "Y") or (elf == "C" and me == "Z"):
		#tie
		if me == "X":
			return 4
		if me == "Y":
			return 5
		if me == "Z":
			return 6		
	if (elf == "C" and me == "X") or (elf == "A" and me == "Y") or (elf == "B" and me == "Z"):
		#win
		if me == "X":
			return 7
		if me == "Y":
			return 8
		if me == "Z":
			return 9		
	if (elf == "C" and me == "Y") or (elf == "A" and me == "Z") or (elf == "B" and me == "X"):
		#loss
		if me == "X":
			return 1
		if me == "Y":
			return 2
		if me == "Z":
			return 3

totScore = 0
for set in data:
	totScore += calcWinPoints(set[:1], set[2:3])

print(totScore)
