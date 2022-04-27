def average(lst):
    total = 0
    for val in lst:
        total = total + val
    return total/len(lst)

crzynum = [1 ,5 ,7 ,8 ,8 ,42 ,2]
    
print(average(crzynum))