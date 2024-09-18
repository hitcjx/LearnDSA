class Node:
    def __init__(self,item):
        self.item = item
        self.next = None

class SingleCircleList:
    def __init__(self):
        self._head = Node(None)

    def creat_list_R(self, len):
        '''尾插法创建带尾指针的循环链表'''
        r = self._head
        for i in range(len):
            item = input()
            p = Node(item)
            p = r.next
            r = p
        r.next = self._head
        return r

def connect(r1,r2):
    p = r1.next
    r1.next = r2.next.next
    del r2.next
    r2.next = p
    return r2