import random
n=random.randint(1,100)
print("guess no btw 1 to 100")    
attempt = 0
some = 10

for i in range(attempts,some+1):
    game = int(input("guess no"))
    attempt += 1
    if game >n:
        print("high")
    elif game <n:
        print("less")
    elif game ==n
