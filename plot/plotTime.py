import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.font_manager import FontProperties
rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['Times New Roman','Sim sun']
# # 设置字号为12
rcParams['font.size'] = 14
font_song = FontProperties(fname=r'C:\Windows\Fonts\simsun.ttc') 

def plot_bar_chart(data):
    x = [str(x)+"×"+str(x) for x in [256,348,512,640]]  # 生成x轴坐标
    plt.bar(x, data,width=0.5)  # 绘制柱状图
    for i, value in enumerate(data):
        plt.text(i, value, str(value), ha='center', va='bottom')
    plt.xlabel('分辨率',fontproperties=font_song)  # 设置x轴标签
    plt.ylabel('单张耗时/秒',fontproperties=font_song)  # 设置y轴标签
    # plt.title('Processing time')  # 设置图表标题
    
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.savefig("Processing_time"+".png");
    plt.show()  # 显示图表
    
# 示例数据
data = [0.044, 0.067, 0.098, 0.155]

# 绘制柱状图
plot_bar_chart(data)