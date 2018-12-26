class Tree(object):
    def __init___(self):
        self.left = None
        self.right = None
        self.data = None

"""
root = Tree()
root.data = "root"
root.left = Tree()
root.left.data = "left"
root.right = Tree()
root.right.data = "right"
"""

class tree(object):
    def __init__(self, name='root', children=None):
        self.name=name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.name

    def add_child(self, node):
        assert isinstance(node, tree)
        self.children.append(node)
#    *
#   /|\
#  1 2 +
#     / \
#    3   4
        
t = tree('*', [tree('1'),
               tree('2'),
               tree('+', [tree('3'),
                          tree('4')])])



        
def numintegral(dwlimit, uplimit, funct):
        width = (uplimit-dwlimit)/100000
        return round(sum(list(map(lambda x: width * funct(dwlimit+x*width), range(100000)))), ndigits=5)

def C(n,k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k) # take advantage of symmetry
    c = 1
    for i in range(k):
        c = c * (n - i) / (i + 1)
    return c
