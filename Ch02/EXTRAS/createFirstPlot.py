'''
Created on Oct 27, 2010

@author: Peter
'''
from numpy import *
import kNN
import matplotlib
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(9, 6))
ax = fig.add_subplot(111)
datingDataMat,datingLabels = kNN.file2matrix('../datingTestSet2.txt')
#ax.scatter(datingDataMat[:,1], datingDataMat[:,2])
ax.scatter(datingDataMat[:,1], datingDataMat[:,2], 15.0*array(datingLabels), 15.0*array(datingLabels))
ax.axis([-2,25,-0.2,2.0])
plt.xlabel('Percentage of Time Spent Playing Video Games')
plt.ylabel('Liters of Ice Cream Consumed Per Week')
plt.show()

fig = plt.figure(figsize=(9, 6))
ax = fig.add_subplot(111)
datingDataMat,datingLabels = kNN.file2matrix('../datingTestSet2.txt')
#ax.scatter(datingDataMat[:,1], datingDataMat[:,2])
ax.scatter(datingDataMat[:,0], datingDataMat[:,1], 15.0*array(datingLabels), 15.0*array(datingLabels))
ax.axis([-20000,100000,-5,25])
plt.xlabel('Percentage of Distance of flight')
plt.ylabel('Percentage of Time Spent Playing Video Games')
plt.show()
