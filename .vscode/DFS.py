from Gragh import Gragh,Vertex

class DFSGragh(Gragh):
    def __init__(self):
        #继承Gragh的参数
        super.__init__()
        '''我们记录了时间，当我们将有向无环图的顶点从无前驱
           顶点开始遍历，按照遍历结束时间从小到大排序，就得到
           拓扑排序'''
        self.time = 0

    def dfs(self):
        for vertex in self.ver_list:
            vertex.set_color('white')
            vertex.set_pred = None
        
        for vertex in self.ver_list:
            if vertex.get_color() == 'white':
                self.dfs_visit(vertex)

    def dfs_visit(self,vertex):
        vertex.set_color('gray')
        time += 1
        for next in vertex.get_connections():
            if self.ver_list[next].get_color() == 'white':
                self.ver_list[next].set_pred = vertex
                dfs_visit(self.ver_list[next])
        vertex.set_color('black')
        time += 1
        
    
