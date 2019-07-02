import requests
from bs4 import BeautifulSoup
url = "https://twitter.com/dna"
response = requests.get(url)
print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
print("type of soup is: ",type(soup))
print("=============")
#print(soup)
#print(soup.prettify)

print(soup.title.text)
print("==========")
print()

# children = soup.children
# for child in children:
#     print(child)
#     print("=========")

# pTags = soup.find_all("p")
# for tag in pTags:
#     print(tag)
#     print("=============")

divTags = soup.find_all("div")
divTags = soup.find_all("div",class_ ="js-tweet-text-container")
for tag in divTags:
    print(tag)
    print("=============")