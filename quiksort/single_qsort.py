# -*- coding: UTF-8 -*-

import random
from  random import  shuffle
import  bigrandom  as bigdata
import  time
import sys

sys.setrecursionlimit(1000000)


def rand_partion(datalist,p,r):
    i=random.randint(p,r)    #产生指定范围内的整数
  #  x, y = y, x
    datalist[i],datalist[r]=datalist[r],datalist[i]
    x=datalist[r]  #基准
    i=p-1  #最小元素索引
    for j in range(p,r):
        if(datalist[j]<=x):
            i+=1
            datalist[i], datalist[j] = datalist[j], datalist[i]
    datalist[i+1], datalist[r] = datalist[r], datalist[i+1]

    return  i+1

def quicksort(datalist,p,r):
    if (p<r):
        q=rand_partion(datalist,p,r)
        quicksort(datalist,p,q-1)
        quicksort(datalist,q+1,r)




if __name__ == "__main__":
  #  test = bigdata.get_many_data(10000, 0, 1000000, repeatnumber)
    #小数据集测试

   # a=[1,5,7,12,45,2,79,23,12]
   # a=[1,2,2,2,2,2,2,2,2,2,2,]

    #print "小数据集测试,排序前"
    #print a
   # n=len(a)
  #  quicksort(a,0,n-1)
 #   print "小数据集测试,排序后"
#    print a

    #尝试无重复数据集的排序
   # for i in range(5):
        repeatnumber=100000*5       # print repeatnumber
        test=bigdata.get_many_data(1000000,0,1000000,repeatnumber)
        print "开始10^6个，重复数为：%d的内置函数sort排序...." %repeatnumber
        shuffle(test)
        start=time.time()
        #print len(test)
        #quicksort(test,0,10000-1)
        test.sort()
        end=time.time()
        print "10^6个重复数：%d的数据集排序时间" %repeatnumber,round(end-start,2)
        print "排序后前50个数："
        print test[0:50]




