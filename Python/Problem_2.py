def Problem_2():
    summ = 0
    a = 1
    b = 2
    while(b < 4000000):
        if(b % 2 == 0):
            summ+=b
        a,b=b,a+b
    return summ
print(Problem_2())
#ANSWER: 4613732
