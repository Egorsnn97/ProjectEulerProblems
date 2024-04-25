def Problem_3():
    l = 0
    for i in range(100,1000):
        for j in range(100,1000):
            if(str(i*j) == str(i*j)[::-1] and i*j>l):
                print(i,j)
                l = i*j
    return l

print(Problem_3())
#ANSWER:906609
#913*993=906609
