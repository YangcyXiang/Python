# from https://blog.csdn.net/qinghuaci666/article/details/81737624
# -*- coding:utf-8 -*-
import cv2
import numpy as np
from collections import deque


def dfprt_median(pixe_list):
    group1 = pixe_list[0:3]
    group2 = pixe_list[3:6]
    group3 = pixe_list[6:9]
    group1.sort()
    group2.sort()
    group3.sort()

    col1 = [group1[0], group2[0], group3[0]]  # max
    col2 = [group1[1], group2[1], group3[1]]  # mid
    col3 = [group1[2], group2[2], group3[2]]  # min
    col1.sort()
    col2.sort()
    col3.sort()
    #              min_max, mid_mid, max_min
    median_list = [col1[2], col2[1], col3[0]]
    median_list.sort()
    return median_list[1]


def median_filtering(image, kernel_size):
    file_output = open(r"timoxi_640x512_grayscale_python_output-threshold.txt", 'w')
    # threshold = int('0000_0011_1111', 2)
    threshold = np.uint16(31)
    image_rows, image_cols = image.shape
    image_result = np.zeros(shape=(image_rows, image_cols), dtype=np.uint8)
    bordered = np.zeros(shape=(image_rows + (kernel_size - 1), image_cols + (kernel_size - 1)), dtype=np.uint8)
    for row in range(image_rows):
        for col in range(image_cols):
            bordered[row + int((kernel_size - 1) / 2)][col + int((kernel_size - 1) / 2)] = image[row][col]
    # cv2.imshow("bordered", bordered)
    bordered_flatten = bordered.flatten()
    # mimic hardware memory
    fifo = deque(np.uint8(0) for i in range((kernel_size - 1) * (image_cols + (kernel_size - 1))))
    pointer = (kernel_size - 1) * (image_cols + (kernel_size - 1)) - 1
    for i in range(pointer + 1):
        fifo[i] = bordered_flatten[i]
    for row in range(image_rows):  # 512
        # repeat (kernel_size-1) times
        for i in range((kernel_size - 1)):
            pointer += 1
            fifo.append(bordered_flatten[pointer])
        for col in range(image_cols):  # 640
            # if pointer >= (image_rows+2)*(image_cols+2):
            #     break
            pointer += 1
            fifo.append(bordered_flatten[pointer])
            # image_result[row][col] = dfptr_median(fifo[0], fifo[1], fifo[2], fifo[image_cols+2], fifo[image_cols+2+1], fifo[image_cols+2+2], fifo[2*(image_cols+2)], fifo[2*(image_cols+2)+1], fifo[2*(image_cols+2)+2])
            current_list = [fifo[0], fifo[1], fifo[2], fifo[image_cols + 2], fifo[image_cols + 2 + 1], fifo[image_cols + 2 + 2], fifo[2 * (image_cols + 2)], fifo[2 * (image_cols + 2) + 1], fifo[2 * (image_cols + 2) + 2]]
            median_filtering_pixel = dfprt_median(current_list)
            # border_list = [fifo[0], fifo[1], fifo[2], fifo[image_cols + 2], fifo[image_cols + 2 + 2], fifo[2 * (image_cols + 2)], fifo[2 * (image_cols + 2) + 1], fifo[2 * (image_cols + 2) + 2]]
            # average = sum(border_list) / len(border_list)
            # variance = sum(list(map(lambda m : (m-average)**2, border_list))) / (len(border_list)-1)
            # if ( abs(fifo[image_cols+2+1]-average) > 0.5*average ) or ( (fifo[image_cols+2+1]-average)**2 > 9*variance ):   # blind pixel
            #     image_result[row, col] = median_filtering_pixel   # filtering
            #     file_output.write("{row:>6d}, {col:>6d}, {is_blind:>10d}\n".format(row=row, col=col, is_blind=11111111))
            # else:
            #     image_result[row, col] = fifo[image_cols + 2 + 1]   # raw pixel
            #     file_output.write("{row:>6d}, {col:>6d}, {is_blind:>10d}\n".format(row=row, col=col, is_blind=0))

            significance0 = abs(np.int16(fifo[image_cols + 2 + 1]) - fifo[0]) > threshold
            significance1 = abs(np.int16(fifo[image_cols + 2 + 1]) - fifo[1]) > threshold
            significance2 = abs(np.int16(fifo[image_cols + 2 + 1]) - fifo[2]) > threshold
            significance3 = abs(np.int16(fifo[image_cols + 2 + 1]) - fifo[image_cols + 2]) > threshold
            significance5 = abs(np.int16(fifo[image_cols + 2 + 1]) - fifo[image_cols + 2 + 2]) > threshold
            significance6 = abs(np.int16(fifo[image_cols + 2 + 1]) - fifo[2 * (image_cols + 2)]) > threshold
            significance7 = abs(np.int16(fifo[image_cols + 2 + 1]) - fifo[2 * (image_cols + 2) + 1]) > threshold
            significance8 = abs(np.int16(fifo[image_cols + 2 + 1]) - fifo[2 * (image_cols + 2) + 2]) > threshold
            counter = 0
            if significance0:
                counter += 1
            if significance1:
                counter += 1
            if significance2:
                counter += 1
            if significance3:
                counter += 1
            if significance5:
                counter += 1
            if significance6:
                counter += 1
            if significance7:
                counter += 1
            if significance8:
                counter += 1
            if counter > 3:   # blind pixel
                image_result[row, col] = median_filtering_pixel   # filtering
                file_output.write("{row:>6d}, {col:>6d}, {is_blind:>10d}\n".format(row=row, col=col, is_blind=11111111))
            else:
                image_result[row, col] = fifo[image_cols + 2 + 1]   # raw pixel
                file_output.write("{row:>6d}, {col:>6d}, {is_blind:>10d}\n".format(row=row, col=col, is_blind=0))

            fifo.popleft()
        # repeat (kernel_size-1) times
        for i in range((kernel_size - 1)):
            fifo.popleft()

    file_output.close()
    return image_result


