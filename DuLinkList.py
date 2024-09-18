class DuLNode:
    def __init__(self, item):
        self.item = item
        self.prior = None
        self.next = None

class DuLinkList:
    def __init__(self):
        self._head = DuLNode(None)
    
    def list_lenth_DuL(self):
        p = self._head
        i = 0
        while p.next is not None:
            p = p.next
            i += 1
        return i
    
    def list_insert_DuL(self, i, e):
        if i > list_lenth_DuL():
            print('Error!')
            return 0
        p = self._head
        for j in range(i):
            p = p.next
        s = Node(e)
        s.prior = p.prior
        p.prior.next = s
        s.next = p
        p.prior = s
        '''不要忘记，我们实际上需要四条连线'''

    def list_delete_DuL(self, i):
        if i > list_lenth_DuL():
            print('Error!')
            return 0
        p = self._head
        for j in range(i):
            p = p.next
        p.next.prior = p.prior
        p.prior.next = p.next
        