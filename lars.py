# -*- coding: utf-8 -*-
"""LARS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/195c4a-oXoeswgt0Yc9ynXcfIHDR4QeJI
"""



"""What is Least Angle Regression?

It is a model selection algorithm in the context of linear regression.
The two main advantages of LARS (Least Angle RegreSsion):
  1. avoid overfitting
  2. increase interpretability
  3. computational efficiency.

We start first by generating data
"""

import os
import numpy as np



import pandas as pd
import numpy as np
def generate_random_points(n, p):
  """
  use hardware entropy to generate random points n points in p-dimensional 
  Euclidean space form 
  """
  x = np.frombuffer(os.urandom(4*n*p), dtype = np.uint32)
  x = x.reshape(n,p)
  x = [row.tolist() for row in x]
  return x

y = generate_random_points(n=100,p=10)
x = generate_random_points(n=100,p=10)

#supress scikit future warnings
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

from numpy import mean, std
from sklearn.preprocessing import StandardScaler, scale
scaler = StandardScaler()
scaler.fit(x)
x_transformed = scaler.transform(x)
x_scaled = scale(x)
y_scaled = scale(y)
# print(x_scaled)
# print(x_transformed)
#print(mean(x))
#print(mean(x_scaled))
#print(mean(x_transformed))
#print(std(x))
#print(std(x_scaled))
#print(std(x_transformed))

#print(mean(x_scaled))
#print(std(x_scaled))





from sklearn.linear_model import Lars
from sklearn.model_selection import train_test_split
lars = Lars(fit_intercept=False, normalize=False, n_nonzero_coefs=100,verbose=True)
x_train, x_test, y_train, y_test = train_test_split(x_scaled,y_scaled,test_size=0.2, random_state=42)
lars.fit(x_train,y_train)

#print(x_test[0])
lars.predict(x_test)[0]

lars.score(x_test, y_test)

lars.get_params()

beta = generate_random_points(n=10, p=10)
scaler.fit(beta)
scaler.fit_transform(beta)
beta = scaler.fit_transform(beta)
epsilons = generate_random_points(n=100,p=10)
#print(epsilons)

y = [[] for _ in range(10)]
for k in range(10):
  y[k]=np.matmul(beta, np.asarray(x[k]))+epsilons[k]

x_scaled = scale(x)
y_scaled = scale(x)
epsilons = scale(epsilons)

lars = Lars(fit_intercept=False, normalize=False, n_nonzero_coefs=100,verbose=True)
x_train, x_test, y_train, y_test = train_test_split(x_scaled,y_scaled,test_size=0.2, random_state=42)
lars.fit(x_train,y_train)

#print(x_test[0])
lars.predict(x_test)[0]

lars.score(x_test, y_test)



