from collections import OrderedDict
print("Hello, world!")
s = open("level 2.txt", "r").read()
chars=OrderedDict()
for x in s:
    chars[x] = chars.get(x, 0) + 1
for y in chars:
    if chars[y] == 1:
        print(y)
