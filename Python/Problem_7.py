def Problem_7():
    i = 2
    curNum = 3
    l = []
    while(i != 10001):
        curNum+=2
        i+=1
        for j in range(2,int(curNum**0.5)+1):
            if(curNum%j==0):
                i-=1
                break

    return curNum

print(Problem_7())
#ANSWER: 104743
