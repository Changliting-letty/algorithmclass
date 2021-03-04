# -*- coding: UTF-8 -*-
# import matplotlib.pyplot as plt
import math
import time
import  src.randompoint  as  randompoint


def sort_polar(point_list,target_point):
    """
    :param point_list:  点集
    :param target_point:  基准点
    :return:  按照余弦，排序
    """
    cos_list= []
    rank_list = []
    norm_list = []  #存方向向量的模
    for i in range(len(point_list)):
        this_point= point_list[i]
        point = [this_point[0] - target_point[0], this_point[1] - target_point[1]]
        rank_list.append(i)
            #求向量
        norm_value = math.sqrt(point[0] * point[0] + point[1] * point[1])
        norm_list.append(norm_value)
        if norm_value == 0:
            cos_list.append(1)
        else:
            cos_list.append(point[0] / norm_value)  #方向向量的余玄值

#按照余玄值进行排序,分别排序三个列表中的值，使用的是冒泡排序
    for i in range(0,len(point_list)-1):
        index = i + 1
        while index > 0:
            if cos_list[index] > cos_list[index - 1] or (
                    cos_list[index] == cos_list[index - 1]
                    and norm_list[index] > norm_list[index - 1]):  #余玄值相同的选择较长的
                    temp = cos_list[index]
                    temp_rank = rank_list[index]
                    temp_norm = norm_list[index]
                    cos_list[index] = cos_list[index - 1]
                    rank_list[index] = rank_list[index - 1]
                    norm_list[index] = norm_list[index - 1]
                    cos_list[index - 1] = temp
                    rank_list[index - 1] = temp_rank
                    norm_list[index - 1] = temp_norm
                    index = index - 1
            else:
                break
    sorted_points = []
    for i in rank_list:
        sorted_points.append(point_list[i])

    return sorted_points  #将排好序的点返回


def get_small_y_point_index(point_list):
    """

    :param point_list: 点集列表[(1,2),(4,9)形式]
    :return: 点集中y值最小的点在列表中的索引,相同y值的取X小的
    """
    min= 0
    for i in range(len(point_list)):
        if(point_list[i][1]<point_list[min][1] or (point_list[i][1]==point_list[min][1] and point_list[i][0]<point_list[min][0])):
            min=i
    return min


#两个向量叉乘，相当于|a|*|b|*sin@
def coss(v1, v2):
    return v1[0] * v2[1] - v1[1] * v2[0]



def grahamscan(point_list):
  #  if len(point_list) <3 :
   #     print "点数少与3，构不成凸包"
   #     return []
    if len(point_list) <=3:
        return  point_list
    y_smallset_point_index=get_small_y_point_index(point_list) #得到y值最小的点M的索引，该点一定在凸包集合上
    bottom_point=point_list.pop(y_smallset_point_index)  #取出最小点M,并且从点集中删除
    #将点集除M之外的点按照极角排序
    sorted_list=sort_polar(point_list,bottom_point)

     #使用列表模拟栈，来完成这个扫描的过程
    stack = []
    #将y值最小的M点和极角距离它最近的两个点入栈
    stack.append(bottom_point)
    stack.append(sorted_list[0])
    stack.append(sorted_list[1])

    for i in range(2,len(sorted_list)):
        length = len(stack)
        top = stack[length - 1]  #取栈顶元素
        next_top = stack[length - 2]  #取栈顶倒数第二个元素

        #使用两个叉乘，判断是否造成左转，如果叉乘大于等于0，说明栈顶元素造成左转了，需要删除栈顶元素。值为正满足条件
        v1 = [sorted_list[i][0] - next_top[0], sorted_list[i][1] - next_top[1]]
        v2 = [top[0] - next_top[0], top[1] - next_top[1]]

        while coss(v1, v2) >= 0:   #循环判断栈内元素是否造成左转，有便删除栈顶元素，直至无左转
            if length < 3:  # 加上这两行代码之后，数据量很大时不会再报错
                break
            stack.pop()  #此时有左转，删除栈顶元素
            length = len(stack)
            top = stack[length - 1]
            next_top = stack[length - 2]
            v1 = [sorted_list[i][0] - next_top[0], sorted_list[i][1] - next_top[1]]
            v2 = [top[0] - next_top[0], top[1] - next_top[1]]
        stack.append(sorted_list[i])

    return stack








if __name__ == "__main__":
   # number = 100
  #  point_list = randompoint.get_many_point(number, 0, 100)
  #  convex_hull = grahamscan(point_list)

   # print convex_hull
   x=[(0,9),(0,5)]
   y=get_small_y_point_index(x)
   print y