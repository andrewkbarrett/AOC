from collections import Counter
 
class card:
    def __init__(self,cards,play,multiplier):
        self.cards = cards
        self.play = play
        self.multiplier = multiplier
        self.rank = 0
        self.others = []
        self.onespot = faceconvert(cards[0])
        self.twospot = faceconvert(cards[1])
        self.threespot = faceconvert(cards[2])
        self.fourspot = faceconvert(cards[3])
        self.fivespot = faceconvert(cards[4])

    def __str__(self):
        return f"card: {self.cards} play:{self.play} multiplier:{self.multiplier} rank:{self.rank} spots:{self.onespot,self.twospot,self.threespot,self.fourspot,self.fivespot} other: {self.others}"
    def incrRank(self):
        self.rank += 1
    def addothers(self,val):
        self.others.append(val)
    def handconvert(self,val):
        posarray = []
        for char in val:
            posarray.append(faceconvert(char))
        
    def runrankings(self):
        #selection sort
        setofcards = []
        setofcards.append((self.handconvert(self.cards)))
        for x in self.others:
            setofcards.append((self.handconvert(x)))
        return(sorted(setofcards))
    
    def faceconvert(f):
        if f == 'A':
            return 14
        elif f == 'K':
            return 13
        elif f == 'Q':
            return 12
        elif f == 'J':
            return 11
        elif f == 'T':
            return 10
        else:
            return int(f)
 
puzzle_text_path = 'example.txt'
data = []
 
with open(puzzle_text_path) as file:
    data = [line.rstrip('\n') for line in file]
 
def faceconvert(f):
    if f == 'A':
        return 14
    elif f == 'K':
        return 13
    elif f == 'Q':
        return 12
    elif f == 'J':
        return 11
    elif f == 'T':
        return 10
    else:
        return int(f)
 
def handcheck(firsthand,secondhand):
    print(firsthand,secondhand)
    fh = [faceconvert(x) for x in firsthand]
    sh = [faceconvert(x) for x in secondhand]
    print(fh,sh)
    counter = 0
    for x in fh:
        if x == sh[counter]:
            counter += 1
        if x > sh[counter]:
            return fh
        elif sh[counter] > x:
            return sh
 
cardrank = []
for row in data:
    hand,multi = row.split(' ')
    dl= list(Counter(hand).keys())
    cl = list(Counter(hand).values())
    play = ""
    #rank = 0
    #flush
    if len(dl) == 1:
        play = "flush"
       # rank = 1
    #four of kind
    elif len(dl) == 2 and (4 in cl and 1 in cl):
        play = "4 of a kind"
        #rank = 2
    #Full house
    elif len(dl) == 2 and (3 in cl and 2 in cl):
        play = "Full House"
     #   rank = 3
    elif len(dl) == 3 and (3 in cl and 1 in cl):
        play = "3 of a kind"
      #  rank = 4
    elif len(dl) == 3 and (2 in cl and 1 in cl) and len(cl) == 3:
        play = "2 pair"
       # rank = 5
    elif len(dl) == 4 and (2 in cl and 1 in cl) and len(cl) == 4:
        play = "pair"
        #rank = 6
    elif len(dl) == 5:
        play = "highcard"
       # rank = 7
    cardrank.append(card(hand,play,int(multi)))


hc = [x for x in cardrank if x.play == 'highcard']
if len(hc) == 1:
    hc[0].incrRank()
elif len(hc) > 1:
    print(hc.sort())

pair = [x for x in cardrank if x.play== 'pair']
print(pair)
if len(pair) == 1:
    pair[0].incrRank()
elif len(pair) > 1:
    print(pair.sort())

twopair = [x for x in cardrank if x.play == '2 pair']
cards = []
if len(twopair) > 1:
    for c in twopair:
        cards.append(c.cards)
for c in twopair:
    c.others = [x for x in cards if x != c.cards]

for c in cardrank:
    c.runrankings()
    print(str(c))


'''
pair2 = []
highcard = []
pair = []
three = []
four = []
FH = []
flush = []
 
for c in cardrank:
    
    print(c[2])
    if c[2] == '2 pair':
        if len(pair2) == 1:
            if handcheck(pair2[0][0],card[0]) == card[0]:
                #pair2.clear()
                pair2.append(card)
        else:
            card.append(1)
            pair2.append(card)
    elif card[2] == 'highcard':
        if len(highcard) == 1:
            if handcheck(highcard[0][0],card[0]) == card[0]:
                #highcard.clear()
                highcard.append(card)
        else:
            highcard.append(card)
    elif card[2] == 'pair':
        if len(pair) == 1:
            if handcheck(pair[0][0],card[0]) == card[0]:
                pair.clear()
                pair.append(card)
        else:
            pair.append(card)
    elif card[2] == '3 of a kind':
        if len(three) == 1:
            if handcheck(three[0][0],card[0]) == card[0]:
                three.clear()
                three.append(card)
        else:
            three.append(card)
    elif card[2] == 'Full House':
        if len(FH) == 1:
            if handcheck(FH[0][0],card[0]) == card[0]:
                FH.clear()
                FH.append(card)
        else:
            FH.append(card)
    elif card[2] == '4 of a kind':
        if len(four) == 1:
            if handcheck(four[0][0],card[0]) == card[0]:
                four.clear()
                four.append(card)
        else:
            four.append(card)
    elif card[2] == 'flush':
        if len(flush) == 1:
            if handcheck(flush[0][0],card[0]) == card[0]:
                flush.clear()
                flush.append(card)
        else:
            flush.append(card)
 
completecardset.append(pair2)
completecardset.append(highcard)
completecardset.append(pair)
completecardset.append(three)
completecardset.append(four)
completecardset.append(FH)
completecardset.append(flush)
 
print(completecardset)
'''