import matplotlib.pyplot as plt
# Y = [10,2,300,210,50]
# plt.plot(Y)
# plt.show()


X = list(range(0,11))

#list comprehenses
Y1 = [n for n in X]
Y2 = [n*n for n in X]
Y3 = [n*n*n for n in X]
print(X)
print(Y1)
print(Y2)
print(Y3)

plt.plot(X,Y1, label="Y1")
plt.plot(X,Y2, label="Y2")
plt.plot(X,Y3, label="Y3")
#plt.show()

plt.legend()
plt.xlabel("x-axis")
plt.ylabel("y-label")

plt.title("polynomial graph")
plt.grid(True)
#plt.savefig("mygraph")

plt.show()
