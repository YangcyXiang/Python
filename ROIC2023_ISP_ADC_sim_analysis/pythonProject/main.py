import re
import numpy as np
import matplotlib.pyplot as plt

# line = "128, 0.055187, 000001111101, 000001111000, 0.054932, 0.052734"

adc_pattern = re.compile(
    "(?P<sample_number>\d+), (?P<ANALOG_INPUT_V>\d+(.\d+)*), (?P<SAR_ADC_OUTPUT_Q11_2_Q0>\d+), (?P<IDEAL_ADC_OUTPUT_Q11_2_Q0>\d+), (?P<SAR_ADC_OUTPUT_V>\d+(.\d+)*), (?P<IDEAL_ADC_OUTPUT_V>\d+(.\d+)*)")

file_pre_layout = open(file='./data/pre-layout-adc_12bit_sample-output.txt', mode='r')
list_pre_layout_sample_number = []
list_pre_layout_analog_input = []
list_pre_layout_sar = []
list_pre_layout_ideal = []
list_pre_layout_delta = []
while True:
    line_pre_layout = file_pre_layout.readline()
    if line_pre_layout is None:
        break
    elif line_pre_layout == '':
        break

    re_pre_layout = adc_pattern.search(line_pre_layout)
    if re_pre_layout is None:
        continue
    else:
        int_sample_number = int(re_pre_layout.group('sample_number'))
        print(int_sample_number)
        list_pre_layout_sample_number.append(int_sample_number)

        float_analog_input = float(re_pre_layout.group('ANALOG_INPUT_V'))
        print(float_analog_input)
        list_pre_layout_analog_input.append(float_analog_input)

        int_pre_layout_SAR_ADC_OUTPUT = int(re_pre_layout.group('SAR_ADC_OUTPUT_Q11_2_Q0'), 2)
        print(int_pre_layout_SAR_ADC_OUTPUT)
        list_pre_layout_sar.append(int_pre_layout_SAR_ADC_OUTPUT)

        int_pre_layout_IDEAL_ADC_OUTPUT = int(re_pre_layout.group('IDEAL_ADC_OUTPUT_Q11_2_Q0'), 2)
        print(int_pre_layout_IDEAL_ADC_OUTPUT)
        list_pre_layout_ideal.append(int_pre_layout_IDEAL_ADC_OUTPUT)
        list_pre_layout_delta.append(int_pre_layout_SAR_ADC_OUTPUT - int_pre_layout_IDEAL_ADC_OUTPUT)  # 实际值减去理论值
file_pre_layout.close()

fig1, axs_pre_layout = plt.subplots(2, 1, layout='constrained')
axs_pre_layout[0].scatter(list_pre_layout_analog_input[234:4102], list_pre_layout_sar[234:4102], s=1, label="sar adc output")
axs_pre_layout[0].scatter(list_pre_layout_analog_input[234:4102], list_pre_layout_ideal[234:4102], s=1, label="ideal adc output")
axs_pre_layout[1].scatter(list_pre_layout_analog_input[234:4102], list_pre_layout_delta[234:4102], s=1, label="delta")
axs_pre_layout[0].set(xlabel='analog input', ylabel='output number', title='pre layout ADC result')
axs_pre_layout[1].set(xlabel='analog input', ylabel='delta(ideal-sar)', title='pre layout ADC result')
plt.legend()
# plt.show()


list_pre_layout_sar_calibrated = []
list_pre_layout_delta_calibrated = []
(slope, intercept) = np.polyfit(list_pre_layout_analog_input[234:4102], list_pre_layout_sar[234:4102], 1)
for item in list_pre_layout_sar:
    list_pre_layout_sar_calibrated.append( 4096*(item-intercept)/(1.8*slope) )

for i in range(len(list_pre_layout_sar_calibrated)):
    list_pre_layout_delta_calibrated.append(list_pre_layout_sar_calibrated[i]-list_pre_layout_ideal[i])

