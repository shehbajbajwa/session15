import requests
from bs4 import BeautifulSoup # External Library for Parsing HTML Data
import matplotlib.pyplot as plt

url = "https://www.imdb.com/india/top-rated-indian-movies/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

# tags = soup.find_all("td", class_="titleColumn")
rates = soup.find_all("td", class_="ratingColumn imdbRating")
year = soup.find_all(class_="secondaryInfo")

# movies = []

# for tag in tags:
#     # print(tag.text)
#     # print("------")
#
#     data = tag.text
#     movies.append(data.strip())


# for movie in movies:
#     print(movie)
#     print("*******")

rating = []
for rate in rates:
    d = rate.text
    rating.append(d.strip())
print(rating)
print("========")

years = []
for yr in year:
    dd = yr.text
    years.append(dd.strip())
print(years)
print("==========")

print(rating)
print(years)

plt.bar(rating, years, label="years")
# plt.plot(rating, Y2, label="Y2")


plt.legend() # How can we place legend on different positions -> Explore

plt.xlabel("rating")
plt.ylabel("years")


plt.show()
