import pandas as pd
teams = ["Rajasthan Royals",
         "Deccan Chargers",
         "Chennai Super Kings",
         "Chennai Super Kings",
         "Kolkata Knight Riders",
         "Mumbai Indians",
        "Kolkata Knight Riders",
        "Mumbai Indians",
         "Sunrisers Hyderabad",
         "Mumbai Indians",
        "Chennai Super Kings",
         "Mumbai Indians",]
ranks = [2,3,3,5,1,6,1,1,3,4,4,5]
year = [2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]
# print(len(teams))
# print(len(ranks))
# print(len(year))
data1 = { "team": teams,
         "rank": ranks,
         "year": year
        }
data2 = { "team": ["kings","rcb","delhi"],
         "rank": [8,9,5]
          }
frame1 = pd.DataFrame(data1)
frame2 = pd.DataFrame(data2)
print(frame1)
print()
print(frame2)
print("=================================")

frame3 = pd.merge(frame1,frame2, on="team",how="left")
print("=================================")
print(frame3)
frame3 = pd.merge(frame1,frame2, on="team",how="right")
print(frame3)
print("=================================")
frame3 = pd.merge(frame1,frame2, on="team",how="outer")
print(frame3)
print("=================================")
frame3 = pd.merge(frame1,frame2, on="team",how="inner")
print(frame3)
print("=================================")
print(frame3)