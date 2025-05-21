def find_pairs(arr, target):
   s = set()
   pair = set()
   for i in arr:
       diff = target - i
       if diff in s:
           pair.add(tuple(sorted((i, diff))))
       s.add(i)
   if pair:
       for p in pair:
           print(p)
   else:
       print("No pairs")
n = input("")
arr = list(map(int, n.split(',')))
target = int(input("sum: "))
find_pairs(arr, target)