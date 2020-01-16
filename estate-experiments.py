
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tree.base import DecisionTree
from metrics import *
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

np.random.seed(42)

# Read real-estate data set
# ...
# 
data = pd.read_excel("https://archive.ics.uci.edu/ml/machine-learning-databases/00477/Real%20estate%20valuation%20data%20set.xlsx")
#Seperating target and features
data_target = data.iloc[:, -1]
data.drop(data.columns[[0, -1]], axis = 1, inplace = True)
#Training, test features and targets 
train_features, test_features = np.split(data, [int(0.7 * len(data))])
train_target, test_target = np.split(data_target, [int(0.7 * len(data))])
#Implementing decision tree on 70, 30 data
MyTree = DecisionTree("information_gain", 3)
fit = MyTree.fit(train_features, train_target)
y_hat = MyTree.predict(test_features)
f = open("1.md", "a")
f.write("Predicted values by my algorithm:\n")
f.write(str(np.array(y_hat)) + "\n")
f.write("RMSE : " + str(rmse(y_hat, test_target)) + "\n")    
f.write("MAE : " + str(mae(y_hat, test_target)) + "\n")
# Using scikit-learn
f.write("Using Scikit-learn:\n")
# Train and Test
X, Y = data, data_target  
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.3, random_state = 100) 

# Decision tree with entropy 
regressor = DecisionTreeRegressor(max_depth = 3, min_samples_leaf = 1) 
# Performing training 
regressor.fit(X_train, y_train) 

# Predictions
y_pred = regressor.predict(X_test) 
f.write("Predicted values:\n") 
f.write(str(y_pred) + "\n") 

# RMSE and MAE
f.write("RMSE : " + str(rmse(y_test, pd.Series(y_pred))) + "\n")    
f.write("MAE : "+ str(mae(y_test, pd.Series(y_pred))) + "\n")
f.close()
