import re
file_input = open(r"D:/Archive/Project/20230626_SAR_ADC/gen_sch_xy.il", "r")
# file_output = open(r"./output.txt", "w")
file_output = open(r"D:/Archive/Project/20230626_SAR_ADC/output.txt", "w")
pattern_wire_name = re.compile(r".*schCreateWireLabel.*strcat\(\"(?P<label_name>.*)\"\).*")

wire_label_list = []

line_number = 0
while True:
    line = file_input.readline()
    line_number += 1
    if line == '':
        break
    re_result = pattern_wire_name.search(line)
    if re_result is None:
        continue
    else:
        wire_label_list.append((line_number, re_result.group('label_name')))

for item in wire_label_list:
    file_output.write('line_number ' + str(item[0]) + ': ' + item[1] + '\n')
