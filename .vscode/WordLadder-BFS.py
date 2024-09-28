from Gragh import Gragh,Vertex

'''创建单词图'''
def build_gragh(WordFile):
    g = Gragh()
    d ={}
    wfile = open(WordFile,'r')
    for line in wfile:
        word = line[:]
        for i in range(len(word)):
            '''这里有一个有趣的现象,a[len(a)]是不行的，而
               a[len(a):]输出为[]'''
            bucket = word[:i]+'_'+word[i+1:]
            if bucket in d:
                bucket.append(word)
            else:
                d[bucket] = word
    for bucket in d.values():
        for word1 in bucket:
            for word2 in bucket:
                if word1 != word2:
                    g.add_edge(word1, word2)
    return g

'''BFS'''
MaxSize = 100
class Queue:
    def __init__(self):
        self.data = []
        self.front = 0
        self.rear = 0
    
    def size(self):
        return (self.rear-self.front)%MaxSize

    def enqueue(self,data):
        self.data[rear] = data
        self.rear = (self.rear+1)%MaxSize

    def dequeue(self):
        data = self.data[self.front]
        del self.data[self.front]
        self.front = (self.front+1)%MaxSize
        return data

def dfs(g,start):
    ver_q = Queue()
    ver_q.enqueue(start)
    while ver_q.size() > 0:
        cur_v = ver_q.dequeue()
        cur_v.set_color('gray')
        for v in cur_v.get_connections:
            if g.ver_list[v].color == 'white':
                g.ver_list[v].set_color('gray')
                g.ver_list[v].predecessor = cur_v
                g.ver_list[v].distance = cur_v.distance+1
                enqueue(g.ver_list[v])
        cur_v.set_color('black')
    
