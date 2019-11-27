class Node():
    def __init__(self,item):
        self.elem = item
        self.lchild = None
        self.rchild = None

class Tree():
    def __init__(self):
        self.root = None

    def add(self,item):
        node = Node(item)
        queue = 