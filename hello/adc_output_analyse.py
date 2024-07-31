import re
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':

    fid_analog_signal = open(r"./adc_output/analog_signal_sample-output.txt", "r")
    fid_digital_signal = open(r"./adc_output/digital_signal_sample-output.txt", "r")
    file_output = open(r"./output.txt", "w")
    # file_output = open(r"D:/Archive/Project/20230626_SAR_ADC/output.txt", "w")
    pattern_analog_signal = re.compile(r"(?P<sample_number>\d+),(\s)+(?P<vin1_plus>\d+(\.\d+)*),(\s)+(?P<vin1_minus>\d+(\.\d+)*)")
    pattern_digital_signal = re.compile(r"(?P<sample_number>\d+),(\s)+(?P<digital_code>\d+)(\s)+")

    data_list = []
    analog_input_list = []
    digital_code_list = []

    while True:
        line_analog = fid_analog_signal.readline()
        line_digital = fid_digital_signal.readline()
        if line_analog == '' or line_digital == '' :
            break
        re_analog_result = pattern_analog_signal.search(line_analog)
        re_digital_result = pattern_digital_signal.search(line_digital)
        if re_analog_result is None or re_digital_result is None:
            continue
        else:
            if re_analog_result.group('sample_number') != re_digital_result.group('sample_number') :
                print("ERROR! analog number = {analog_number}, digital number = {digital_number}".format(analog_number=re_analog_result.group('sample_number'), digital_number=re_digital_result.group('sample_number')))
                break
            data_list.append((re_analog_result.group('sample_number'), re_analog_result.group('vin1_plus'), re_analog_result.group('vin1_minus'), re_digital_result.group('digital_code')))
            analog_input_list.append(float(re_analog_result.group('vin1_plus')) - float(re_analog_result.group('vin1_minus')))
            digital_code_list.append(re_digital_result.group('digital_code'))
    fid_analog_signal.close()
    fid_digital_signal.close()


    file_output.write("sample_number, vin1_plus, vin1_minus, digital_code, digital_code(radix 10)\n")
    for item in data_list:
        # file_output.write("{sample_number}, {vin1_plus}, {vin1_minus}, {digital_code}\n".format(sample_number=item[0], vin1_plus=item[1], vin1_minus=item[2], digital_code=item[3]))
        # file_output.write("{sample_number}, {analog_input:.6f}, {digital_code}, {digital_number_radix10}\n".format(sample_number=item[0], analog_input=float(item[1]) - float(item[2]), digital_code=item[3], digital_number_radix10=int(item[3], 2)))
        file_output.write("{sample_number}, {vin1_plus}, {vin1_minus}, {digital_code}, {analog_input:.6f}, {digital_number_radix10}\n".format(sample_number=item[0], vin1_plus=item[1], vin1_minus=item[2], digital_code=item[3], analog_input=float(item[1]) - float(item[2]), digital_number_radix10=int(item[3], 2)))
    file_output.close()

    # # 输出的编码遇到了问题，目前通过python替换的方式纠正一下编码的问题，coarse与实际值刚好反了
    # replace_str = {
    #     "000": "111",
    #     "001": "110",
    #     "010": "101",
    #     "011": "100",
    #     "100": "011",
    #     "101": "010",
    #     "110": "001",
    #     "111": "000",
    # }
    # replace_pattern = re.compile("|".join(replace_str.keys()))
    y = []
    for code in digital_code_list:
        # correct_012 = replace_pattern.sub(lambda m: replace_str[re.escape(m.group(0))], code[0:3])
        # correct = correct_012 + code[3:]
        # y.append(int(correct, 2))
        y.append(int(code, 2))

    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    ax.scatter(analog_input_list, y, s=5, c='#2cf02c')  # Plot some data on the axes.
    ax.plot(analog_input_list, list(map(lambda m: int(m/2.5*4096), analog_input_list)), linestyle='solid', c='#d62728', label='reference')  # Plot some data on the axes.
    ax.set_xlabel('analog input')
    ax.set_ylabel("digital code")
    ax.legend()
    # matplotlib.pyplot.xlabel('analog input')
    # matplotlib.pyplot.ylabel('digital code')
    # plt.xlabel('analog input')
    # plt.ylabel("digital code")

    plt.show()