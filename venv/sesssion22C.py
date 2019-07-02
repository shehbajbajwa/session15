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
data = { "team": teams,
         "rank": ranks,
         "year": year
        }

frame = pd.DataFrame(data)
# frame = pd.DataFrame({ "team": teams,
#          "rank": ranks,
#          "year": year
#         })
print("=================")
print(frame)
print("=================")

print("=================group by teams =================")
group = frame.groupby("team")
print(group)
print(group.groups)
print("=================")


print("=================group by teams and rank =================")
group = frame.groupby(["team","rank"])
print(group)
print(group.groups)
print("=================")

print()
print("==========iterate in group==========")
group = frame.groupby("team")

for teamname,grp in group:
    print(teamname)
print("=============get a group==============")
print(group.get_group("Chennai Super Kings"))
print("==================")
