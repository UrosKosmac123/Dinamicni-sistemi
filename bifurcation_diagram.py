import matplotlib.pyplot as plt
import math
import numpy as np

P=np.linspace(1,2,10000)
m=0.7
# Initialize your data containers identically
X = []
Y = []
# l is never used, I removed it.
for u in P:
    # Add one value to X instead of resetting it.
    X.append(u)
    # Start with a random value of m instead of remaining stuck
    # on a particular branch of the diagram
    m = np.random.random()
    for n in range(1001):
      m=u*math.cos(m)
    # The break is harmful here as it prevents completion of
    # the loop and collection of data in Y 
    for l in range(1051):
      m= u*math.cos(m)
    # Collection of data in Y must be done once per value of u
    Y.append(m)
# Remove the line between successive data points, this renders
# the plot illegible. Use a small marker instead.
plt.plot(X, Y, ls='', marker=',')
plt.show()