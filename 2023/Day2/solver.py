#puzzle_text_path = 'example.txt'
puzzle_text_path = 'input.txt'

with open(puzzle_text_path) as file: 
	data = [line.rstrip('\n') for line in file]

maxVals = {"green": 13, "red": 12, "blue": 14}
currvals = {}

possibleIDs = []
for game in data:
    ValidGame = True
    gameID,plays = game.split(":")
    currvals[gameID] = {"green": 0, "red": 0, "blue": 0}
    for play in plays.split(";"):
        for draw in play.split(","):
            amt,color = draw.strip().split(" ")
            currvals[gameID][color] = amt

            if int(currvals[gameID][color]) > int(maxVals[color]):
                print("game is invalid, ID will not be appended")
                ValidGame = False
                break
        
    if ValidGame == True:
         possibleIDs.append(int(gameID.split(' ')[1])) 

print(possibleIDs)        
print(sum(possibleIDs))
