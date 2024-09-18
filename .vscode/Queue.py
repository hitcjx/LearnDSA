MaxSize = 100
class CSqQueue:
    def __init__(self):
        self.data = [None]*MaxSize
        self.front = 0
        self.rear = 0

    def empty(self):
        return self.front == self.rear

    def lenth(self):
        '''事实上，这东西比我原先想象的要复杂
           对于队列，其元素并不一定从[0]号位置开始
           在循环队列中，front实际位置不一定在rear之前
           注意代码如何解决这些问题'''
        return (self.rear-self.front+MaxSize)%MaxSize

    def push(self, e):
        assert (self.rear+1)%MaxSize != self.front
        self.rear = (self.rear+1)%MaxSize
        self.data[rear] = e

    def pop(self):
        assert self.rear != self.front
        e = self.data[self.front]
        self.front = (self.front+1)%MaxSize

    def get_head(self):
        assert self.rear != self.front
        return self.data[self.front]

class LinkNode:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkQueue:
    def __init__(self):
        self.front = LinkNode(None)
        self.rear = LinkNode(None)

    def destroy_LQ(self):
        while self.rear is not None:
            p = self.front
            self.front = self.front.next
            del p
    
    def push(self,e):
        p = linkNode(e)
        if self.front == self.rear:
            self.front = self.rear = p
        else:
            self.rear.next = p
            self.rear = p

    def pop(self):
        assert self.front.data is not None
        if self.front == self.rear:
            e = self.front.data
            self.front.data = None
        else:
            e = self.front.data
            self.front = self.front.next
        return e

    def get_head(self):
        assert self.front.data is not None
        return self.front.data

    
         
    
        