# read image
# img = cv2.imread("data/timoxi_640x512.jpg", cv2.IMREAD_UNCHANGED)
# img = cv2.imread("data/timoxi_640x512_grayscale_noise.jpg", cv2.IMREAD_GRAYSCALE)  # change to grayscale
# img = cv2.imread("data/timoxi_640x512_grayscale_noise.jpg", cv2.IMREAD_UNCHANGED)  # change to grayscale
img = cv2.imread("data/timoxi_640x512_grayscale_noise_0.01.jpg", cv2.IMREAD_UNCHANGED)  # change to grayscale
cv2.imshow("src", img)

# # add salt and pepper noise
# probability = 0.1
# img_noise=img
# img_noise_coordinate = np.zeros(shape=(rows, cols), dtype=np.uint8)
# for row in range(rows):
#     for col in range(cols):
#         # if np.random.random() > 0.95:
#         if np.random.random() > 1 - probability:
#             img_noise[row, col] = 255
#             img_noise_coordinate[row, col] = 255
# cv2.imshow("salt and pepper noise: (" + str(probability) + "/1)", img_noise)
# cv2.imshow("salt and pepper noise coordinate", img_noise_coordinate)
# noise_flatten = img_noise.flatten()
# noise_coordinate_flatten = img_noise_coordinate.flatten()

# # add stripe noise
# for i in range(cols):
#     if np.random.random() > 0.99:
#         img_noise[:, i] = 255
# cv2.imshow("stripe noise: (" + str(probability) + "/1)", img_noise)

# median filtering, kernel size can be changed
# result_3x3 = cv2.medianBlur(img, 3)
# result_5x5 = cv2.medianBlur(img, 5)
# result_9x9 = cv2.medianBlur(img, 9)
img_filtered = median_filtering(img, 3)

# cv2.imshow("median filtering 3x3", result_3x3)
# cv2.imshow("median filtering 5x5", result_5x5)
# cv2.imshow("median filtering 9x9", result_9x9)
cv2.imshow("windowing filtered", img_filtered)

# wait to show
cv2.waitKey(0)
cv2.destroyAllWindows()

# save noised image
# cv2.imwrite("timoxi_640x512_grayscale_noise.jpg", img_noise)
# cv2.imwrite("timoxi_640x512_grayscale_filtering_3x3.jpg", result_3x3)
# cv2.imwrite("timoxi_640x512_grayscale_filtering_5x5.jpg", result_5x5)
# cv2.imwrite("timoxi_640x512_grayscale_filtering_9x9.jpg", result_9x9)
# cv2.imwrite("data/timoxi_320x256_grayscale_noise.jpg", img_noise)
# cv2.imwrite("data/timoxi_320x256_grayscale_filtering.jpg", result)
cv2.imwrite("timoxi_640x512_grayscale_windowing_filter-threshold.jpg", img_filtered)
