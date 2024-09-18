'''顺序存储，速度快,中间有浪费空间，更适合完全二叉树和满二叉树'''
MaxSize = 100
sq_bitree = []*MaxSize

'''链式存储'''
'''在这里我们需要搞清楚一个内容，如果t原先是BTNode类型,然后t=None
   此时t为None类型，就不能再使用t,data了！不过，t=BTNone(None)
   仍然是BTNone类型'''
'''print语句默认以反斜杠n结尾，则输出后会自动换行，我们可以用
   peint(a,end='输出结尾内容，如空格，逗号，什么也没有也可以')'''
'''一次只读入一个字符的方法：
   import sys
   sys.stdin.read(1)
   //从标准输入流中读入一个字符''' 
class BTNode:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None
'''各遍历算法'''       
def pre_order_traverse(t):
    if t is not None:
        print(t.data,end=',')
        pre_order_traverse(t.lchild)
        pre_order_traverse(t.rchild)

def in_order_traverse(t):
    if t is not None:
        in_order_traverse(t.lchild)
        print(t.data,end=',')
        in_order_traverse(t.rchild)

def post_order_traverse(t):
    if t is not None:
        post_order_traverse(t.lchild)
        post_order_traverse(t.rchild)
        print(t.data,end=',')

MaxSize = 100
class Queue:
    def __init__(self):
        self.data = []*MaxSize
        self.front = 0
        self.rear = 0

    def push(self, e):
        self.data[self.rear] = e
        self.rear = (self.rear+1)%(MaxSize+1)

    def pop(self):
        f = self.front
        self.front = (f+1)%(MaxSize+1)
        return self.data[f]

def level_order(t):
    q = Queue()
    q.push(t)
    while (q.front != q.rear):
        p = q.pop()
        print(p,end=',')
        if p.lchild is not None:
            q.push(p.lchild)
        elif p.rchild is not None:
            q.push(p.rchild)

'''遍历算法的应用'''
import sys
def creat_bitree():    
    ch = sys.stdin.read(1)
    if ch == ' ':
        t = None
    else:
        t = BTNode(ch)
        t.lchild = creat_bitree()
        t.rchild = creat_bitree()
    return t

def copy(t):
    if t is not None:
        n = BTNode(t.data)
        n.lchild = copy(t.lchild)
        n.rchild = copy(t.rchild)
    else:
        n = None
    return n

def depth(t):
    if t is None:
        return 0
    else:
        m = depth(t.lchild)
        n = depth(t.rchild)
        if m >= n:
            return m+1
        else:
            return n+1 

def node_count(t):
    if t is None:
        return 0
    else:
        return node_count(t.lchild)+node_count(t.rchild)+1

def lead_count(t):
    if t is None:
        return 0
    else:
        if t.lchild is None and t.rchild is None:
            return 1
        else:
            return lead_count(t.lchild)+lead_count(t.rchild)

t = creat_bitree()
n = copy(t)
print(depth(n))
print(node_count(n))
print(lead_count(n))