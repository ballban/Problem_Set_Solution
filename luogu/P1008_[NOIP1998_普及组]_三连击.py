check = 1*2*3*4*5*6*7*8*9

for a in range(123,333):
    if '0' in str(a):
        continue
    
    result = 1
    for i in range(1,4):
        for j in str(a * i):
            result *= int(j)

    if result == check:
        print(a, a * 2, a * 3)
