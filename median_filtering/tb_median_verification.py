import re
import operator 
import os
print(os.getcwd())
# re_pattern = re.compile("in\[0\]=(\s)*(?P<in0>\d+), in\[1\]=(\s)*(?P<in1>\d+), in\[2\]=(\s)*(?P<in2>\d+), in\[3\]=(\s)*(?P<in3>\d+), in\[4\]=(\s)*(?P<in4>\d+), in\[5\]=(\s)*(?P<in5>\d+), in\[6\]=(\s)*(?P<in6>\d+), in\[7\]=(\s)*(?P<in7>\d+), in\[8\]=(\s)*(?P<in8>\d+), out\[0\]=(\s)*(?P<out0>\d+), out\[1\]=(\s)*(?P<out1>\d+), out\[2\]=(\s)*(?P<out2>\d+), out\[3\]=(\s)*(?P<out3>\d+), out\[4\]=(\s)*(?P<out4>\d+), out\[5\]=(\s)*(?P<out5>\d+), out\[6\]=(\s)*(?P<out6>\d+), out\[7\]=(\s)*(?P<out7>\d+), out\[8\]=(\s)*(?P<out8>\d+)")
# line = "in[0]=  45, in[1]=3915, in[2]= 194, in[3]=1566, in[4]=1293, in[5]=3564, in[6]=3352, in[7]=3025, in[8]=3206, out[0]=3915, out[1]=3564, out[2]=3352, out[3]=3206, out[4]=3025, out[5]=1566, out[6]=1293, out[7]= 194, out[8]=  45 "
re_pattern = re.compile("in\[0\]=(\s)*(?P<in0>\d+), in\[1\]=(\s)*(?P<in1>\d+), in\[2\]=(\s)*(?P<in2>\d+), in\[3\]=(\s)*(?P<in3>\d+), in\[4\]=(\s)*(?P<in4>\d+), in\[5\]=(\s)*(?P<in5>\d+), in\[6\]=(\s)*(?P<in6>\d+), in\[7\]=(\s)*(?P<in7>\d+), in\[8\]=(\s)*(?P<in8>\d+), med=(\s)*(?P<med>\d+)")
# line = "in[0]=2168, in[1]=2395, in[2]=2889, in[3]=3647, in[4]=3882, in[5]= 856, in[6]=2182, in[7]=3214, in[8]= 668, med=2395"
# re_result = re_pattern.search(line)
# print(re_result)
input_file_name = r"sim/tb_median_output.txt"
file_input = open(input_file_name, "r")

count = 0
while True:
    count += 1
    line = file_input.readline()
    if line is None:
        break
    elif line == '':
        break
    
    re_result = re_pattern.search(line)
    if re_result is None:
        continue
    else:
        in0 = int(re_result.group('in0'))
        in1 = int(re_result.group('in1'))
        in2 = int(re_result.group('in2'))
        in3 = int(re_result.group('in3'))
        in4 = int(re_result.group('in4'))
        in5 = int(re_result.group('in5'))
        in6 = int(re_result.group('in6'))
        in7 = int(re_result.group('in7'))
        in8 = int(re_result.group('in8'))
        # out0 = int(re_result.group('out0')) # max
        # out1 = int(re_result.group('out1'))
        # out2 = int(re_result.group('out2'))
        # out3 = int(re_result.group('out3'))
        # out4 = int(re_result.group('out4'))
        # out5 = int(re_result.group('out5'))
        # out6 = int(re_result.group('out6'))
        # out7 = int(re_result.group('out7'))
        # out8 = int(re_result.group('out8')) # min
        med = int(re_result.group('med'))
        input_list = [in0, in1, in2, in3, in4, in5, in6, in7, in8]
        # output_list = [out0, out1, out2, out3, out4, out5, out6, out7, out8]
        input_list.sort(reverse=True)
        # golden_list = input_list
        # if operator.eq(output_list, golden_list) is False:
        #     print("ERROR!")
        golden_median = input_list[4]
        if golden_median != med :
            print("ERROR!")
        else : 
            print(count)
print("SUCCESS!")