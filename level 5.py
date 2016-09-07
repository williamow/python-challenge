print("Level 5 is terrible!")
import requests, pickle

# page = requests.get("http://www.pythonchallenge.com/pc/def/banner.p")
stuf = open("level 5.txt", "r").read()
obj = pickle.load(stuf)
print(obj)
