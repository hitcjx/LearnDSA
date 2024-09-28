'''树的双亲孩子表示法'''
'''使用时创建一个列表储存PTNode'''
class PTNode:
    def __init__(self,data):
        self.data = data
        self.parent = 0
        '''child列表储存所有孩子结点的下标'''
        self.child = []

'''孩子兄弟表示法'''
'''此处的child是指第一个孩子'''
class CBNode:
    def __init__(self,data):
        self.data = data
        self.child = None
        self.bro = None





