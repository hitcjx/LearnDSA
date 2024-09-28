'''值得注意的是，self.weight默认为char型，要手动化为int'''
class HTNode:
    def __init__(self,weight):
        self.weight = int(weight)
        self.parent = 0
        self.lch = 0
        self.rch = 0

def creat_Haffman_tree(n):
    '''初始化'''
    ht = [None]*n*2
    ht[0] = 0
    for i in range(n):
        weight = input('请输入权重：')
        ht[i+1] = HTNode(weight) 
    
    '''构造'''
    for j in range(1,n):
        k = 2
        a = [0]*2
        w = 0
        for l in range(2):
            while ht[k]:
                if ht[k].parent == 0:
                    if ht[k].weight <= ht[k-1].weight:
                        a[l] = k
                    else:
                        a[l] = k-1
                k += 1
            if a[l] != 0:
                ht[a[l]].parent = n+j
                w += ht[a[l]].weight

        ht[n+j] = HTNode(w)
        ht[n+j].lch = a[0]
        ht[n+j].rch = a[1]

    return ht

ht1 = creat_Haffman_tree(3)   
for i in range(1,4):
    print(ht1[i].weight)