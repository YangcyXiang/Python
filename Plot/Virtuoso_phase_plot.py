import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager  # Chinese character
from matplotlib.ticker import EngFormatter  # engineering_formatter
from matplotlib.ticker import FixedLocator, LogLocator, MultipleLocator, MaxNLocator
import numpy as np
import csv

from matplotlib.backends.backend_pgf import FigureCanvasPgf
matplotlib.backend_bases.register_backend('pdf', FigureCanvasPgf)

font_path = r"C:/Windows/Fonts/simsun.ttc"  # Your font path goes here
font_manager.fontManager.addfont(font_path)
prop = font_manager.FontProperties(fname=font_path)

config = {
    "font.family": 'serif',
    "font.serif": prop.get_name(),
    # "font.size": 14,  # 五号，10.5磅
    # "axes.unicode_minus": False,
    # "text.usetex": True,
    # "mathtext.fontset": "stix",  # 设置 LaTeX 字体，stix 近似于 Times 字体
}
plt.rcParams.update(config)

def phase_corner_plot(csv_file_name, img_file_name):
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
    ax.yaxis.set_major_locator(FixedLocator(np.arange(-260, 20, 20)))

    # TT
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
    ax.set_xlabel(r'频率 ($Hz$)')
    ax.set_ylabel(r'相位 (\textdegree)')
    # ax.set_title('Scatter Plot of Data')
    plt.grid(visible=True, linestyle='--')
    ax.legend()

    # save image before show
    plt.savefig(img_file_name, format='pdf', dpi=300)

    # Show the plot
    plt.show()


if __name__ == '__main__':
    # # CITA amp
    # phase_corner_plot(csv_file_name='./data/ROIC512U30_2023AUT_CTIA_AMP_V2_sim_phase_corner.csv',
    #                   img_file_name='./img/ROIC512U30_2023AUT_CTIA_AMP_V2_sim_phase_corner.pdf'
    #                   )
    # # COLUMN amp
    # phase_corner_plot(csv_file_name='./data/ROIC512U30_2023AUT_COLUMN_AMP_V2_sim_phase_corner.csv',
    #                   img_file_name='./img/ROIC512U30_2023AUT_COLUMN_AMP_V2_sim_phase_corner.pdf'
    #                   )
    # TERMINAL amp
    phase_corner_plot(csv_file_name='./data/ROIC512U30_2023AUT_TERMINAL_AMP_V2_sim_phase_corner.csv',
                      img_file_name='./img/ROIC512U30_2023AUT_TERMINAL_AMP_V2_sim_phase_corner.pdf'
                      )
