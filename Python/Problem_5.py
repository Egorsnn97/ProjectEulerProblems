def Problem_5():
    i = 20
    while(True):
        for j in range(3,21):
            if(i % j != 0):
                break
            elif(j == 20):
                return i
        i += 20

print(Problem_5())
#232792560
