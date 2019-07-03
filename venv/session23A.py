import threading
class printer:
    def printDocu(self,docName,times):
        for i in range(1,times+1):
            print(">>printing{} copy#{}".format(docName,i))

class desktop:
    def __init__(self,printr):
        self.printr=printr
    def run(self):
        printr.printDocu("learningpython.pdf",10)
printr = printer()
# pref = printer()
printr.printDocu("learningpython.pdf",10)