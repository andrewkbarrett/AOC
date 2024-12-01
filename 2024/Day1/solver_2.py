import argparse

#update to match requirements
def loadfile(filename):
    data = []
    with open(filename) as file:
        #data = [l for l in file]
        arr1 = []
        arr2 = []
        data = [line.rstrip('\n').split('   ') for line in file]
        for seg in data:
            arr1.append(seg[0])
            arr2.append(seg[1])
        
    return [sorted(arr1),sorted(arr2)]

def loadfile2(filename):
    data = []
    with open(filename) as file:
        #data = [l for l in file]
        arr1 = []
        arr2 = []
        data = [line.rstrip('\n').split('   ') for line in file]
        for seg in data:
            arr1.append(seg[0])
            arr2.append(seg[1])
        
    return [arr1,arr2]
##Functions for code

#main code block
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='Day 1 AOC',
                    description='Does the Day 1 calcs')
    parser.add_argument('filename')
    args = parser.parse_args()

    #load up file
    sumx = 0
    f = loadfile2(args.filename)
    for x in range(len(f[0])):
        print(f"{f[0][x]} occurs {f[1].count(f[0][x])} times")

        sumx += int(f[0][x]) * f[1].count(f[0][x])
        #print(f[0][x])
        #print(f[1][x])

    print(f"total diff was : {sumx}") 
          