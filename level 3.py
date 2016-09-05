print("Let's solve level 3!")
d = open("level 3.txt", "r").read()
d = d.replace("\n\r", "")
s = ""
m = d.lower()
for x in range(0, len(d)):
    if(m[x] == d[x]):
        s += "l"
    else:
        s += "U"

c = s.count("lUUUlUUUl")
print(c)
lc = 10
a = s.index("lUUUlUUUl")
lc += a
print(a)
print(d[a+4])
    
