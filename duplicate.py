n = input()
num = list(map(int, n.split(',')))
m = len(num)
for i in range(m):
   for j in range(i+1 , m):
       if num[i] == num[j]:
           print("Dup ---", num[i])
           break 