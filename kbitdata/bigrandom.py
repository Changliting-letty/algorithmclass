# -*- coding: UTF-8 -*-
import random


"""
  实现：矩形内的随机多个点
  参数说明：
  input：
      number: 生成随机点的个数
      left:生成随机数的左阈值
      right:生成随机数的右阈值
      repeatenum: 重复的数据
   output:
        number个点的列表   
"""
def get_many_data(number,left,right):
    data_list=[]
    for i  in  range(number):
        x = random.randint(left, right)
        data_list.append(x)

    return data_list

if  __name__=="__main__":
    number=100;  #生成随机点的个数
    point_list=get_many_point(number,0,100)
    print point_list