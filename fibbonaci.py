 
def f_b(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b
 
num = int(input("Enter number of terms: "))
print(f_b(num))
 
 