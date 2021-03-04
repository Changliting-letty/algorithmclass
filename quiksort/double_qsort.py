# -*- coding: UTF-8 -*-
import random
import  bigrandom  as bigdata
import  time
'''
双路快排分区基函数
输入：nums:待排序数组，l，r:待分区的数组的起始位置，数组长度减一
作用：在数组中随机选取一个元素视为基准元素v，并将所有小于v的元素放到左边，大数放到右边
输出：返回正确分割索引j即小于与大于的分界
'''
def partition_double(nums,l,r):
    m=random.randint(l,r)#randint产生一个随机数
    nums[l],nums[m]=nums[m],nums[l]#将上一程序的第一元素为基准数改为随机数，这样下面的内容就跟partition_first_base一样
    v=nums[l]#以第一个元素为基准元素
    i,j=l+1,r
    while True:
        while i<=r and nums[i]<v:
            i+=1
        while j>=1 and nums[j]>v:
            j-=1
        if i>j:
            break
        else:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1
    nums[j],nums[l]=nums[l],nums[j]
    return j
'''
双路快排函数
输入：待排序数组，l:数组起始位置，r：数组长度-1
作用：将数组进行排序
输出：返回已排好的数组
'''
def quick_sort_double(nums,l,r):
    if l<r:
        m=partition_double(nums,l,r)
        quick_sort_double(nums,l,m-1)
        quick_sort_double(nums,m+1,l)
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
        quick_sort_double(test, 0, 1000000-1)
        #quicksort(test,0,10000-1)
     #   test.sort()
        end=time.time()
        print "10^6个重复数：%d的数据集排序时间" %repeatnumber,round(end-start,2)
        print "排序后前50个数："
        print test[0:50]
