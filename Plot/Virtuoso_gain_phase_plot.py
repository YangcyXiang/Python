import matplotlib.pyplot as plt
from matplotlib import font_manager # Chinese character
from matplotlib.ticker import EngFormatter # engineering_formatter
from matplotlib.ticker import FixedLocator, LogLocator, MultipleLocator, MaxNLocator
import numpy as np
import csv

font_SongTi = font_manager.FontProperties(fname="C:/Windows/Fonts/simsun.ttc")

# Get data from .csv file
gain_x_tt = []
gain_y_tt = []
gain_x_ss = []
gain_y_ss = []
gain_x_ff = []
gain_y_ff = []

# Load the data
with open('./data/ROIC256U30_2023AUT_CTIA_AMP_V2_sim_gain_corner.csv', 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        gain_x_tt.append(row[0]) # IT'S STRING !!!
        gain_y_tt.append(row[1])
        gain_x_ss.append(row[2])
        gain_y_ss.append(row[3])
        gain_x_ff.append(row[4])
        gain_y_ff.append(row[5])


fig, ax = plt.subplots()
ax.set_xscale('log')

formatter0 = EngFormatter(unit='Hz')
formatter1 = EngFormatter(places=1)  # U+2009
ax.xaxis.set_minor_locator(MaxNLocator)
# ax.xaxis.set_major_locator(LogLocator(base=10))
ax.xaxis.set_major_formatter(formatter1)

ax.yaxis.set_major_locator(FixedLocator(np.arange(-120, 90, 10)))

plt.plot([float(i) for i in gain_x_tt[2:-1]], [float(i) for i in gain_y_tt[2:-1]],
         '-p', # data dot marker
         color='#B3CAD8',
         label='TT',
        # markersize=15, linewidth=4,
        # markerfacecolor='white',
        # markeredgecolor='gray',
        # markeredgewidth=2
        )

# set x as log scale
# plt.yscale('log')

# Add labels and title
ax.set_xlabel('频率 (Hz)', fontproperties=font_SongTi)
ax.set_ylabel('增益 (dB)', fontproperties=font_SongTi)
# ax.set_title('Scatter Plot of Data')
ax.grid(True)
ax.legend()

# Show the plot
plt.show()
