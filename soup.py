import time
import requests
from bs4 import BeautifulSoup

url = "website.com?xml=1"
result = requests.get(url)

content = result.content
soup = BeautifulSoup(content, "html.parser")

steamID = soup.find_all("x")
print (y)

