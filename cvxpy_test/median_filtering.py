# from https://blog.csdn.net/qinghuaci666/article/details/81737624
# -*- coding:utf-8 -*-
import cv2
import numpy as np
from collections import deque


def dfprt_median(in1, in2, in3, in4, in5, in6, in7, in8, in9):
    group1 = [in1, in2, in3]
    group2 = [in4, in5, in6]
    group3 = [in7, in8, in9]
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


def median_filtering(image):
    image_rows, image_cols = image.shape
    image_result = np.zeros(shape=(image_rows, image_cols), dtype=np.uint8)
    mask = np.zeros(shape=(image_rows+2, image_cols+2), dtype=np.uint8)
    for row in range(image_rows):
        for col in range(image_cols):
            mask[row+1][col+1] = image[row][col]
    # cv2.imshow("mask", mask)
    mask_flatten = mask.flatten()
    # mimic hardware memory
    # fifo = deque(np.uint8(0) for i in range(2*(image_cols+2)+3))
    fifo = deque(np.uint8(0) for i in range(2*(image_cols+2)))
    pointer = 2*(image_cols+2) -1
    for i in range(pointer + 1):
        fifo[i] = mask_flatten[i]
    # fifo.popleft()
    # fifo.append(mask_flatten[pointer])
    # pointer += 1
    for row in range(image_rows):   # 512
        pointer += 1
        fifo.append(mask_flatten[pointer])
        pointer += 1
        fifo.append(mask_flatten[pointer])
        # fifo.popleft()
        # fifo.append(mask_flatten[pointer])
        # pointer += 1
        for col in range(image_cols):   # 640
            # if pointer >= (image_rows+2)*(image_cols+2):
            #     break
            pointer += 1
            fifo.append(mask_flatten[pointer])
            # image_result[row][col] = dfptr_median(fifo[0], fifo[1], fifo[2], fifo[image_cols+2], fifo[image_cols+2+1], fifo[image_cols+2+2], fifo[2*(image_cols+2)], fifo[2*(image_cols+2)+1], fifo[2*(image_cols+2)+2])
            temp = dfprt_median(fifo[0], fifo[1], fifo[2], fifo[image_cols + 2], fifo[image_cols + 2 + 1], fifo[image_cols + 2 + 2], fifo[2 * (image_cols + 2)], fifo[2 * (image_cols + 2) + 1], fifo[2 * (image_cols + 2) + 2])
            image_result[row, col] = temp
            fifo.popleft()
        fifo.popleft()
        fifo.popleft()

    return image_result

if __name__ == '__main__':
    # read image
    # img = cv2.imread("data/timoxi_640x512.jpg", cv2.IMREAD_UNCHANGED)

    # img = cv2.imread("data/timoxi_640x512.jpg", cv2.IMREAD_GRAYSCALE) # change to grayscale
    # img = cv2.imread("D:/Workspace/datasets/onedrive_omit/Set12/airplane256.png", cv2.IMREAD_GRAYSCALE) # change to gra
    # img = cv2.imread("D:/Workspace/datasets/onedrive_omit/Set12/barbara512.png", cv2.IMREAD_GRAYSCALE) # change to grayscale
    # img = cv2.imread("D:/Workspace/datasets/onedrive_omit/Set12/boat512.png", cv2.IMREAD_GRAYSCALE) # change to grayscale

    # img = cv2.imread("D:/Workspace/datasets/onedrive_omit/Set12/Cameraman256.png", cv2.IMREAD_GRAYSCALE) # change to grayscale
    # img = cv2.imread("D:/Workspace/datasets/onedrive_omit/Set12/couple512.png", cv2.IMREAD_GRAYSCALE) # change to grayscale
    # img = cv2.imread("D:/Workspace/datasets/onedrive_omit/Set12/fishstar256.png", cv2.IMREAD_GRAYSCALE) # change to grayscale
    # img = cv2.imread("D:/Workspace/datasets/onedrive_omit/Set12/house256.png", cv2.IMREAD_GRAYSCALE) # change to grayscale
    # img = cv2.imread("D:/Workspace/datasets/onedrive_omit/Set12/Lena512.png", cv2.IMREAD_GRAYSCALE) # change to grayscale
    # img = cv2.imread("D:/Workspace/datasets/onedrive_omit/Set12/man512.png", cv2.IMREAD_GRAYSCALE) # change to grayscale
    # img = cv2.imread("D:/Workspace/datasets/onedrive_omit/Set12/monarch256.png", cv2.IMREAD_GRAYSCALE) # change to grayscale
    # img = cv2.imread("D:/Workspace/datasets/onedrive_omit/Set12/parrot256.png", cv2.IMREAD_GRAYSCALE) # change to grayscale
    # img = cv2.imread("D:/Workspace/datasets/onedrive_omit/Set12/peppers256.png", cv2.IMREAD_GRAYSCALE) # change to grayscale
    img = cv2.imread("./data/loki256.png", cv2.IMREAD_GRAYSCALE) # change to grayscale
    #
    # yscale
    # img = cv2.imread("data/timoxi_320x256.jpg", cv2.IMREAD_GRAYSCALE) # change to grayscale
    img_noise=img

    cv2.imshow("src", img)

    # rows, cols, chn = img_noise.shape
    rows, cols = img_noise.shape


    # add noise
    for row in range(rows):
        for col in range(cols):
            if np.random.random() > 0.975:
                img_noise[row, col] = 255
            elif np.random.random() < 0.025:
                img_noise[row, col] = 0

    # for i in range(5000):
    #     x = np.random.randint(0, rows)
    #     y = np.random.randint(0, cols)
    #     # img_noise[x, y, :] = 255
    #     img_noise[x, y] = 255
    # for i in range(cols):
    #     if np.random.random() > 0.9:
    #         img_noise[:, i] = 255


    cv2.imshow("noise", img_noise)

    # median filtering, kernel size can be changed
    # result = cv2.medianBlur(img_noise, 3)
    result = median_filtering(img_noise)

    cv2.imshow("median filtering", result)

    # wait to show
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # save noised image

    # cv2.imwrite("data/timoxi_640x512_grayscale_noise.jpg", img_noise)
    # cv2.imwrite("data/timoxi_640x512_grayscale_filtering.jpg", result)

    # cv2.imwrite("data/timoxi_320x256_grayscale_noise.jpg", img_noise)
    # cv2.imwrite("data/timoxi_320x256_grayscale_filtering.jpg", result)