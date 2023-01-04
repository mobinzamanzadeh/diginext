

def counter_a(x,y):
    x = str(x)
    y = int(y)
    n = int(len(x))
    l = [] 
    while int(len(l)) != y :
        for i in range(n):
            l.append(x[i])

            if int(len(l)) == y:
                break
    
    c = l.count('a')
        
    print(c)

k = input()
h = input()
counter_a(k,h)



