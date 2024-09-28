'''邻接矩阵法'''
MVNum = 100
MaxInt = 32767 #表示无穷(极大值)
class Gragh1:
    def __init__(self):
        self.vertex = [ ]*MVNum
        #标准的二维数组创建，后面可以用numpy
        self.arc = [[0 for i in range(MVNum)] for j in range(MVNum)]
        self.vexnum = 0
        self.arcnum = 0

    def locate_vex(self, v):
        for i in range(vexnum):
            if v == self.vextex[i]:
                return i

'''创建无向网'''
def creat_UDN(g):
    g.vexnum = input('请输入顶点数：')
    g.arcnum = input('请输入弧数：')
    for i in range(g.vexnum):
        g.vertex = input('请输入顶点：')
    for j in range(g.vexnum):
        for k in range(g.vexnum):
            g.arc[j][k] = MaxInt
    for k in range(arcnum):
        w = input('请输入弧的权值：')
        v1 = input('请输入弧依附的第一个点：')
        v2 = input('请输入弧依附的第二个点：')
        i = g.locate_vex(v1)
        j = g.locate_vex(v2)
        g.arc[i][j] = g.arc[j][i] = w

'''衔接表法(更常用)'''
'''关于字典：字典内的item为key:value,遍历的时候可以分别单独遍历
   items(),keys(),values().
   字典的key如果是字符要加上引号！'''
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connect_to = {}
        self.predecessor = None
        self.color = 'white'
        self.distance = 0

    def add_neighber(self,nbr,weight):
        self.connect_to[nbr] = weight

    def get_connections(self):
        return self.connect_to.keys()

    def set_pred(self,vertex):
        self.predecessor = vertex.id
    
    def get_id(self):
        return self.id

    def get_weight(self,nbr):
        return self.connect_to[nbr]

    def set_color(self,color):
        self.color = color

    def get_color(self):
        #print('?',self.color)
        return self.color

    def __str__(self):
        '''格式化输出的写法，注意学习'''
        return str(self.id)+'connect_to'+str([x for x in self.connect_to])

#vertices是vertex的复数形式
class Gragh:
    def __init__(self):
        self.ver_list = {}
        self.vertices_num = 0

    def add_vertex(self,key):
        self.vertices_num += 1
        newver = Vertex(key)
        self.ver_list[key] = newver
        #print(key)
        #print(self.ver_list[key])
        return newver

    def get_verex(self,n):
        if n in self.ver_list:
            return self.ver_list[n]
        else:
            return None

    def add_edge(self,f,t,w=0):
        #print('f=',f)
        #print('t=',t)
        if f not in self.ver_list:
            nv = self.add_vertex(f)
            #print('一')
        if t not in self.ver_list:
            nv = self.add_vertex(t)
            #print('二')
        #print(self.ver_list[17])
        self.ver_list[f].add_neighber(self.ver_list[t].id,w)

    def get_vertices(self):
        return self.ver_list.keys()

#test
'''
g = Gragh()
for i in range(6):
    g.add_vertex(i)
g.add_edge(0,1,5)
g.add_edge(0,5,2)
g.add_edge(1,2,4)
g.add_edge(2,3,9)
g.add_edge(3,4,7)
g.add_edge(3,5,3)
g.add_edge(4,0,1)
g.add_edge(5,4,8)
g.add_edge(5,2,1)

for x in g.ver_list.values():
    for y in x.connect_to:
        print('('+str(x.id)+','+str(y.id)+')')
'''


