import pandas as pd
import numpy as np

data = np.random.rand(5,4)
# print(data)

frame = pd.DataFrame(data, columns=["col1","col2","col3","col4"])
print(frame)
print("=======")
print(frame["col1"])
print("=======")

for key,value in frame.iteritems():
    print(key)
    print("=======")
    print(value)
    print("=======")
    print(type(value))
    print("=======")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

for row in frame.itertuples():
    print(row)
    print("=======")
    
