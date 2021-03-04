# -*- coding:utf-8 -*-
from matplotlib import pyplot as plt
import  numpy as np
import  time


plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
#matplotlib画图中中文显示会有问题，需要这两行设置默认字体

#画凸包

def drow_contex(convex_hull,pointlist,title):
    all_x= [i[0] for i in pointlist]
    all_y=[i[1] for i in pointlist]
    area = np.pi * 4 ** 2  # 点面积
    #画散点
    plt.scatter(all_x,all_y, s=area, c='#DC143C', alpha=0.4)
    #画框
    convex_hull.append(convex_hull[0])
    for i in range(len(convex_hull)-1):
        x1=convex_hull[i][0]
        y1=convex_hull[i][1]
        x2=convex_hull[i+1][0]
        y2=convex_hull[i+1][1]
        plt.plot([x1,x2],[y1,y2],linewidth = '0.5',color='#000000')
   # plt.plot([convex_hull[0][0],convex_hull[-1][0]], [convex_hull[0][1],convex_hull[-1][1]], linewidth='0.5', color='#000000')
    plt.title(title)
    plt.show()