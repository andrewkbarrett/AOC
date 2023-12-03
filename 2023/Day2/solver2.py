from rich import print as rprint
#puzzle_text_path = 'example.txt'
puzzle_text_path = 'input.txt'

with open(puzzle_text_path) as file: 
	data = [line.rstrip('\n') for line in file]

currvals = {}
for game in data:
    ValidGame = True
    gameID,plays = game.split(":")
    currvals[gameID] = {"green": 0, "red": 0, "blue": 0}
    for play in plays.split(";"):
        for draw in play.split(","):
            amt,color = draw.strip().split(" ")
            if currvals[gameID][color] < int(amt):
                currvals[gameID][color] = int(amt)

MultiSum = 0
for game in currvals.items():
    multiplier = int(game[1]['red']) * int(game[1]['green']) * int(game[1]['blue'])
    MultiSum += multiplier
    print(f"gameID: {game[0]} RedMin: {game[1]['red']} GreenMin: {game[1]['green']}  BlueMin: {game[1]['blue']} Multiplier = {multiplier}") 

print(MultiSum)