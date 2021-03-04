# -*- coding:utf-8 -*-
import  random
import bigrandom as brand
import  divide_conquer as dc
import  time
import  lazyselect as ls


if __name__ == "__main__":
    #随机选择数据集合大小
        datasize_list=[1000,2000,5000,10000,20000,50000,100000]
    #从列表中随机选择一个数据集大小
    #datasize=random.choice(datasize_list)
    #随机生成datasize个范围再(0,1000000)的数
        methodcode = input('请选择method(0：分治法),(1:随机法)')
        k=100  #第100小的，后期改为变动
        if methodcode==0:
            timelist = []
            for datasize in datasize_list:
                datalist = brand.get_many_data(datasize, 0, 1000000)
                timesum = 0
                for i in range(1000):
                    start=time.time()
                    value=dc.divide_conquer(datalist,0,datasize-1,100)
                  #  print i,value
                    end=time.time()
                    thistime=end-start
                    timesum+=thistime
                avgtime=timesum/1000
                print "分治法求解数据量为%d第100小问题1000次的平均时间为：" %datasize, avgtime*1000
        if methodcode==1:
                timelist = []
                #k = input('请输入k值:(k<%d)' % datasize)
                for datasize in datasize_list:
                    datalist = brand.get_many_data(datasize, 0, 1000000)
                    timesum = 0
                    for i in range(2):
                        start = time.time()
                        value=ls.lazy_select(datalist, 0, datasize - 1, 100)
                        #  print i,value
                        end = time.time()
                        thistime = end - start
                        timesum += thistime
                        #if (value != None):
                         #   print "第%d次得到了结果,值为%d" %(i,value)
                          #  break
                    avgtime = timesum / 2

                    print "随机法求解数据量为%d的第100小问题1000次的平均时间为：" %datasize,avgtime*1000




