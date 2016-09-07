print("Level 5 is terrible!")
import requests, pickle

# page = requests.get("http://www.pythonchallenge.com/pc/def/banner.p")
stuf = open("level 5.txt", "r+b")
obj = pickle.load(stuf)
print(obj)
