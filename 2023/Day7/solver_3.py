from collections import Counter
from operator import itemgetter
 
puzzle_text_path = 'example.txt'
data = []

def sortable(r,c):
    arr = []
    arr.append(r)
    for x in c:
        arr.append(x)
    
def cardplay(card):
    dl= list(Counter(card).keys())
    cl = list(Counter(card).values())
    print(dl,cl)
    play = ""
    rank = 0
    jCnt = card.count('J')

    #flush
    if len(dl) == 1:
        play = "flush"
        rank = 7
    elif len(dl) == 2 and jCnt == 1:
        play = "flush"
        rank = 7

    #four of kind
    elif len(dl) == 2 and (4 in cl and 1 in cl):
        play = "4 of a kind"
        rank = 6
    elif len(dl) == 3 and (3 in cl and 1 in cl and jCnt == 1):
        play = "4 of a kind"
        rank = 6
    elif len(dl) == 4 and (2 in cl and jCnt == 2):
        play = "4 of a kind"
        rank = 6
    elif len(dl) == 2 and (1 in cl and jCnt == 3):
        play = "4 of a kind"
        rank = 6
    
    #Full house
    elif len(dl) == 2 and (3 in cl and 2 in cl and jCnt == 0):
        play = "Full House"
        rank = 5
    elif len(dl) == 3 and (3 in cl and 1 in cl and jCnt == 1):
        play = "Full House"
        rank = 5
    elif len(dl) == 3 and (2 in cl and jCnt == 2):
        play = "Full House"
        rank = 5

    elif len(dl) == 3 and (3 in cl and 1 in cl):
        if 'J' in card:
            play = "4 of a kind"
            rank = 6
        else: 
            play = "3 of a kind"
            rank = 4
    elif len(dl) == 3 and (2 in cl and 1 in cl) and len(cl) == 3:
        if 'J' in card:
            play = "3 of a kind"
            rank = 4
        else:
            play = "2 pair"
            rank = 3
    elif len(dl) == 4 and (2 in cl and 1 in cl) and len(cl) == 4:
        if 'J' in card:
            play = "3 of a kind"
            rank = 4
        else:
            play = "pair"
            rank = 2
    elif len(dl) == 5:
        play = "highcard"
        rank = 1
    return rank

with open(puzzle_text_path) as file:
    data = [line.rstrip('\n') for line in file]
 
cardset = []
for line in data:
    x,y = line.split(' ')
    card = []
    print(x)
    play = cardplay(x)

    for char in x:
        if char == 'A':
            card.append(14)
        elif char == 'K':
            card.append(13)
        elif char == 'Q':
            card.append(12)
        elif char == 'J':
            card.append(1)
        elif char == 'T':
            card.append(10)
        else:
            card.append(int(char))
    cardset.append((card,play,y))

#sort1 = sorted(cardset,key=lambda card: card[1][1])
sort1 = sorted(cardset, key=itemgetter(1,0), reverse=False)
print(sort1)
rank = 1
summ =0

for s in sort1:
    print(s,rank)
    for t in range(1,8):
        if s[1] == t:
            if rank == 1:
                summ += int(s[2]) * rank
                print(s)
                rank +=1
            else:
                
                summ += int(s[2]) * rank
                print(s)
                rank += 1
print(summ)