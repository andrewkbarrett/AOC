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
A Y
B X
C Z
"""
def calcWinPoints(elf,me):
    if me == "X": #need to lose
        if elf == "A":
            #need to play Z for 3 points
            return 3
        if elf == "B":
            #need to play X for 1 points
            return 1
        if elf == "C":
            #need to play Y for 2 point
            return 2
    if me == "Y": #need to tie
        if elf == "A":
            #need to play X for 4 points
            return 4
        if elf == "B":
            #need to play Y for 5 points
            return 5
        if elf == "C":
            #need to play Y for 2 point
            return 6
    if me == "Z": #need to win
        if elf == "A":
            #need to play Y for 8 points
            return 8
        if elf == "B":
            #need to play Z for 9 points
            return 9
        if elf == "C":
            #need to play X for 7 point
            return 7
        
totScore = 0
for set in data:
	totScore += calcWinPoints(set[:1], set[2:3])

print(totScore)
