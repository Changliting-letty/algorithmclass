# -*- coding:utf-8 -*-
import  random
import bigrandom as brand
import  math
import  time
import  divide_conquer as dc

# 独立、均匀、可放回地从S随机选取的n^3/4元素;
def getsonlist(dalist,num):
    """
    :param dalist:源数据集
    :param num:  要随机取数的个数
    :return:  随机选取的含num个元素的子集
    """
    return  random.sample(dalist,num)

#在O(n) 时间内排序R;计数排序
def count_sort(R):
    if len(R) < 2:
        return R
    max_num = max(R)
    count = [0] * (max_num + 1)
    for num in R:
        count[num] += 1
    new_array = list()
    for i in range(len(count)):
        for j in range(count[i]):
            new_array.append(i)
    return new_array


def get_rank(S,L):
    """
    :param S: 数据集
    :param L: 数据集中的一个元素
    :return:  排完序后L是第几小
    """
    index=0
    for i in range(len(S)):
        if S[i] < L:
            index +=1



    return index

    #S.sort()
    #for i in range(len(S)):
     #   if S[i]==L:
     #       return i+1
   # print "L不在S中，异常"
   # return  None


def lazy_select(datalist,l,r,k):
    """
    2021-1-2
    :param datalist: 数据集
    :param l:  最左边index
    :param r: 最右边index
    :param k:   求的第K小
    :return:   数据集中第k小的值
    """
        #i=0
    while(True):
            #独立、均匀、可放回地从S随机选取的n^3/4元素;
        length=len(datalist)
        s= round(8.0/8.0,2)
        datasize=int (length**s)  #随机数据集的大小
      #  print datasize
        R=getsonlist(datalist,datasize)
        #在O(n) 时间内排序R;
        sort_R=count_sort(R)
        x=(k*1.0/length*1.0)*datasize
     #   print x
        l=int(max([math.floor(x-length**0.5),0]))
        h=int(min([math.floor(x+length**0.5),datasize]))
      #  print  l,h
        if(l>=1):
            L=sort_R[l-1]
        else:
            L=sort_R[l]
        H=sort_R[h-1]
        Lp=get_rank(datalist,L)
        Lh=get_rank(datalist,H)
        P=[]
        for i in datalist:
            if i>=L and i<= H:
                P.append(i)
        if  k>=Lp and k<= Lh  and len(P)<=(4*datasize+1):
            P.sort()
            return  P[k-Lp]
        #return None




if __name__ == "__main__":
   # datasize_list = [1000, 2000, 5000, 10000, 20000, 50000, 100000]
    # 从列表中随机选择一个数据集大小
  #  datasize = random.choice(datasize_list)
    # 随机生成datasize个范围再(0,1000000)的数
    datasize=50000
    datalist = brand.get_many_data(datasize, 0, 1000000)
    # print  datalist[0:30]
    #k=input('请输入k值:(k<%d)'%datasize)
    k=10
  #  cishu=0
  #  sum=0
    #for  i  in range(1):
    start = time.time()
    m = lazy_select(datalist, 0, datasize - 1, k)
    #if m != None:
    end=time.time()
    print m
       # cishu+=1
    thistime=(end-start)*1000
    #    sum+=thistime
        ##用于验证正确
        #datalist.sort()
        #print datalist[0:30]
   # avgtime=sum/1

    print  "第一次运行算法可以得到K位小的次数和运行一次算法的平均时间：%s"  %(thistime)






