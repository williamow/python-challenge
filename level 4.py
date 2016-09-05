import requests
import re
print("let's wreck level four!")
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
num = "12345"
num = "8022"
while True:
    page = requests.post(url % num)
    match = re.search("nothing is (\d+)", page.text)
    print(match)
    if (match == "None"):
        print("Hi!")
        break
    else:
        num = match.group(1)
        print(num)
