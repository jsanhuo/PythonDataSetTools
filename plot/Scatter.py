import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib import rcParams

rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['Times New Roman']
# 设置字号为12
rcParams['font.size'] = 12

#             RESCAN     PReNet   MPRNet   OURS
datalabel = ["RESCAN", "PReNet" ,"MPRNet","OURS"]
time = [0.016,0.01,0.028,0.018]
psnr = [28.59,29.42,32.73,32.56]
ssim = [0.857,0.897,0.921,0.924]
par = [0.15,0.17,3.64,1.18]



def plot_Time_PSNR_scatter():
    x = time
    y = psnr
    plt.scatter(x[:3], y[:3])  # 绘制散点图
    plt.grid(linestyle='dashed')
    plt.xlabel("Ave.inf.time (s)")  # 设置x轴标签
    plt.ylabel("PSNRSSIM (dB)")  # 设置y轴标签
    plt.xlim(0.005,0.032)
    plt.ylim(28,33.5)

    plt.scatter(x[3], y[3], marker='*',s=200, edgecolors='none', color='red')
    # plt.tick_params(axis='both', which='both', length=0)
    for i, label in enumerate(datalabel):
        plt.text(x[i]+0.001, y[i]+0.1, label,ha='center', va='bottom')
        plt.text(x[i], y[i]-0.4, f'({x[i]}, {y[i]})', ha='center', va='bottom')
    plt.savefig("Ave.inf.time (s)"+"_"+"PSNRSSIM (dB)"+".png");
    plt.show()

def plot_Par_PSNR_scatter():
    x = par
    y = psnr
    xlable = "Parameters (Millions)"
    ylable = "PSNRSSIM (dB)"
    plt.grid(linestyle='dashed')
    plt.scatter(x[:3], y[:3])  # 绘制散点图
    plt.xlabel(xlable)  # 设置x轴标签
    plt.ylabel(ylable)  # 设置y轴标签
    plt.xlim(0,4.1)
    plt.ylim(28,33.5)

    plt.scatter(x[3], y[3], marker='*',s=200, edgecolors='none', color='red')
    # plt.tick_params(axis='both', which='both', length=0)
    for i, label in enumerate(datalabel):
        plt.text(x[i]+0.15, y[i]+0.1, label,ha='center', va='bottom')
        if (i in (0, 1)):
            plt.text(x[i] + 0.23, y[i] - 0.4, f'({x[i]}, {y[i]})', ha='center', va='bottom')
        else:
            plt.text(x[i], y[i] - 0.4, f'({x[i]}, {y[i]})', ha='center', va='bottom')

    plt.savefig(xlable+"_"+ylable+".png");
    plt.show()


def plot_Par_SSIM_scatter():
    x = par
    y = ssim
    xlable = "Parameters (Millions)"
    ylable = "SSIM"
    plt.grid(linestyle='dashed')
    plt.scatter(x[:3], y[:3])  # 绘制散点图
    plt.xlabel(xlable)  # 设置x轴标签
    plt.ylabel(ylable)  # 设置y轴标签
    plt.xlim(0,4.1)
    plt.ylim(0.8,1)
    plt.scatter(x[3], y[3], marker='*',s=200, edgecolors='none', color='red')
    # plt.tick_params(axis='both', which='both', length=0)
    for i, label in enumerate(datalabel):
        plt.text(x[i]+0.15, y[i]+0.005, label,ha='center', va='bottom')
        if(i in (0,1)):
            plt.text(x[i]+0.23, y[i] - 0.015, f'({x[i]}, {y[i]})', ha='center', va='bottom')
        else:
            plt.text(x[i], y[i] - 0.015, f'({x[i]}, {y[i]})', ha='center', va='bottom')
    plt.savefig(xlable+"_"+ylable+".png");
    plt.show()

def plot_Time_SSIM_scatter():
    x = time
    y = ssim
    xlable = "Ave.inf.time (s)"
    ylable = "SSIM"
    plt.grid(linestyle='dashed')
    plt.scatter(x[:3], y[:3])  # 绘制散点图
    plt.xlabel(xlable)  # 设置x轴标签
    plt.ylabel(ylable)  # 设置y轴标签
    plt.xlim(0.005,0.032)
    plt.ylim(0.8,1)
    plt.scatter(x[3], y[3], marker='*',s=200, edgecolors='none', color='red')
    # plt.tick_params(axis='both', which='both', length=0)
    for i, label in enumerate(datalabel):
        plt.text(x[i]+0.001, y[i]+0.005, label,ha='center', va='bottom')
        plt.text(x[i], y[i] - 0.015, f'({x[i]}, {y[i]})', ha='center', va='bottom')
    plt.savefig(xlable+"_"+ylable+".png");
    plt.show()






datalabel_test1200 = ["OURS", "MPRNet"]
psnr_test1200 = [33.11,32.91]
ssim_test1200 = [0.924,0.916]
time_test1200 = [0.097,0.14]

datalabel_test2800 = ["OURS", "MPRNet"]
psnr_test2800 = [33.43,33.64]
ssim_test2800 = [0.937,0.938]
time_test2800 = [0.079,0.12]

def plot_Test1200_Time_SSIM_scatter():
    x = time_test1200
    y = ssim_test1200
    xlable = "Ave.inf.time (s)"
    ylable = "SSIM"
    plt.grid(linestyle='dashed')
    plt.scatter(x, y)  # 绘制散点图
    plt.xlabel(xlable)  # 设置x轴标签
    plt.ylabel(ylable)  # 设置y轴标签
    plt.xlim(0.08,0.16)
    plt.ylim(0.91,0.93)
    # plt.scatter(x[3], y[3], marker='*
    # ',s=200, edgecolors='none', color='red')
    # plt.tick_params(axis='both', which='both', length=0)
    for i, label in enumerate(datalabel_test1200):
        plt.text(x[i], y[i]+0.0018, label,ha='center', va='bottom')
        plt.text(x[i], y[i]+0.0008, f'({x[i]}, {y[i]})', ha='center', va='bottom')
    plt.savefig("Test1200"+xlable+"_"+ylable+".png");
    plt.show()


def plot_Test1200_Time_PSNR_scatter():
    x = time
    y = psnr
    plt.scatter(x[:3], y[:3])  # 绘制散点图
    plt.grid(linestyle='dashed')
    plt.xlabel("Ave.inf.time (s)")  # 设置x轴标签
    plt.ylabel("PSNRSSIM (dB)")  # 设置y轴标签
    plt.xlim(0.005,0.032)
    plt.ylim(28,33.5)

    plt.scatter(x[3], y[3], marker='*',s=200, edgecolors='none', color='red')
    # plt.tick_params(axis='both', which='both', length=0)
    for i, label in enumerate(datalabel):
        plt.text(x[i]+0.001, y[i]+0.1, label,ha='center', va='bottom')
        plt.text(x[i], y[i]-0.4, f'({x[i]}, {y[i]})', ha='center', va='bottom')
    plt.savefig("Ave.inf.time (s)"+"_"+"PSNRSSIM (dB)"+".png");
    plt.show()




if __name__ == '__main__':
    plot_Test1200_Time_SSIM_scatter()
    plt.cla()
    # plot_Test1200_Time_PSNR_scatter()
    # plt.cla()