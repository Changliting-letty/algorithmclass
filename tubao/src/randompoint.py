# -*- coding: UTF-8 -*-
import random

"""
  实现：矩形内的随机多个点
  参数说明：
  input：
      number: 生成随机点的个数
      left:生成随机数的左阈值
      right:生成随机数的右阈值
   output:
        number个点的列表   
"""
def get_many_point(number,left,right):
    point_list=[]
    xlist=[]
    ylist=[]
    for i  in  range(number):
        x = random.randint(left, right)
        y = random.randint(left, right)
        if(x not in xlist and y not in ylist):
            xlist.append(x)
            ylist.append(y)
            point_list.append([x,y])
    return point_list

if  __name__=="__main__":
    number=100;  #生成随机点的个数
    point_list=get_many_point(number,0,100)
    print point_list