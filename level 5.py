print("Level 5 is terrible!")
import requests, pickle

page = requests.get("http://www.pythonchallenge.com/pc/def/banner.p")
stuf = page.text
obj = pickle.load(stuf)
print(obj)
