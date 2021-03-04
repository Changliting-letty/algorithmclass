# -*- coding:utf-8 -*-

import math
import time
import sys
#from PointOpration import Chessbord
from PointOpration import Point
import  drow as drow
"""
构造
"""

#计算点的G值
def comu_G(parent,son):
    #移动代价
    if (abs(son.x-parent.x)+abs(son.y-parent.y)==1):
        yidong=10
    else:
        yidong=14
    #地形代价
    if(son.isdesert==1):
        dixing=4
    elif(son.isriver==1):
        dixing=2
    else:
        dixing=0
    #print parent.G,yidong,dixing
    return round(parent.G+yidong+dixing,2)
#用曼哈顿距离
def comu_H(thispoint,end_point):

    return abs(end_point.x-thispoint.x)+abs(end_point.y-thispoint.y)


def comu_F(thispoint):

    return thispoint.G+thispoint.H


#判断点是否在二维列表中

def isinlist(thispoint,twodlist):
    for list in twodlist:
        for point in  list :
            if point.x==thispoint.x and point.y==thispoint.y:
                return True
    return  False


#找到列表中F值最小的点 O（n）
def get_smallest_F(point_list):
    point=point_list[0]
    for i in range(1,len(point_list)):
        if point.F > point_list[i].F:
            point=point_list[i]

    return  point  #返回F值最小的点

def isinonelist(thisp,point_list):
    for point in point_list:
        if point.x==thisp.x and  point.y ==thisp.y:
            return  True
    else:
        return False
def get_son_list(current,deathlist,point_list):
    #当前节点四周八个点 是否可达以及不在死结点表中
    sonlist=[]
    for x in range(current.x-1,current.x+2):
        for  y in range(current.y-1,current.y+2):
            if(current.canreach(x,y,point_list) and( not isinonelist(point_list[x][y],deathlist))):
                sonlist.append(point_list[x][y])
  #  print(len(sonlist))
    return  sonlist


def  single_findpath(point_list,start_point,end_point):
    live_list=[]  #活结点表
    death_list=[]  #死节点表
    live_list.append(start_point)  #将起始节点装入活结点表
    while(len(live_list) != 0):
        current=get_smallest_F(live_list)

        print("(",current.x,current.y,")","F:",current.F,"G:",current.G,"H:",current.H)
        live_list.remove(current)   #从活结点表中删除
        death_list.append(current)  #并且加入到死节点表
        son_list=get_son_list(current,death_list,point_list)
        #遍历儿子节点，如果不在表中，便极端F,G,H值并且加入活结点表中
        #如果在表中看从当前节点走到该点是否更好，通过G值判断这个点是否更近 更好便修改该点的parent属性。
       # if current.x==8 and current.y==27:
        #    for son in son_list:
         #       print "问题所在"
          #      print son.x,son.y
        for son in son_list:
            if (isinonelist(son,death_list)):
                continue
            if(not isinonelist(son,live_list)):
                son.parent=current
                son.G=comu_G(current,son)
                son.H=comu_H(son,end_point)
                son.F=comu_F(son)
                live_list.append(son)
            else:
                if son.x==current.x or son.y==current.y:
                     new_G = current.G+10+son.isdesert+son.isriver
                else:
                    new_G=current.G+ 14+son.isdesert+son.isriver
                if new_G < son.G:
                    son.parent=current
                    son.G = comu_G(current, son)
                    son.H = comu_H(son, end_point)
                    son.F = comu_F(son)
            if (isinonelist(end_point, live_list)):
                return end_point


    return  None

