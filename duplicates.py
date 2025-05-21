n = input()
if n:  
    s = list(map(int, n.split(',')))
    s.sort()
    
    l = []
    for i in range(1, len(s)):
        if s[i] == s[i - 1] and s[i] not in l:
            l.append(s[i])
    
    print(l)
else:
    print("Input is empty.")