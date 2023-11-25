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
    plt.scatter(time, psnr)  # 绘制散点图
    plt.xlabel("Ave.inf.time (s)")  # 设置x轴标签
    plt.ylabel("PSNR (dB)")  # 设置y轴标签
    plt.xlim(0.005,0.032)
    plt.ylim(28,33.5)
    # plt.tick_params(axis='both', which='both', length=0)
    for i, label in enumerate(datalabel):
        plt.text(time[i]+0.001, psnr[i]+0.1, label,ha='center', va='bottom')
    plt.savefig("Ave.inf.time (s)"+"_"+"PSNR (dB)"+".png");
    plt.show()

def plot_Par_PSNR_scatter():
    x = par
    y = psnr
    xlable = "Parameters (Millions)"
    ylable = "PSNR (dB)"
    plt.scatter(x, y)  # 绘制散点图
    plt.xlabel(xlable)  # 设置x轴标签
    plt.ylabel(ylable)  # 设置y轴标签
    plt.xlim(0,4.1)
    plt.ylim(28,33.5)
    # plt.tick_params(axis='both', which='both', length=0)
    for i, label in enumerate(datalabel):
        plt.text(x[i]+0.15, y[i]+0.1, label,ha='center', va='bottom')
    plt.savefig(xlable+"_"+ylable+".png");
    plt.show()


def plot_Par_SSIM_scatter():
    x = par
    y = ssim
    xlable = "Parameters (Millions)"
    ylable = "SSIM"
    plt.scatter(x, y)  # 绘制散点图
    plt.xlabel(xlable)  # 设置x轴标签
    plt.ylabel(ylable)  # 设置y轴标签
    plt.xlim(0,4.1)
    plt.ylim(0.8,1)
    # plt.tick_params(axis='both', which='both', length=0)
    for i, label in enumerate(datalabel):
        plt.text(x[i]+0.15, y[i]+0.005, label,ha='center', va='bottom')
    plt.savefig(xlable+"_"+ylable+".png");
    plt.show()

def plot_Time_SSIM_scatter():
    x = time
    y = ssim
    xlable = "Ave.inf.time (s)"
    ylable = "SSIM"
    plt.scatter(x, y)  # 绘制散点图
    plt.xlabel(xlable)  # 设置x轴标签
    plt.ylabel(ylable)  # 设置y轴标签
    plt.xlim(0.005,0.032)
    plt.ylim(0.8,1)
    # plt.tick_params(axis='both', which='both', length=0)
    for i, label in enumerate(datalabel):
        plt.text(x[i]+0.001, y[i]+0.005, label,ha='center', va='bottom')
    plt.savefig(xlable+"_"+ylable+".png");
    plt.show()

if __name__ == '__main__':
    plot_Time_PSNR_scatter()
    plt.cla()
    plot_Par_PSNR_scatter()
    plt.cla()
    plot_Par_SSIM_scatter()
    plt.cla()
    plot_Time_SSIM_scatter()