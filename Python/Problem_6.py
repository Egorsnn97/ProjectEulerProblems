def Problem_6():
    return (sum(range(1,101)) * sum(range(1,101)))-sum(i*i for i in range(1,101))

print(Problem_6())
