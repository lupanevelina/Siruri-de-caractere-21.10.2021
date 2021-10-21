s=str(input("Dati sirul S: "))
#a
for i in range(0,len(s)):
    aa=s.count("A")
print("a)",aa)
#b
for i in range(0,len(s)):
    x=s.replace("A","*")
print("b)",x)
#c66
for i in range(0,len(s)):
    y=s.replace("B","")
print("c)",y)
#d
for i in range(0,len(s)):
    n=s.count("MA")
print("d)",n)    
#e
for i in range(0,len(s)):
    w=s.replace("MA","TA")
print("e)",w)    
#f
for i in range(0,len(s)):
    p=s.replace("TO","")
print("f)",p)  
#g
u=len(s)
g=s[u::-1]
print("g)",g)
