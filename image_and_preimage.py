import matplotlib.pyplot as plt
import math
import numpy as np

s = 0.5
x=np.linspace(-s,s,10000)
y = x 

n = 3
a = 4
b = 1

H_x = x
H_y = y
Hinv_x = x
Hinv_y = y

for i in range(1, n+1):
    # Image of map H_(a,b) after n - iterations
    H_x = 1 - a*(H_x*H_x) + H_y
    H_y = b*H_y

    # Preimage of map H_(a, b) or image of H^(-1)_(a,b) after n - iterations
    Hinv_x = Hinv_y/b
    Hinv_y = Hinv_x - 1 + (a/(b*b))*(Hinv_y*Hinv_y)

#plt.figure()
plt.plot(H_x, H_y)

#plt.figure()
plt.plot(Hinv_x, Hinv_y)
plt.show()


def horseshoe_map(X, Y, stretch=2.0, compress=0.5):
    # Step 1: Stretch in x and compress in y
    X_new = stretch * X
    Y_new = compress * Y
    
    # Step 2: Fold: split domain into left/right and flip right side
    fold_mask = X_new > 0
    Y_new[fold_mask] = -Y_new[fold_mask]  # flip vertically
    X_new[fold_mask] = -X_new[fold_mask]  # flip horizontally

    # Step 3: Translate to bring folded part back into square (optional)
    X_new += 0.5  # recenter
    Y_new += 0.0  # no vertical shift here

    return X_new, Y_new

# N = 500
# x = np.linspace(-1, 1, N)
# y = np.linspace(-1, 1, N)
# X, Y = np.meshgrid(x, y)
# X = X.flatten()
# Y = Y.flatten()

# # Iterate the horseshoe map
# num_iters = 5
# for i in range(num_iters):
#     X, Y = horseshoe_map(X, Y)
#     plt.figure(figsize=(6, 6))
#     plt.scatter(X, Y, s=0.1, color='navy')
#     plt.title(f'Horseshoe Map - Iteration {i+1}')
#     plt.axis('equal')
#     plt.axis('off')
#     plt.show()