def double_findpath(point_list,start_point,end_point):
    live_list1=[]  #从前开始的活结点表
    live_list2=[]   #从后开始的活结点表
    death_list1=[]  #从前开始的死结点表
    death_list2=[]  #从后开始的死节点表
    live_list1.append(start_point)  # 将起始节点装入活结点表
    live_list2.append(end_point)  # 将起始节点装入活结点表
    while(len(live_list1)!=0 and len(live_list2)!=0):
        current1= get_smallest_F(live_list1)
        current2=get_smallest_F(live_list2)
        print("forward(",current1.x, current1.y,")"," F:",current1.F ," G:", current1.G, "H:", current1.H)
        print("behind(", current2.x, current2.y ,")" ," F:" , current2.F , " G:" ,current2.G , "H:", current2.H)
        live_list1.remove(current1)  # 从活结点表中删除
        live_list2.remove(current2)
        death_list1.append(current1)  # 并且加入到死节点表
        death_list2.insert(0,current2)
        son_list1 = get_son_list(current1, death_list1, point_list)
        son_list2 = get_son_list(current2, death_list2, point_list)
        # 遍历儿子节点，如果不在表中，便极端F,G,H值并且加入活结点表中
        # 如果在表中看从当前节点走到该点是否更好，通过G值判断这个点是否更近 更好便修改该点的parent属性。
        for son in son_list1:
            if (isinonelist(son, death_list1)):
                continue
            if (not isinonelist(son, live_list1)):
                son.parent = current1
                son.G = comu_G(current1, son)
                son.H = comu_H(son, end_point)
                son.F = comu_F(son)
                live_list1.append(son)
            else:
                if son.x == current1.x or son.y == current1.y:
                    new_G = current1.G + 10
                else:
                    new_G = current1.G + 14
                if new_G < son.G:
                    son.parent = current1
                    son.G = comu_G(current1, son)
                    son.H = comu_H(son,end_point)
                    son.F = comu_F(son)
            for son2 in son_list2:
                if (isinonelist(son2, death_list2)):
                    continue
                if (not isinonelist(son2, live_list2)):
                      #如果这个点已经在第1个活节点表中，z #判断前后两条路径，是否存在一个点即在前边活结表中也在后边活结点表中。此时便找到了一条路径
                    if(isinonelist(son2,live_list1)):
                        #print  son2.x,son2.y,current2.x,current2.y,current2.parent.x,current2.parent.y
                        return son2,current2
                    son2.parent=current2
                    son2.G = comu_G(current2, son2)
                    son2.H = comu_H(son2, start_point)
                    son2.F = comu_F(son2)
                    live_list2.append(son2)

                else:
                    if son2.x == current2.x or son2.y == current2.y:
                        new2_G = current2.G + 10
                    else:
                        new2_G = current2.G + 14
                    if new2_G < son2.G:
                        son2.parent = current2
                        son2.G = comu_G(current2, son2)
                        son2.H = comu_H(son2, start_point)
                        son2.F = comu_F(son2)






    print"找不到这样一条双向路径"
    return None,None



#找单向路径
def get_path(endpoint):
    path=[]
    while(endpoint != None):
        path.insert(0,endpoint)
        endpoint=endpoint.parent
    return path

#找双向路径
def get_doublepath(m1,m2):
    path=[]
    path1=[]
    path2=[]
    while(m1!=None) :#
        path1.insert(0,m1)
        m1=m1.parent

    while(m2!=None):
        path2.append(m2)
        m2=m2.parent

    path.extend(path1)
    path.extend(path2)

    return  path,path1,path2





