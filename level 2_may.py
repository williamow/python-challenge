print("Hello, world!")
s = open("level 2.txt", "r").read()
chars = [[],[]]
for x in range(len(s)):
    for k in range(len(chars)):
        if s[x] == chars[k][0]:
            chars[k][1] = chars[k][1] + 1
            found = True
        else:
            found = False
            break
        if found == False:
            chars[k][0] = s[x]
            chars[k][1] = 1
        else:
            break
        print(chars[k][0],chars[k][1])

