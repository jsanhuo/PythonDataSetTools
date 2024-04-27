import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib import rcParams

rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['Times New Roman']
# 设置字号为12
rcParams['font.size'] = 12

#             RESCAN     PReNet   MPRNet   OURS
datalabel_test1200 = ["OURS", "MPRNet"]
psnr_test1200 = [33.11,32.91]
ssim_test1200 = [0.924,0.916]
time_test1200 = [0.097,0.14]

datalabel_test2800 = ["OURS", "MPRNet"]
psnr_test2800 = [33.43,33.64]
ssim_test2800 = [0.937,0.938]
time_test2800 = [0.079,0.12]



def draw3D_Test1200():
    # 散点图
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    ax.scatter(xs=psnr_test1200[0], ys=ssim_test1200[0], zs=time_test1200[0], zdir='z', s=50, c="r", depthshade=True, cmap="jet", marker="o")


    ax.scatter(xs=psnr_test1200[1], ys=ssim_test1200[1], zs=time_test1200[1], zdir='z', s=30, c="g", depthshade=True, cmap="jet", marker="o")



    ax.text(psnr_test1200[0]-0.2, ssim_test1200[0], time_test1200[0]+0.004,
            f'{datalabel_test1200[0]}\n({psnr_test1200[0]}, {ssim_test1200[0]}, {time_test1200[0]})')
    ax.text(psnr_test1200[1]-0.2, ssim_test1200[1], time_test1200[1]+0.004,
            f'{datalabel_test1200[1]}\n({psnr_test1200[1]}, {ssim_test1200[1]}, {time_test1200[1]})')
    ax.set_xlabel('PSNRSSIM')
    ax.set_ylabel('SSIM',labelpad=10)
    ax.set_zlabel('Ave.inf.time (s)')
    # 设置 x y z 的范围
    # ax.set_xlim(32.8,33.2)
    ax.set_xticks([32.8,33,33.2])
    ax.set_yticks([0.91,0.92,0.93])
    ax.set_zticks([0.08, 0.12, 0.16])
    ax.grid(linestyle='dashed')
    plt.show()

if __name__ == '__main__':
    draw3D_Test1200()