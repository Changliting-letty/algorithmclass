# -*- coding: UTF-8 -*-

import  grahamscan  as graham_scan
import  src.randompoint  as  randompoint



def divide_conquer(point_list):
    #将点集按照x值进行排序
    if len(point_list)<6:  #当点数小于6的时候，再进行划分可能会有一边无法构成凸包，这个时候就用graham求凸包就行
        return  graham_scan.grahamscan(point_list)

    #取x值的中间值，将点集分为左右两个子问题
    merge_list=[]  #用于合并的点集
    middle_index=len(point_list)/2
    list1=divide_conquer(point_list[0:middle_index])
   # print "list1",list1
    list2=divide_conquer(point_list[middle_index:len(point_list)])
  #  print "list2",list2
    merge_list.extend(list1) #将左子问题的凸包集合加进来
    merge_list.extend(list2)#将右子问题的凸包集合加进来
    convex_hull=graham_scan.grahamscan(merge_list)  #将左右问题的并集最后进行一次凸包，进行合并
    return  convex_hull




if __name__ == "__main__":
    number = 100
    point_list = randompoint.get_many_point(number, 0, 100)
    sorted_point = sorted(point_list,key = lambda x: x[0])
    convex_hull = divide_conquer(sorted_point)
    print convex_hull



