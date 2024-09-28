from Gragh import Gragh,Vertex

'''创建骑士路线图'''
def knight_gragh(bdsize):
    kt_gragh = Gragh()
    '''遍历棋盘,col:column,列'''
    for col in range(bdsize):
        for row in range(bdsize):
            nodeid = pos_to_nodeid(col,row,bdsize)
            #if nodeid > 0:
            #    print(kt_gragh.ver_list[nodeid-1].connect_to)
            #print('node=',nodeid)
            #if nodeid > 0:
            #    print(kt_gragh.ver_list[nodeid-1].connect_to)
            new_pos = gen_legal_moves(col,row,bdsize)
            for elem in new_pos:
                #print(elem[0],elem[1])
                next_nid = pos_to_nodeid(elem[0],elem[1],bdsize)
                #print(next_nid)
                kt_gragh.add_edge(nodeid,next_nid,0)
            #print('node=',nodeid,'connect to',kt_gragh.ver_list[nodeid].connect_to)
    
    #for i in range(64):
    #    print('node=',i,'connect to',kt_gragh.ver_list[i].connect_to.keys())

    return kt_gragh

def pos_to_nodeid(col,row,bdsize):
    return col*bdsize+row

def gen_legal_moves(col,row,bdsize):
    new_moves = []
    moves = [(2,1),(1,2),(-1,2),(-2,1),
            (-2,-1),(-1,-2),(1,-2),(2,-1)]
    for move in moves:
        y = move[0]+col
        x = move[1]+row
        if exam(x,y,bdsize):
            new_moves.append((y,x))
    return new_moves

def exam(a,b,bd):
    return a>=0 and a<bd and b >=0 and b< bd

kt_gragh = knight_gragh(8)
#print(kt_gragh.ver_list[0].connect_to)

'''骑士周游'''
def knight_tour(n,path,u,limit):
    #print(u.get_color())
    u.set_color('gray')
    path.append(u)
    if n < limit-1:
        #'list()函数将一个可迭代函数转化成列表'
        nbr_list = list(order_by_avail(u))
        #print('u=',u.id)
        #print('?',nbr_list)
        #print(kt_gragh.ver_list[nbr_list[0]].get_color())
        done = False
        i = 0
        while i < len(nbr_list) and not done:
            #print(nbr_list)
            #print(i)
            #print(i,len(nbr_list))
            #print('?')
            #print('color=',kt_gragh.ver_list[nbr_list[i]].get_color())
            if kt_gragh.ver_list[nbr_list[i]].get_color() == 'white':
                #print('??')
                #print(nbr_list[i])
                done = knight_tour(n+1,path,kt_gragh.ver_list[nbr_list[i]],limit)
            i = i+1
                #print(i)
        if not done:
            path.pop()
            u.set_color('white')
    else:
        done = True
    
    return done

'''list.sort()对列表从小到大进行排序，如果是字符串则按照字母
   list.sort(reverse=True)则可以从大到小'''
'''lambda表达式:
   lambda aguments:expression
   等价于
   def name(aguments):
        expression
'''
'''对元组列表排序可以用
   list.sort(key = lambda x:x[0])'''

def order_by_avail(node):
    re_list = []
    for e in node.get_connections():
        if kt_gragh.ver_list[e].get_color() == 'white':
            c = 0
            for elem in kt_gragh.ver_list[e].get_connections():
                if kt_gragh.ver_list[elem].get_color() == 'white':
                    c += 1
            re_list.append((c,e))
    re_list.sort(key = lambda x:x[0])
    return [y[1] for y in re_list]

path = []
u = kt_gragh.ver_list[0]
print(knight_tour(0,path,u,64))
#print('path=',path)
for i in range(64):
    if i%16==0 and i!=0:
        print()
    print(path[i].id,end='->')
