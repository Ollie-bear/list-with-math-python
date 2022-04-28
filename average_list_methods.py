numlist = list()
while True :
    inp = input('Enter a number one by one and type done when you are done')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)
    
print(sum(numlist) / len(numlist))