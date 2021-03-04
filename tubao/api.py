# -*- coding: UTF-8 -*-

import math
import time
import src.randompoint  as  randompoint
import  enumerate as  meijv
import  grahamscan as  gra
import   divide_conquer as dc
import drow.drow  as drow
import  copy

"""
入口函数，可以选择两种方式执行
第一种 一次执行一类方法
第二种  一次执行三种方法进行比较
"""
def main1():
    while(True):
        time_list=[]  #三种方式的执行时间，用于画折线图进行比较
        datasize = input('请输入随机点的个数:')
        point_list1 = randompoint.get_many_point(datasize, 0, 100)  # 参数0和100表示点的坐标的范围
      #  print point_list

        point_list2=copy.deepcopy(point_list1)
        point_list3=copy.deepcopy(point_list1)
        start1 = time.time()
        # 枚举法
        temp1=meijv.enumerate_method(point_list1)# 暴力枚举法求凸包得到的凸包结果
        i1 = gra.get_small_y_point_index(temp1)
        convex_hull1 = gra.sort_polar(temp1,temp1[i1])    #按极角排序
        end1 = time.time()
        time1=end1-start1
        time_list.append(time1)
        #grhamscan法
        start2=time.time()
        temp2= gra.grahamscan(point_list2)
        i2=gra.get_small_y_point_index(temp2)
        convex_hull2 =gra.sort_polar(temp2,temp2[i2])
        end2 = time.time()
        time2 = end2-start2
        time_list.append(time2)
        #分治法
        start3 = time.time()
        sorted_point = sorted(point_list3, key=lambda x: x[0])
        temp3=dc.divide_conquer(sorted_point)
       # print "temp3" ,temp3
        i3= gra.get_small_y_point_index(temp3)
        convex_hull3 =gra.sort_polar(temp3,temp3[i3])
        end3 = time.time()
        time3 = end3-start3
        time_list.append(time3)
        #打印三种方式的结果
        print convex_hull1
        print time1

        print convex_hull2
        print time2

        print convex_hull3
        print time3
        drow.drow_contex(convex_hull1,point_list1,"Enumerate")
        drow.drow_contex(convex_hull2, point_list2, "Graham_scan")
        drow.drow_contex(convex_hull3, point_list3, "Divide_conquer")




# 产生随机点
if __name__ == "__main__":
    main1()



