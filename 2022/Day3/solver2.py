from enum import Enum
from collections import Counter

class alphtoNum(Enum):
    a = 1   
    b = 2
    c = 3
    d = 4
    e = 5
    f = 6
    g = 7
    h = 8 
    i = 9
    j = 10
    k = 11
    l = 12
    m = 13
    n = 14
    o = 15
    p = 16
    q = 17
    r = 18
    s = 19
    t = 20
    u = 21
    v = 22
    w = 23
    x = 24
    y = 25
    z = 26

puzzle_text_path = 'input.txt'
data = []

with open(puzzle_text_path) as file: 
	data = [line.rstrip('\n') for line in file]

data_get = (y for y in data)
totbatches = len(data) / 3
foundletter = []
while totbatches > 0:
    line1 = next(data_get)
    line2 = next(data_get)
    line3 = next(data_get)
    
    for let in line1:
        l2Cnt = Counter(line2)
        l3Cnt = Counter(line3)
        cnt2 = l2Cnt[let]
        cnt3 = l3Cnt[let]

        if (cnt2 >= 1 and cnt3 >= 1):
            val = 0
            if let.isupper():
                val += 26
            val += alphtoNum[let.lower()].value
            foundletter.append(val)
            break
    
    totbatches -= 1
print(sum(foundletter))

"""
foundletter = []
for x in data:
    totlen = len(x)
    compart =  [x[:int(totlen/2)], x[int(totlen/2):]]
    for let in compart[0]:
        cnt = Counter(compart[1])
        if cnt[let] >= 1:
            val = 0
            if let.isupper():
                val += 26
            val += alphtoNum[let.lower()].value
            foundletter.append(val)
            break
print(sum(foundletter))

"""