fig2, axs_pre_layout = plt.subplots(2, 1, layout='constrained')
axs_pre_layout[0].scatter(list_pre_layout_analog_input[234:4102], list_pre_layout_sar_calibrated[234:4102], s=1, label="sar adc output(calibrated)")
axs_pre_layout[0].scatter(list_pre_layout_analog_input[234:4102], list_pre_layout_ideal[234:4102], s=1, label="ideal adc output")
axs_pre_layout[1].scatter(list_pre_layout_analog_input[234:4102], list_pre_layout_delta_calibrated[234:4102], s=1, label="delta")
axs_pre_layout[0].set(xlabel='analog input', ylabel='output number', title='pre layout ADC result(calibrted)')
axs_pre_layout[1].set(xlabel='analog input', ylabel='delta(ideal-sar) calibrated', title='pre layout ADC result')
plt.legend()
# plt.show()


file_post_layout = open(file='./data/post-layout-adc_12bit_sample-output.txt', mode='r')
list_post_layout_sample_number = []
list_post_layout_analog_input = []
list_post_layout_sar = []
list_post_layout_ideal = []
list_post_layout_delta = []
while True:
    line_post_layout = file_post_layout.readline()
    if line_post_layout is None:
        break
    elif line_post_layout == '':
        break

    re_post_layout = adc_pattern.search(line_post_layout)
    if re_post_layout is None:
        continue
    else:
        int_sample_number = int(re_post_layout.group('sample_number'))
        print(int_sample_number)
        list_post_layout_sample_number.append(int_sample_number)

        float_analog_input = float(re_post_layout.group('ANALOG_INPUT_V'))
        print(float_analog_input)
        list_post_layout_analog_input.append(float_analog_input)

        int_post_layout_SAR_ADC_OUTPUT = int(re_post_layout.group('SAR_ADC_OUTPUT_Q11_2_Q0'), 2)
        print(int_post_layout_SAR_ADC_OUTPUT)
        list_post_layout_sar.append(int_post_layout_SAR_ADC_OUTPUT)

        int_post_layout_IDEAL_ADC_OUTPUT = int(re_post_layout.group('IDEAL_ADC_OUTPUT_Q11_2_Q0'), 2)
        print(int_post_layout_IDEAL_ADC_OUTPUT)
        list_post_layout_ideal.append(int_post_layout_IDEAL_ADC_OUTPUT)
        list_post_layout_delta.append(int_post_layout_SAR_ADC_OUTPUT - int_post_layout_IDEAL_ADC_OUTPUT)  # 实际值减去理论值
file_post_layout.close()

fig3, axs_post_layout = plt.subplots(2, 1, layout='constrained')
axs_post_layout[0].scatter(list_post_layout_analog_input[234:4102], list_post_layout_sar[234:4102], s=1, label="sar adc output")
axs_post_layout[0].scatter(list_post_layout_analog_input[234:4102], list_post_layout_ideal[234:4102], s=1, label="ideal adc output")
axs_post_layout[1].scatter(list_post_layout_analog_input[234:4102], list_post_layout_delta[234:4102], s=1, label="delta")
axs_post_layout[0].set(xlabel='analog input', ylabel='output number', title='post layout ADC result')
axs_post_layout[1].set(xlabel='analog input', ylabel='delta(ideal-sar)', title='post layout ADC result')
plt.legend()
# plt.show()


list_post_layout_sar_calibrated = []
list_post_layout_delta_calibrated = []
(slope, intercept) = np.polyfit(list_post_layout_analog_input[234:4102], list_post_layout_sar[234:4102], 1)
for item in list_post_layout_sar:
    list_post_layout_sar_calibrated.append( 4096*(item-intercept)/(1.8*slope) )

for i in range(len(list_post_layout_sar_calibrated)):
    list_post_layout_delta_calibrated.append(list_post_layout_sar_calibrated[i]-list_post_layout_ideal[i])

fig4, axs_post_layout = plt.subplots(2, 1, layout='constrained')
axs_post_layout[0].scatter(list_post_layout_analog_input[234:4102], list_post_layout_sar_calibrated[234:4102], s=1, label="sar adc output(calibrated)")
axs_post_layout[0].scatter(list_post_layout_analog_input[234:4102], list_post_layout_ideal[234:4102], s=1, label="ideal adc output")
axs_post_layout[1].scatter(list_post_layout_analog_input[234:4102], list_post_layout_delta_calibrated[234:4102], s=1, label="delta")
axs_post_layout[0].set(xlabel='analog input', ylabel='output number', title='post layout ADC result(calibrted)')
axs_post_layout[1].set(xlabel='analog input', ylabel='delta(ideal-sar) calibrated', title='post layout ADC result')
plt.legend()
plt.show()