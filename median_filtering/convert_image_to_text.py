import cv2
import numpy as np

noise_file_name = r"sim/python/data/timoxi_640x512_grayscale_noise.txt"
noise_coordinate_file_name = r"sim/python/data/timoxi_640x512_grayscale_noise_coordinate.txt"
bordered_file_name = r"sim/python/data/timoxi_642x514_grayscale_bordered.txt"
bordered_coordinate_file_name = r"sim/python/data/timoxi_642x514_grayscale_bordered_coordinate.txt"

# output_file_name = r"D:\Coding\vivado\median_filtering\sim\timoxi_642x514_grayscale_noise_bordered.txt"
file_noise = open(noise_file_name, "w")
file_noise_coordinate = open(noise_coordinate_file_name, "w")
file_bordered = open(bordered_file_name, "w")
file_bordered_coordinate = open(bordered_coordinate_file_name, "w")

# read raw image
img = cv2.imread("sim/python/data/timoxi_640x512.jpg", cv2.IMREAD_GRAYSCALE) # change to grayscale
rows, cols = img.shape
cv2.imshow("raw", img)

# add salt and pepper noise
probability = 0.01
img_noise=img
img_noise_coordinate = np.zeros(shape=(rows, cols), dtype=np.uint8)
for row in range(rows):
    for col in range(cols):
        # if np.random.random() > 0.95:
        if np.random.random() > 1 - probability:
            if img_noise[row, col] > 128:
                img_noise[row, col] = 0
            else:
                img_noise[row, col] = 255
            img_noise_coordinate[row, col] = 255
cv2.imshow("salt and pepper noise: (" + str(probability) + "/1)", img_noise)
cv2.imshow("salt and pepper noise coordinate", img_noise_coordinate)
noise_flatten = img_noise.flatten()
noise_coordinate_flatten = img_noise_coordinate.flatten()

# # add stripe noise
# for i in range(cols):
#     if np.random.random() > 0.99:
#         img_noise[:, i] = 255
# cv2.imshow("stripe noise: (" + str(probability) + "/1)", img_noise)


# add black bordered
kernel_size = 3     # 3 for 3x3 window
img_bordered = np.zeros(shape=(rows+int((kernel_size-1)), cols+int((kernel_size-1))), dtype=np.uint8)
img_bordered_coordinate = np.zeros(shape=(rows+int((kernel_size-1)), cols+int((kernel_size-1))), dtype=np.uint8)
for row in range(rows):
    for col in range(cols):
        img_bordered[row+int((kernel_size-1)/2)][col+int((kernel_size-1)/2)] = img_noise[row][col]
        img_bordered_coordinate[row+int((kernel_size-1)/2)][col+int((kernel_size-1)/2)] = img_noise_coordinate[row][col]
cv2.imshow("bordered", img_bordered)
cv2.imshow("bordered coordinate", img_bordered_coordinate)
bordered_flatten = img_bordered.flatten()
bordered_coordinate_flatten = img_bordered_coordinate.flatten()

# output 640x512 noised image to hex text 
for i in range(noise_flatten.size):
    file_noise.write(hex(noise_flatten[i])[2:]+"\n")
    file_noise_coordinate.write(hex(noise_coordinate_flatten[i])[2:]+"\n")
file_noise.close()
file_noise_coordinate.close()

# output  642x514 bordered noised image to hex text 
for i in range(bordered_flatten.size):
    file_bordered.write(hex(bordered_flatten[i])[2:]+"\n")
    file_bordered_coordinate.write(hex(bordered_coordinate_flatten[i])[2:]+"\n")
file_bordered.close()
file_bordered_coordinate.close()

# wait to show image
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("sim/python/data/timoxi_640x512_grayscale_noise_" + str(probability) + ".jpg", img_noise)
cv2.imwrite("sim/python/data/timoxi_640x512_grayscale_noise_coordinate.jpg", img_noise_coordinate)
cv2.imwrite("sim/python/data/timoxi_642x514_grayscale_bordered.jpg", img_bordered)
cv2.imwrite("sim/python/data/timoxi_642x514_grayscale_bordered_coordinate.jpg", img_bordered_coordinate)
