class SqString:
    def __init__(self):
        self.MaxStringSize = 256
        self.chars = ""
        self.lenth = 0

    def creat_string(self):
        string = input()
        self.lenth = len(string)
        if self.lenth > 256:
            print('Overflow!')
        else:
            self.chars = string

s1 = SqString()
s2 = SqString()
s1.creat_string()
s2.creat_string()

def index_BF(s1, s2):
    assert s1.lenth >= s2.lenth
    for i in range(s1.lenth-s2.lenth):
        for j in range(s2.lenth):
            if s2.chars[j] == s1.chars[i+j]:
                j += 1
            else:
                break
        if j == s2.lenth:
            return i
        else:
            i += 1
    return 'Can\'t find!'

'''kmp算法'''
def get_next(s2):
    next = []*len(s2)
    next[0] = -1
    i = 0
    j = -1
    while i < len(s2)-1:
        if s2.chars[i] == s2.chars[j] or j == -1:
            i += 1
            j += 1
            next[i] = j
        else:
            j = next[j]

def index_KMP(s1, s2):
    assert s1.lenth >= s2.lenth
    p = -1
    i = -1
    while p < s1.lenth and i < s2.lenth:
        if s1.chars[p] == s2.chars[i] or i == -1:
            p += 1
            i += 1
        else:
            i = next[i]
    if i == s2.lenth:
        return p-s2.lenth
    else:
        return 'Can\'t find!'



