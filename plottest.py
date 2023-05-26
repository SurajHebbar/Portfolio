from mpl_toolkits import mplot3d

#matplotlib inline

import matplotlib.pyplot as plt

import math
import csv

import numpy as np
import argparse
import time







FN = 'R' + '.csv'
with open(FN, 'r') as f:
    RGB = np.array(list(csv.reader(f, delimiter=",")))
    print(FN)
print(RGB.shape)
RGB = RGB.astype(float)
Frame_Count = RGB.shape[0]










plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


x = np.linspace(-1, 1, 1200)
y =np.linspace(-1,1,1200)
z = np.linspace(-1,1,1200)

R = RGB[:,0]
G = RGB[:,1]
B = RGB[:,2]
# c = 2*G - 1.18*B - R
c = R + B

# ST1 = wdc*(G - R)  + 1*(G - B) - (R  + B)
# ST2 = (R + B)



img = ax.scatter( x, y, z, c=c, cmap='YlGnBu', alpha=1)
# img1 = ax.scatter(x, y, z, c=c, cmap='YlOrRd', alpha=1)

ax.set_xlim3d([-2, 2])
ax.set_ylim3d([-2, 2])
ax.set_zlim3d([-2, 2])
ax.set_xlabel('R_F')
ax.set_ylabel('B_F')
ax.set_zlabel('G_F')
ax.view_init(190, 220)
fig.colorbar(img)
# fig.colorbar(img1)
plt.show()

# plt.rcParams["figure.figsize"] = [7.00, 3.50]
# plt.rcParams["figure.autolayout"] = True
# fig = plt.figure()

# ax = fig.add_subplot(111, projection='3d')
# x = RGB[100:500,0]
# y = RGB[100:500,1]
# z = RGB[100:500,2]
# c = -x - 1.18*z + 2*y
# d = x + y
# img = ax.scatter(x, z, z, c, cmap='YlOrRd', alpha=1)
# #img = ax.scatter(x, y, z, c=c, cmap='YlOrRd', alpha=1)
# ax.set_xlabel('R_F')
# ax.set_ylabel('B_F')
# ax.set_zlabel('G_F')
# ax.view_init(190, 220)
# fig.colorbar(img)
# plt.show()
