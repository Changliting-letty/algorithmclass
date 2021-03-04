# -*- coding: UTF-8 -*-


    #def  drow_original(self):



class Point(object):
    def __init__(self,x,y):
        self.x=x  #X坐标值
        self.y=y  #Y坐标值
        self.G=0  #从起点到此点的代价
        self.H=0  #从此点到重点估计代价
        self.F=0   # 从起点到终点，走此点
        self.geo_cost=0  #地形代价： 0为平地，4为沙漠，溪流为2
      #  self.color=0  # 0为白色， 1为黑色 ， 2为蓝色， 4为黄色  表示 平地、障碍物、溪流、沙漠
        self.parent=None  #记录该点的前驱节点，为列表中的索引值
       # seld.isvisited=0 #标记该点是否访问过，1为访问过
        self.isbegin=0 #标记是否是起点
        self.isend=0 #标记是否是终点
        self.isbarrier=0  #标记是否是障碍物说·
        self.isriver=0  #标记是否是河流
        self.isdesert=0  #标记是否是沙漠
        self.color='white'


    #返回X坐标值
    def get_x(self):
        return  self.x
    #返回y的坐标值
    def get_y(self):
        return  self.y
    #返回点的父节点索引

    def get_parent(self):
        return  self.parent

    #返回 地形信息
    def get_isbarrier(self):
        return  self.isbarrier

    #

    def get_isriver(self):

        return  self.isriver

    def get_isdesert(self):
        return  self.isdesert

  #  是否是起点

    def get_isbegin(self):
        return self.isbegin

    # 是否是终点
    def get_isend(self):
        return self.end

    #计算和返回地形代价
    def get_geocost(self):
        if self.isriver==1:
            self.geo_cost=2
        if self.isdesert==1:
            self.geo_cost=4
        return  self.geo_cost

    # 计算和返回G值
    def get_G(self):

        return self.G
    #计算并且返回H值
    def  get_H(self):

        return self.H


    #计算并且返回F值
    def get_F(self):
        return  self.G+self.H

    # 如果点与当前节点重合、超出地图、是障碍，返回false
    def canreach(self,x,y,pointlist):
        if (x < 0 or x > (len(pointlist)-1)  or y < 0 or y> (len(pointlist[1]) - 1) ) :
            return False;
       # print("超出",x,y,len(pointlist)-1)
        if(pointlist[x][y].isbarrier==1 or (x==self.x and y== self.y )):
            return  False
        return  True



"""
 def setG(self,G):
        self.G=G

    def setH(self,H):
        self.H=H

    def setF(self,F):
        self.F=F

    def setGeocost(self,geo_cost):
        self.geo_cost=geo_cost

    def setParent(self,parent):

        self.parent=parent

    def setIsbegin(self,isbegin):
        self.isbegin=isbegin

    def setIsend(self,isend):

        self.isend=isend

    def setIsreiver(self,isriver):
        self.isriver=isriver

    def setIsbarrier(self,isbarrier):
        self.isbarrier=isbarrier

    def setIsdesert(self,isdesert):
        self.isdesert=isdesert
        class  Chessbord(object):
    def __init__(self,row,col,barrier,desert=None,river=None,start,end,is_single=1,path1=None,path2=None):
        self.row=row
        self.col=col
        self.barrier=barrier #障碍物列表
        self.desert=desert  #沙漠列表
        self.river=river  #河流列表
        self.start=start #起点坐标
        self.end= end   #终点坐标
        self.issingle=is_single  #单向A *还是双向A*
        self.path1=path1  #单向的时候该路径就是最最终路径 ,双向时为左边一办路径    点对象列表类型
        self.path2=path2    #双向的时候的有值   点对象列表类型

"""



