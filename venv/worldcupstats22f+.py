# Assignment
# Fetch Data from espn cric info and analyze world cup stats :)

import requests
from bs4 import BeautifulSoup # External Library for Parsing HTML Data
import matplotlib.pyplot as plt

url = "http://stats.espncricinfo.com/ci/engine/records/team/match_results.html?id=12357;type=tournament"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

tags = soup.find_all("th", class_="title")
# tags = soup.find_all( class_="engineTable")
print(tags)

# print(soup.title.text)
# print("==========")
# print()

# data = { "team1": Team_1,
#           "team2": Team2,
#           "winner": Winner,
#             "Margin": Margin,
#             "ground played on": Ground,
#             "match date": MatchDate,
#             "scorecard": Scorecard
#          }
#
# frame = pd.DataFrame(data)
# print("==============")
# print(frame)
# print("==============")