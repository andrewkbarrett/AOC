puzzle_text_path = 'input.txt'
data = []

with open(puzzle_text_path) as file: 
	data = [line.rstrip('\n') for line in file]

full_set = []

t_set = []
for e in data:

    if e != '':
        t_set.append(e)
    if e == '':
        full_set.append(t_set)
        t_set = []

Top1 = 0
Top2 = 0
Top3 = 0

for s in full_set:
    
    temp_tot = sum([int(i) for i in s])
    if temp_tot > Top1:
        Top3 = Top2
        Top2 = Top1
        Top1 = temp_tot
        
    elif temp_tot > Top2:
        Top3 = Top2
        Top2 = temp_tot
        
    elif temp_tot > Top3:
        Top3 = temp_tot
    

print(f"Top 1 {Top1}, Top 2 {Top2}, Top 3 {Top3}")
print(sum([Top1,Top2,Top3]))
    