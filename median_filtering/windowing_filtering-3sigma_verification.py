import re
import os

print(os.getcwd())
python_output_pattern = re.compile("(\s)*(?P<row>\d+), (\s)*(?P<col>\d+), (\s)*(?P<is_blind>\d+)")
coordinate_pattern = re.compile("(?P<is_blind>\S+)")
# line = "ff"
# re_result = coordinate_pattern.search(line)
# print(re_result)
input_file_name = r"timoxi_640x512_grayscale_python_output-3sigma.txt"
golden_file_name = r"data/timoxi_640x512_grayscale_noise_coordinate.txt"

file_input = open(input_file_name, "r")
file_golden = open(golden_file_name, 'r')


count_over_processing = 0
while True:
    input_line = file_input.readline()
    golden_line = file_golden.readline()
    if input_line is None or golden_line is None:
        break
    elif input_line == '' or golden_line == '':
        break

    python_result = python_output_pattern.search(input_line)
    golden_result = coordinate_pattern.search(golden_line)
    if python_result is None or golden_result is None:
        continue
    else:
        if golden_result.group('is_blind') == 'ff':     # blind pixel
            if python_result.group('is_blind') == '0':  # omit blind pixel
                # (419, 412), checked
                print("{row:>6}, {col:>6}, {is_blind:>10}\n".format(row=python_result.group('row'), col=python_result.group('col'), is_blind=python_result.group('is_blind')))
        else:   # raw pixel
            if python_result.group('is_blind') == '11111111':  # over processing pixel
                count_over_processing += 1
                # print("{row:>6}, {col:>6}, {is_blind:>10}\n".format(row=python_result.group('row'), col=python_result.group('col'), is_blind=python_result.group('is_blind')))
print("over processing rate = {rate:>6.6f}".format(rate=count_over_processing/640/512))
file_input.close()
file_golden.close()
print("SUCCESS!")