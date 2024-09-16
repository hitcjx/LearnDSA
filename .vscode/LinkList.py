'''python中的变量实际上都是指向数据的一个引用，
   当没有引用指向数据时，该数据自动被删除'''

class Node:
    def __init__(self,item):
        self.item = item
        self.next = None

class LinkList:
    def __init__(self):
        self._head = Node(None)

    def IsEmpty(self):
        return self._head.next is None

    def DestroyList(self):
        while IsEmpty() == False:
            p = self._head
            self._head = self._head.next
            del p

    def ClearList(self):
        p = self._head.next
        self._head.next = None
        while p is not None:
            q = p.next
            del p
            p = q

    def ListLenth(self):
        p = self._head
        i = 0
        while p.next is not None:
            i += 1
            p = p.next
        return i

    def GetElem (self, i):
        p = self._head
        if i > ListLenth():
            print('Error!')
            r = 0
        else:
            for j in range(i):
                p = p.next
            r = p.item
        return r

    def LocateElem(self, e):
        p = self._head.next
        i = 1
        while p is not None and p.item != e:
            p = p.next
            i += 1
        if p is None:
            print('Can\'t find!')
        else:
            return i
    
    def ListInsert(self, i, e):
        if i > ListLenth():
            print('Error!')
            return 0
        p = self._head
        for j in range(0,i):
            p = p.next
        s = Node(e)
        s.next = p.next
        p.next = s

    def ListDelete(self, i):
        if i > ListLenth():
            print('Error!')
            return 0
        p = self._head
        for j in range(0, i):
            p = p.next
        q = p.next
        p.next = q.next
        del q

    def CreatList_H(self, len):
        for i in range(len):
            item = input()
            h = Node(item)
            h.next = self._head.next
            self._head.next = h
        
    def CreatList_R(self, len):
        r = self._head
        for i in range(len):
            item = input()
            p = Node(item)
            r.next = p
            r = p
        

link_list = LinkList()