import requests
import threading
#child thread
class fetchNewsTask(threading.Thread):
    #what child thead should do will be written in the run function
    def run(self):
        url1 = "https://newsapi.org/v2/everything?q=bitcoin&from=2019-06-03&sortBy=publishedAt&apiKey=fad0d097a5d74809b2f0f4df0dbcf080"
        print("fetching data from url1")
        responce1 = requests.get(url1)
        print(responce1.text)

class fetchBookTask(threading.Thread):
    #what child thead should do will be written in the run function
    def run(self):
        url2 = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=fad0d097a5d74809b2f0f4df0dbcf080"
        print("fetching data from url2")
        responce1 = requests.get(url2)
        print(responce1.text)

print("======app started ======")
newsTask = fetchNewsTask()
bookTask = fetchBookTask()

newsTask.start()
bookTask.start()



# print("fetching data from url1")
# responce1 = requests.get(url1)
# print(responce1.text)
# print("fetching data from url2")
# responce2 = requests.get(url2)
# print(responce2.text)
for i in range(1,11):
    print(">>>>>>:",i)
print(">>>>>> app finished >>>>>>")