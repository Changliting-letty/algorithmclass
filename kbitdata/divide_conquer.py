# -*- coding:utf-8 -*-
import random
import  time
import bigrandom as brand


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

def divide_conquer(datalist,p,r,k):
        q=rand_partion(datalist,p,r)
        if (q==k-1):
            return datalist[q]
        elif (q<k):
            return  divide_conquer(datalist,q+1,r,k)
        else:
            return  divide_conquer(datalist,p,q-1, k)

if __name__ == "__main__":
    # 小数据集测试

    datasize_list = [1000, 2000, 5000, 10000, 20000, 50000, 100000]
    # 从列表中随机选择一个数据集大小
    datasize = random.choice(datasize_list)
    # 随机生成datasize个范围再(0,1000000)的数
    datalist = brand.get_many_data(datasize, 0, 1000000)
    # print  datalist[0:30]
    k=input('请输入k值:(k<%d)'%datasize)
    m = divide_conquer(datalist, 0, datasize - 1, k)
    print m
    ##用于验证正确
    datalist.sort()
    print datalist[0:30]
