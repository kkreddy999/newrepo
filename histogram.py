def pattern(n):
    for i in range(1, 20):
        stars = '*' * n.count(i)
        if stars:
            print(f"{i}: {stars}")
n = list(map(int,input("enter the numbers").split(',')))
print(pattern(n))
 