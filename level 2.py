print("Hello, world!")
s = open("level 2.txt", "r").read()
chars = {}
for x in s:
    chars[x] = chars.get(x, 0) + 1
for y in chars:
    print(y, str(chars[y]))
