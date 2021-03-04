# -*- coding: UTF-8 -*-

"""
使用枚举法解决凸包问题
解决思路：考虑Q中的任意四个点A、B、C、D，如果A处于BCD构成的三角形内部，那么A一定不属于凸包P的顶点集合
"""
import sys
import  src.randompoint  as  randompoint
import math
import  time

def isline(point1, point2, point3):  # 返回点的位置和点
    (x1, y1), (x2, y2), (x3, y3) = point1, point2, point3
    list = [point1, point2, point3]
    if ((y2 - y1) * (x3 - x1) - (y3 - y1) * (x2 - x1)) == 0:  # 在一条直线
        list.sort(key=lambda x: x[1])
        if list[1] == point1:
            #print(list[1])
            return 1, list[1]
        if list[1] == point2:
            return 2, list[1]
    else:
        return 0, list

def get_triangle_area(A,B,C):
    """
    :param A:
    :param B:
    :param C:
    :return 三角形ABC的面积:

    """

def  GetTrangleArea(x1,y1,x2,y2,x3,y3):

    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

def judge(A,B,C,D):

    ABC = GetTrangleArea(A[0], A[1], B[0], B[1], C[0], C[1])# 三角形ABC的面积
    DBC = GetTrangleArea(D[0], D[1],B[0], B[1], C[0], C[1])  # 三角形DBC的面积
    DAC = GetTrangleArea(A[0], A[1],D[0], D[1],  C[0], C[1])   # 三角形ADC的面积
    DAB = GetTrangleArea(A[0], A[1],D[0], D[1], B[0], B[1])  # 三角形ADB的面积

    return (ABC == DBC + DAC + DAB)

def get_dot_metrix(x,y):
    """
    输入两个二维向量，求点积
    """
    return  x[0]*y[0]+x[1]*y[1]

#这个方法总是出现除数为0的错误，不再使用
def  judge_old(A,B,C,D):
    """
       三角型三个顶点A,B,C；判断点D是否在三角形内部
       为重心法，和数学联系
       :return 如果在三角形ABC内 输出为TRUE

    """
    p0x=A[0]
    p0y=A[1]
    p1x=B[0]
    p1y=B[1]
    p2x=C[0]
    p2y=C[1]
    px=D[0]
    py=D[1]

    Area = 0.5 * (-p1y * p2x + p0y * (-p1x + p2x) + p0x * (p1y - p2y) + p1x * p2y);

    u = 1 / (2 * Area) * (p0y * p2x - p0x * p2y + (p2y - p0y) * px + (p0x - p2x) * py);
    v = 1 / (2 * Area) * (p0x * p1y - p0y * p1x + (p0y - p1y) * px + (p1x - p0x) * py);


    if(u>0 and v>0 and u+v<1):
        return True
    else:
        return  False
    '''
      v0 =(C[0]-A[0],C[1]-A[1])  #V0=C-A
    v1=(B[0]-A[0],B[1]-A[1])  #V1=B-A
    v2=(D[0]-A[0],D[1]-A[1])  #V2=D-A
    
    try:
        d11=get_dot_metrix(v1,v1)
        d00=get_dot_metrix(v0,v0)
        d12=get_dot_metrix(v1,v2)
        d01=get_dot_metrix(v0,v1)
        d02 = get_dot_metrix(v0,v2)

        #print  float(d00*d11-d01*d01)
        u1=1/float(d00*d11-d01*d01)
        u=(d11*d02-d01*d12)*u1
        v=(d00*d12-d01*d02)*u1
        if (u<0 or u>1 or v<0 or v>1):
            return  False;
        return  u+v < 1
    except ZeroDivisionError as e:
        print e

    '''






def  enumerate_method(point_list):
    if len(point_list)==3:   #如果多边形为三角形，那么三个点是凸包顶点
        return point_list
    else :
        #点按照纵坐标排序，y最小的点一定在凸包上
      #  print point_list
        point_list.sort(key=lambda x: (x[1],x[0]))
     #   print point_list;
        p0=point_list[0]  #p0是y值最小的点，一定在凸包上
      #  print p0
        point_list_left=point_list[1:] #所以只需考虑p0之外的点
        no_list=[]  #该集表示确定不是凸包上的点在point_list上的索引
        #三重循环找不在凸包内的点，判断逻辑 任选三个点和p0构成四个点，这里体现暴力
        # 如果A处于BCD构成的三角形内部，那么A一定不属于凸包P的顶点集合
        for i in range(0,len(point_list_left)-2):  #每次选择三个点和p0构成四个点，判断一个点是否在P0和另外两个点构成的三角行内
            pi=point_list_left[i]
            #判断点pi是否已经确定不在凸包上
            if i in no_list:
                continue
            for j in range(i+1,len(point_list_left)-1):
                 #同理，判断点p是否已经确定不在凸包上
                 pj=point_list_left[j]
                 if j in no_list:
                    continue
                 for k in range(j+1,len(point_list_left)):
                    pk=point_list_left[k]
                    #判断点pk是否已经确定不在凸包上
                    #判断pi是否在p0,pj,pk构成的三角形内
                    if k in no_list:
                        continue
                    is_pi=judge(p0,pj,pk,pi)
                    if  is_pi==True:
                        if i not in no_list:
                            no_list.append(i)
                    # 判断pj是否在p0,pi,pk构成的三角形内
                    is_pj = judge(p0, pi, pk, pj)
                    if is_pj == True:
                        if j not in no_list:

                            no_list.append(j)
                    # 判断pk是否在p0,pj,pi构成的三角形内
                    is_pk = judge(p0, pi, pj, pk)
                    if is_pk == True:
                        if k not  in no_list:

                            no_list.append(k)

        convex_hull=[]  #最终的凸包集合
      #  print no_list
      #  print len(no_list)

        for index,point in enumerate(point_list_left):
            if index not in no_list:
                convex_hull.append(point)
        #将之前的P0也加入到凸包集合
        convex_hull.append(p0)
        return  convex_hull



if  __name__=="__main__":

    #number=sys.argv[1]  #凸包问题的规模n
    start=time.time()
    number=1000
    point_list=randompoint.get_many_point(number,0,1000)
    #print point_list
    convex_hull=enumerate_method(point_list)  #暴力枚举法求凸包
    end=time.time()
    print convex_hull
    print end-start
    #x=judge((60.046948510299536, 13.688093088281816), (12.382829224375168, 24.590673279285657), (8.987933452247976, 44.290537359396374),
       #     (83.95757587288519, 44.74940195286518))
    #print x