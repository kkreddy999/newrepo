n = input()
dict = {}
for i in n:
   if i.isdigit():
       if i in dict:
           dict[i] += 1
       else:
           dict[i] = 1
for i in sorted(dict):
   total= dict[i]
   print(i,"---",total)