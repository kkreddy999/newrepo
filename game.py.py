import random
s=random.randint(1,100)
attempt=0
max_attempt=10

for i in range(attempt, max_attempt):
    m=int(input("enter the random number"))
    attempt+=1
    if m > s:
        print("too high")
    elif m < s:
        print("too low")
    elif m == s:
        print("your guess was correct")
    
else:
    print("game over",s ,"correct value")    