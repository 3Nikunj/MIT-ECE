lt = [45, 63, 78, 96, 12, 36, 85, 12, 36, 79, 45]
window_size = 3
sum = lt[0]+lt[1]+lt[2]
n = len(lt)
new_sum = sum 
for i in range(1,n-2):
    #print(lt[i],lt[i+1],lt[i+2])
    new_sum = new_sum - lt[i-1] + lt[i+2]
    if sum < new_sum:
        p = [i, i+1, i+2]
        sum = new_sum 
print(sum)
print(p)