if __name__ == "__main__":
    while(True):
        filecode = input("输入0使用小数据集，输入1使用大数据集:")
        if filecode == 0:
            filename = "./data/chessform1"  # 文件路径
            break
        elif filecode==1:
            filename = "./data/chessform2"  # 文件路径
            break
        else:
            print("输入错误，请重新输入")
    file_read = open(filename, 'r')
    content = file_read.readlines()
    row_cal = content[0].strip().split(',')
    row = int(row_cal[0])
    col = int(row_cal[1])
    start = content[1].strip().split(',')
    start[0] = int(start[0])
    start[1] = int(start[1])
    end = content[2].strip().split(',')
    end[0] = int(end[0])
    end[1] = int(end[1])
    data=[] # 大数据集
    for i in range(3,len(content)):
       # print content[i].strip().split(" ")
        data.append(content[i].strip().split(" "))
   # print big
   #构造点
    point_list = []

    start_point = Point(start[0], start[1])
    start_point.isbegin = 1

    end_point = Point(end[0], end[1])
    end_point.isend = 1
    for i in range(0, row):
        point_list.append([])
        for j in range(0, col):
            if i == start[0] and j == start[1]:
                start_point.color="red"
                point_list[i].append(start_point)
                continue
            if i == end[0] and j == end[1]:
                end_point.color="red"
                point_list[i].append(end_point)
                continue
            point = Point(i, j)
            if  data[i][j]  == '1':
                point.isbarrier=1
                point.color='grey'
            elif data[i][j] == '4':
                point.isdesert=1
                point.color='yellow'
            elif data[i][j]=='2':
                point.isriver=1
                point.color="blue"
            point_list[i].append(point)

    while(True):
        code = input('单向A*输入0，双向A*输入1：')
        if (code == 0):
            print "正在执行单向搜索：..."
            end_result = single_findpath(point_list, start_point, end_point)  # 返回带前驱元素的终点
            single_path = get_path(end_result)
            ##从头到尾打印路径，打印坐标
            print "单向搜索路径为："
            for i in single_path:
                i.color="green"
                point_list[i.x][i.y].color="green"
                print "(" + str(i.x) + " ," + str(i.y) + ")"
            drow.draw_chess(point_list,"single_path")
            break

        elif (code == 1):
            # 双向搜索
            print "正在执行双向搜索：..."
            p1, p2 = double_findpath(point_list, start_point, end_point)
            path,path1,path2 = get_doublepath(p1, p2)

            print "双向搜索路径为："
            for i in path1:
                i.color = "pink"
                point_list[i.x][i.y].color = "pink"
                print "(" + str(i.x) + " ," + str(i.y) + ")"
            for i in path2:
                i.color = "purple"
                point_list[i.x][i.y].color = "purple"
                print "(" + str(i.x) + " ," + str(i.y) + ")"
            drow.draw_chess(point_list, "double_path")
            break
        else:
            print "输入错误，请重新输入"







"""
if __name__ == "__main__":
     filecode=input("输入0使用小数据集，输入1使用大数据集")
     if  filecode==0:
        filename = "./data/chessform1"  # 文件路径
     else:
         filename = "./data/chessform2"  # 文件路径
     file_read=open(filename,'r')
     content=file_read.readlines()
     row_cal=content[0].strip().split(',')
     row=int(row_cal[0])
     col=int(row_cal[1])
     start=content[1].strip().split(',')
     start[0]=int(start[0])
     start[1]=int(start[1])
     end=content[2].strip().split(',')
     end[0] = int(end[0])
     end[1] = int(end[1])
     barri_list_str = content[3].strip().split(" ")  #相同道理，这里可以再加沙漠和河流的坐标列表
     barri_list=[]
     for i in barri_list_str:
         barri_list.append(eval(i))

     point_list=[]

     start_point=Point(start[0],start[1])
     start_point.isbegin=1
     end_point=Point(end[0],end[1])
     end_point.isend=1
     for i in range(0,row):
        point_list.append([])
        for j in range(0,col):
            if i== start[0] and  j== start[1]:
                point_list[i].append(start_point)
                continue
            if i==end[0]  and  j==end[1] :
                point_list[i].append(end_point)
                continue
            point = Point(i, j)
            if (i,j) in barri_list:
                point.isbarrier=1
                #print("这是障碍点")
            point_list[i].append(point)

    #让用户选择是单向还是双向：
     code = input('单向A*输入0，双向A*输入1：')
     if(code == 0):
        print "正在执行单向搜索：..."
        end_result = single_findpath(point_list, start_point, end_point)  # 返回带前驱元素的终点
        single_path=get_path(end_result)
         ##从头到尾打印路径，打印坐标
        print "单向搜索路径为："
        for i in single_path:
            print "("+ str(i.x) +" ," + str(i.y) +")"
     elif(code==1):
     #双向搜索
         print "正在执行双向搜索：..."
         p1,p2=double_findpath(point_list, start_point, end_point)
         double_path=get_doublepath(p1,p2)
         print "双向搜索路径为："
         for i in double_path:
             print "("+ str(i.x) +" ," + str(i.y) +")"
     else:
         print "输入错误，请重新执行"

"""









