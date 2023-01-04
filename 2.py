
def deleted_counter(x):
    x = str(x)
    l = []
    for i in range(len(x)):
        l.append(x[i])

    c = 0
    for j in range(len(x)-1):
        if x[j] == 'A' and x[j+1] == 'A' :
            c +=1
        if x[j] == 'B' and x[j+1] == 'B' :
            c+=1


    print(c)


k = input()
deleted_counter(k)