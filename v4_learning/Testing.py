# tarverse a binary tree in level order using list
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
  def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.PrintTree()
print("Level order traversal of binary tree is -")
def printLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printGivenLevel(root, i)
def printGivenLevel(root , level):
    if root is None:
        return
    if level == 1:
        print(root.data),
    elif level > 1 :
        printGivenLevel(root.left , level-1)
        printGivenLevel(root.right , level-1)
def height(node):
    if node is None:
        return 0
    else :
        lheight = height(node.left)
        rheight = height(node.right)
        if lheight > rheight :
            return lheight+1
        else:
            return rheight+1
printLevelOrder(root)

#unit test for the above code
import unittest

