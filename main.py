#showing binary tree from left to right
import random

SIZE = 20

class Node():

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def add(self, val):
        if val < self.val:
            if self.left:
                self.left.add(val)
            else:
                self.left = Node(val)
        elif val > self.val:
            if self.right:
                self.right.add(val)
            else:
                self.right = Node(val)
        else: # val == self.val
            pass

    def print(self, depth = 0):
        if self.left:
            self.left.print(depth = depth + 1)
        print('%s%s' %('    '*depth, str(self.val)))

        if self.right:
            self.right.print(depth = depth + 1)
            
class Tree:
    def __init__(self):
        self.root = None

    def append(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            self.root.add(val)
    def print(self):
        self.root.print()

t = Tree()

lst = list()

lst = list(range(1, SIZE+1))
random.shuffle(lst)
print(lst)
for i in lst:
    t.append(i)
    
t.append(3)

t.print()
