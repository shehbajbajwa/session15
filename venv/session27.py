from sklearn.datasets import load_iris
from sklearn import tree
irisData = load_iris()
print("====>>>>>>>>>>===IRIS DATASET==>>>>>>>>>>>>>>==")
print(irisData)
print(type(irisData))
print()

#array of features
print(irisData.data)
print()

#array of targets
print(irisData.target)
print()

#array of target names
print(irisData.target_names)
print()

#2 lets create model
model = tree.DecisionTreeClassifier()

#3 train the model \ supervised learning
model.fit(irisData.data,irisData.target)

#4 lets test our model
inputdata = [5.5,2.6,4.4,1.2] #-> veriscular type of iris flower

predictedClass = model.predict([inputdata])
print()
#print(">> predicted flower type is :",predictedClass)
#print(">> predicted flower type is :",predictedClass[0])
print(">> predicted flower type is :",irisData.target_names[predictedClass[0]])


# export our data as graph visual
import graphviz
data = tree.export_graphviz(model,out_file=None)
graph = graphviz.Source(data)
graph.render("iris dataset tree")
graph.view()