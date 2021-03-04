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
def get_many_data(number,left,right,repeatnum):
    data_list=[]
    #首先生成不重复的数
    if repeatnum<number:
        for i  in  range(number-repeatnum):
            x = random.randint(left, right)
            data_list.append(x)
        #生成重复数据,随机选择一个点，重复repeatenum
        datacopy=random.choice(data_list)
        test=[datacopy for i in range(repeatnum)]
        data_list.extend(test)
       # if(repeatnum!=0):
        #    for i  in range(30):
         #       random.shuffle(data_list)
               #print i
    else:
        #对于生成10^6个重复数的情况
        x = random.randint(left, right)
        data_list=[x for i in range(repeatnum)]


    return data_list

if  __name__=="__main__":
    number=100;  #生成随机点的个数
    point_list=get_many_point(number,0,100)
    print point_list