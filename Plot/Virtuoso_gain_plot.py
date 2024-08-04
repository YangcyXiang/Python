import matplotlib.pyplot as plt
from matplotlib import font_manager  # Chinese character
from matplotlib.ticker import EngFormatter  # engineering_formatter
from matplotlib.ticker import FixedLocator, LogLocator, MultipleLocator, MaxNLocator
import numpy as np
import csv

font_SongTi = font_manager.FontProperties(fname="C:/Windows/Fonts/simsun.ttc")


def gain_corner_plot(csv_file_name, img_file_name):
    # Get data from .csv file
    gain_x_tt = []
    gain_y_tt = []
    gain_x_ss = []
    gain_y_ss = []
    gain_x_ff = []
    gain_y_ff = []

    # Load the data
    with open(csv_file_name, 'r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        for row in lines:
            gain_x_tt.append(row[0])  # IT'S STRING !!!
            gain_y_tt.append(row[1])
            gain_x_ss.append(row[2])
            gain_y_ss.append(row[3])
            gain_x_ff.append(row[4])
            gain_y_ff.append(row[5])

    fig, ax = plt.subplots()

    # set x axis and y axis
    ax.set_xscale('log')
    ax.xaxis.set_major_locator(FixedLocator([0, 1, 10, 100, 1000, 1e4, 1e5, 1e6, 1e7, 1e8, 1e9]))
    ax.xaxis.set_major_formatter(EngFormatter(places=0))
    ax.yaxis.set_major_locator(FixedLocator(np.arange(-120, 90, 10)))

    # color from Huang's TCAS-I
    # #ff1a1c red
    # #377eb8 blue
    # #4daf4a green
    # #ff7f00 orange
    # #a668b0 purple

    plt.plot([float(i) for i in gain_x_tt[2:-1]], [float(i) for i in gain_y_tt[2:-1]],
             's-',  # fmt = '[marker][line][color]'
             markersize=5,
             color='#377eb8',
             label='TT',
             # linewidth=4,
             # markerfacecolor='white',
             # markeredgecolor='gray',
             # markeredgewidth=2
             )
    # SS
    plt.plot([float(i) for i in gain_x_ss[2:-1]], [float(i) for i in gain_y_ss[2:-1]],
             'o-',  # fmt = '[marker][line][color]'
             markersize=5,
             color='#4daf4a',
             label='SS',
             # linewidth=4,
             # markerfacecolor='white',
             # markeredgecolor='gray',
             # markeredgewidth=2
             )

    # FF
    plt.plot([float(i) for i in gain_x_ff[2:-1]], [float(i) for i in gain_y_ff[2:-1]],
             '^-',  # fmt = '[marker][line][color]'
             markersize=5,
             color='#ff7f00',
             label='FF',
             # linewidth=4,
             # markerfacecolor='white',
             # markeredgecolor='gray',
             # markeredgewidth=2
             )

    # Add labels and title
    ax.set_xlabel('频率 (Hz)', fontproperties=font_SongTi)
    ax.set_ylabel('增益 (dB)', fontproperties=font_SongTi)
    # ax.set_title('Scatter Plot of Data')
    plt.grid(visible=True, linestyle='--')
    ax.legend()

    # save image before show
    plt.savefig(img_file_name, format='png', dpi=300)

    # Show the plot
    plt.show()


if __name__ == '__main__':
    gain_corner_plot(csv_file_name='./data/ROIC256U30_2023AUT_CTIA_AMP_V2_sim_gain_corner.csv',
                     img_file_name='./img/ROIC256U30_2023AUT_CTIA_AMP_V2_sim_gain_corner.png'
                     )
