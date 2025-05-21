n = input("enter the list")
m =list(map(int,n.split(',')))
print(m)
s=[]
for i in m:
    if i not in s:
        s.append(i)
print(f"not repeated {s}")
 
s.sort()
s.reverse()
print(s)
 
sum_two_no = s[0] + s[-1]
s.insert(1,sum_two_no)
print(f"two elements {s}")
s.reverse()
print(f"final list {s}")