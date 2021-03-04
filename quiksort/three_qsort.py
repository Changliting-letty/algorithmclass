# -*- coding: UTF-8 -*-
import random
import  bigrandom  as bigdata
import  time

import random
'''
三路快排分区基函数
输入：nums:待排序数组，l，r:待分区的数组的起始位置，数组长度减一
作用：在数组中随机选取一个元素视为基准元素v，划分为三区间
输出：返回正确分割索引lt,gt即小于与大于的分界
'''

def partition_three_ways(nums,l,r):
    m=random.randint(l,r)#randint产生一个随机数
    nums[l],nums[m]=nums[m],nums[l]#将上一程序的第一元素为基准数改为随机数，这样下面的内容就跟partition_first_base一样
    v=nums[l]#以第一个元素为基准元素
    lt=l # nums[l+1...lt]<v,lt初始化为l,保证其刚开始为无效数组
    gt=r+1# nums[gt...len(nums)-1]>v
    i=l+1 # nums[lt+1...i]==v
    while i<gt:
        # i==gt时表示已经比较结束
        if nums[i]<v:
            nums[i],nums[lt+1]=nums[lt+1],nums[i]
            lt+=1
            i+=1
        elif nums[i]>v:
            nums[i],nums[gt-1]=nums[gt-1],nums[i]
            gt-=1
        else:# nums[i]==v
            i+=1
    nums[l],nums[lt]=nums[lt],nums[l]
    return lt,gt
'''
三路快排函数
输入：待排序数组，l:数组起始位置，r：数组长度-1
作用：将数组进行排序
输出：返回已排好的数组
'''
def quick_sort_three_ways(nums,l,r):
    if l<r:
        lt,gt= partition_three_ways(nums,l,r)
        quick_sort_three_ways(nums,l,lt-1)
        quick_sort_three_ways(nums,gt,r)
    return nums



if __name__ == "__main__":
    #尝试无重复数据集的排序
    for i in range(11):
        repeatnumber=100000*i       # print repeatnumber
        test=bigdata.get_many_data(1000000,0,1000000,repeatnumber)
        print "开始10^6个，重复数为：%d的内置函数sort排序...." %repeatnumber
       # shuffle(test)
        start=time.time()
        #print len(test)
        quick_sort_three_ways(test, 0, 1000000-1)
        #quicksort(test,0,10000-1)
     #   test.sort()
        end=time.time()
        print "10^6个重复数：%d的数据集排序时间" %repeatnumber,round(end-start,2)
        print "排序后前50个数："
        print test[0:50]
