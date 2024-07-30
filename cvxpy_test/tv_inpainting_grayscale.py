# from https://www.cvxpy.org/examples/applications/tv_inpainting.html
#####################################################################################
# 1. load the original image and the corrupted image and construct the Known matrix #
#####################################################################################
import matplotlib.pyplot as plt
import numpy as np
# Load the images.
u_orig = plt.imread("data/loki512.png")
u_corr = plt.imread("data/loki512_corrupted.png")
rows, cols = u_orig.shape

# known is 1 if the pixel is known,
# 0 if the pixel was corrupted.
known = np.zeros((rows, cols))
for i in range(rows):
    for j in range(cols):
         if u_orig[i, j] == u_corr[i, j]:
            known[i, j] = 1

#%matplotlib inline
fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].imshow(u_orig, cmap='gray')
ax[0].set_title("Original Image")
ax[0].axis('off')
ax[1].imshow(u_corr, cmap='gray');
ax[1].set_title("Corrupted Image")
ax[1].axis('off');
plt.show()

####################################################################
# 2. Recover the original image using total variation in-painting. #
####################################################################
import cvxpy as cp


U = cp.Variable(shape=(rows, cols))
obj = cp.Minimize(cp.tv(U))
constraints = [cp.multiply(known, U) == cp.multiply(known, u_corr)]
prob = cp.Problem(obj, constraints)

# Use SCS to solve the problem.
prob.solve(verbose=True, solver=cp.SCS)
print("optimal objective value: {}".format(obj.value))

fig, ax = plt.subplots(1, 2, figsize=(10, 5))
# Display the in-painted image.
ax[0].imshow(U.value, cmap='gray');
ax[0].set_title("In-Painted Image")
ax[0].axis('off')

img_diff = 10*np.abs(u_orig - U.value)
ax[1].imshow(img_diff, cmap='gray');
ax[1].set_title("Difference Image")
ax[1].axis('off');
plt.show()
