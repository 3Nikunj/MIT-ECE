map = [
    [0,2,0,9,7,0,0],
    [0,0,0,12,0,0,10],
    [0,0,0,0,0,3,0],
    [0,0,5,0,0,0,19],
    [0,0,2,6,0,0,0,],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,9,0]
]
i = 0 
while True:
    min_val = 9999
    for j in range(7):   
        if map[i][j]!=0 and map[i][j]<min_val:
            min_val = map[i][j]
            min_index = j
    i = min_index
    if map[i].count(0) == 7:
        break

# lt = [0,0,0,0,0,0,0]
# del lt[0]
# print(lt)