num = 600851475143
def IsPrime(i):
    for j in range(2,i//2):
        if(i % j == 0):
            return 0
def Problem_3():
    global num 
    while(num != 1):
        for i in range(2,num):
            if(num % i == 0 and IsPrime(i) != 0):
                num /= int(i)
            if(num == 1):
                return i
print(Problem_3())
#6857
