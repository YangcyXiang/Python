import random


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

for i in range(100):
    img_in0 = random.randint(0, 99)
    img_in1 = random.randint(0, 99)
    img_in2 = random.randint(0, 99)
    img_in3 = random.randint(0, 99)
    img_in4 = random.randint(0, 99)
    img_in5 = random.randint(0, 99)
    img_in6 = random.randint(0, 99)
    img_in7 = random.randint(0, 99)
    img_in8 = random.randint(0, 99)
    img_list = [img_in0, img_in1, img_in2, img_in3, img_in4, img_in5, img_in6, img_in7, img_in8]
    median = dfprt_median(img_in0, img_in1, img_in2, img_in3, img_in4, img_in5, img_in6, img_in7, img_in8)
    img_list.sort()
    if median != img_list[4]:
        print("ERROR!")
