print("Let's solve level 3!")
d = open("level 3.txt", "r").read()
d = d.replace("\n\r", "")
s = ""
m = d.lower() #all lowercase version
for x in range(0, len(d)):
    if(m[x] == d[x]): #if they are equal, then original was lowercase
        s += "l" #add l or U to create string of uppercase and lowercase
    else:
        s += "U"

#returns number of occurances of pattern within string
c = s.count("lUUUlUUUl") 
print(c)
lc = 10

#returns index of first occurance of the propper uppercase-lowercase pattern
for b in range (0, c):
    a = s.index("lUUUlUUUl") 
    print(a)
    print(d[a+4])
    s = s[(a+3):] #cuts a+3 characters from the front of the string
    
