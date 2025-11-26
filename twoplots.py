# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 08:14:43 2025

@author: lenovo
"""
import matplotlib.pyplot as plt
import numpy as np

# age and speed of 8 cars
x =np.array([5,7,8,7,2,17,9,6])
y =np.array([99,86,87,88,111,134,101,125])
colors=np.array(["red","orange","yellow","pink","purple","black","blue","gray"])
plt.scatter(x,y, c=colors)


# age and speed of 10 cars
x =np.array([5,7,8,7,2,17,9,6,3,9])
y =np.array([99,86,87,88,111,134,101,125,112,111])
colors =np.array(["hotpink","red","orange","yellow","blue","gray","black","pink","black","brown"])
plt.scatter(x,y, c=colors)
plt.show()
