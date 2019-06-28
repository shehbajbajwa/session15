#create a chess board of 8*8 with 1s and os in pycharm

import numpy as np
x = np.ones((3,3))
print("Checkerboard pattern:")
x = np.zeros((8,8),dtype=int)
x[1::2,::2] = 1
x[::2,1::2] = 1
print(x)

#ask user to place 4 queens on chessboard
# y = int(input("enter the position of queen: "))
# y[]
for i in range(0, 4):
    i += 1
    queenposition = input("where to place 1st queen:")
    i = int(queenposition[0])
    j = int(queenposition[2])
    x[i][j] = 9
    print(x)
#3
queenposition = input("where to place 2nd queen:")
i = int(queenposition[0])
j = int(queenposition[2])
for x in range(0,8):
    if(x[i][j] or x[j][i]==9):
        print(x)



#3. validate


