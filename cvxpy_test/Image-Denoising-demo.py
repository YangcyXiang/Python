# changed from verilog https://github.com/livebinary/Image-Denoising
def sort2(input1, input2):
    sort2_list = [input1, input2]
    sort2_list.sort()
    return sort2_list


def sort4(input1, input2, input3, input4):
    sort4_list = [input1, input2, input3, input4]
    sort4_list.sort()
    return sort4_list


# def sort9
# [in1, in2, in3, in4, in5, in6, in7, in8, in9] = [9, 8, 7, 6, 5, 4, 3, 2, 1]
[in1, in2, in3, in4, in5, in6, in7, in8, in9] = [8, 3, 6, 4, 7, 5, 1, 9, 2]
print('in1', 'in2', 'in3', 'in4',  'in5',  'in6',  'in7',  'in8',  'in9', sep='   |   ')
print(in1, in2, in3, in4, in5, in6, in7, in8, in9, sep='         ')

# step1
# sort4 j1(in1,in2,in3,in4,in11,in22,in33,in44);
# sort4 hj(in5,in6,in7,in8,in88,in77,in66,in55);
[in11, in22, in33, in44] = sort4(in1, in2, in3, in4)
[in88, in77, in66, in55] = sort4(in5, in6, in7, in8)
print(in11, in22, in33, in44, in88, in77, in66, in55, in9, sep='         ')

# step2
# sorter_2 a1(in11,in55,m1,w1);
# sorter_2 af(in33,in77,m2,w2);
# sorter_2 a2(in22,in66,m3,w3);
# sorter_2 a3(in44,in88,m4,w4);
[m1, w1] = sort2(in11, in55)
[m2, w2] = sort2(in33, in77)
[m3, w3] = sort2(in22, in66)
[m4, w4] = sort2(in44, in88)
print(m1, m3, m2, m4, w4, w2, w3, w1, in9, sep='         ')

# # step3
# # sorter_2 a4(w1,w2,m5,w5);
# # sorter_2 ar(m1,m2,m6,w6);
# # sorter_2 a2f(w3,w4,m7,w7);
# # sorter_2 a3d(m3,m4,m8,w8);
# [m5, w5] = sort2(w1, w2)
# [m6, w6] = sort2(m1, m2)
# [m7, w7] = sort2(w3, w4)
# [m8, w8] = sort2(m3, m4)
# print(m6, m8, w6, w8, m7, m5, w7, w5, in9, sep='         ')
#
# # step4
# # sorter_2 a41(w5,w7,m9,w9);
# # sorter_2 ar1(m5,m7,m10,w10);
# # sorter_2 a2f1(w6,w8,m11,w11);
# # sorter_2 a3d1(m6,m8,m12,w12);
# [m9, w9] = sort2(w5, w7)
# [m10, w10] = sort2(m5, m7)
# [m11, w11] = sort2(w6, w8)
# [m12, w12] = sort2(m6, m8)
# print(m12, w12, m11, w11, m10, w10, m9, w9, in9, sep='         ')

[s1, s2, s3, s4] = sort4(m1, m3, m2, m4)
[s5, s6, s7, s8] = sort4(w4, w2, w3, w1)
print(s1, s2, s3, s4, s5, s6, s7, s8, in9, sep='         ')
