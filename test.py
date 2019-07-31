s = input()
l=[]
cs = len(s)
j=1
while s != "" and j < cs-1:
    for i in range(0,(cs-1)):
    	if i % 2 == 0:
        	l.append(s[0:cs-i])
		else:
			l.append(s[0:cs-i]::-1)
	s=s[::-1]
	s=s[j:]
	j = j+1    
print(l)
l = list(dict.fromkeys(l))
print(l)
print(len(l)-1)
