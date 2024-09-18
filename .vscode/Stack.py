class SqStack:
    def __init__(self):
        self.data = []

    def empty(self):
        if len(self.data) == 0:
            temp = True
        else:
            temp = False
        return temp

    def push(self, e):
        self.data.append(e)

    def pop(self):
        '''not是python中的逻辑非，当栈非空，empty为False,
           有not变其为True，因此断言满足'''
        assert not self.empty()
        return self.data.pop() 

    def gettop(self):
        assert not self.empty()
        return self.data[-1]

    def DestroyStack(self):
        del self.data

class StackNode:
    def __init__(self,data):
        self.data = data
        self.next = None

class StackLink(self):
    def __init__(self):
        self._head = StackLink(None)

    def empty(self):
        if self._head.next is None:
            temp = True
        else:
            temp = False
        return temp

    def push(self,data):
        p = StackNode(data)
        p.next = self._head
        self._head = p

    def pop(self):
        assert not empty()
        e = self._head.data
        p = self._head
        self._head = self._head.next
        del p
        return e
    
    def gettop(self):
        assert not empty()
        return self._head.data