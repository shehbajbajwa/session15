import os
"""
print(os.getcwd())
print(os.name)
#print(os.uname())
print(os.getlogin())
print(os.getppid())

pathToDir = "/Users/Shehbaj Bajwa/Downloads"
pathToFile = "/Users/Shehbaj Bajwa/Downloads/14 Trg.docx"
print("Is Downloads available:", os.path.exists(pathToDir))
print("Is 14 Trg.docx available:", os.path.exists(pathToFile))

#path = "/Users/Shehbaj bajwa/Downloads/MyPythonPrograms"
#os.mkdir(path)

"""
#print(os.getcwd())
#os.chdir("/Users/ishantkumar/Downloads/MyPythonPrograms")
#print(os.getcwd())
"""

# os.rmdir("/Users/Shehbaj Bajwa/Downloads/MyPythonPrograms")
# print(">> Directory Removed")

files = os.walk("/Users/Shehbaj Bajwa/Downloads")
print("files:",files)

allFiles = list(files)
for file in allFiles:
    print(file)
    """

# Assignment
# Ask path of a folder from user as input
# Tell him how many number of audio files, video files and documents exists
# Explore : To find all those files which were created long ago and are not in use :)

print("WELCOME USER TO THE DATA TELLER CODE")
print("please enter the following to check the details")
a = input("enter pathToDir: ")
#pathToDir = "/Users/Shehbaj Bajwa/Downloads"
b = input("enter pathToFile: ")
#pathToFile = "/Users/Shehbaj Bajwa/Downloads/songs"

songs = os.walk("b")
print("songs:",songs)

allFiles = list(songs)
for song in allFiles:
    print(songs)

songs = "file"

print("True/False?", songs.endswith(".mp3"))