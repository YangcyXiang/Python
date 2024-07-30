# from https://www.cvxpy.org/examples/applications/tv_inpainting.html
####################################################################################################################################
# load the original image and construct the Known matrix by randomly selecting 30% of the pixels to keep and discarding the others #
####################################################################################################################################
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1)
# Load the images.
u_orig = plt.imread("data/loki512color.png")
rows, cols, colors = u_orig.shape

# known is 1 if the pixel is known,
# 0 if the pixel was corrupted.
# The known matrix is initialized randomly.
known = np.zeros((rows, cols, colors))
for i in range(rows):
    for j in range(cols):
        if np.random.random() > 0.7:
            for k in range(colors):
                known[i, j, k] = 1
u_corr = known * u_orig

# Display the images.
# %matplotlib inline
fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].imshow(u_orig, cmap='gray');
ax[0].set_title("Original Image")
ax[0].axis('off')
ax[1].imshow(u_corr)
ax[1].set_title("Corrupted Image")
ax[1].axis('off')
plt.show()


####################################################################
# 2. Recover the original image using total variation in-painting. #
####################################################################
import cvxpy as cp


variables = []
constraints = []
for i in range(colors):
    U = cp.Variable(shape=(rows, cols))
    variables.append(U)
    constraints.append(cp.multiply(known[:, :, i], U) == cp.multiply(known[:, :, i], u_corr[:, :, i]))

prob = cp.Problem(cp.Minimize(cp.tv(*variables)), constraints)
prob.solve(verbose=True, solver=cp.SCS)
print("optimal objective value: {}".format(prob.value))

####################################################################################################################
# display the in-painted image and the difference in RGB values at each pixel of the original and in-painted image #
####################################################################################################################
import matplotlib.pyplot as plt
import matplotlib.cm as cm
#%matplotlib inline

rec_arr = np.zeros((rows, cols, colors))
for i in range(colors):
    rec_arr[:, :, i] = variables[i].value
rec_arr = np.clip(rec_arr, 0, 1)

fig, ax = plt.subplots(1, 2,figsize=(10, 5))
ax[0].imshow(rec_arr)
ax[0].set_title("In-Painted Image")
ax[0].axis('off')

img_diff = np.clip(10 * np.abs(u_orig - rec_arr), 0, 1)
ax[1].imshow(img_diff)
ax[1].set_title("Difference Image")
ax[1].axis('off')
plt.show()
