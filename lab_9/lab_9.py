#Exercise 1


#PreOrder

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
    
    #A function to do inorder tree traversal
    
def printPreOrder(root):
    if root:
        print(root.val, end = " ")
        printPreOrder(root.left)
        printPreOrder(root.right)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
 
    # Function call
    print("Prenorder traversal of binary tree is")
    printPreOrder(root)
    print("\n")

#InOrder
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
    
    #A function to do inorder tree traversal
    
def printInOrder(root):
    if root:
        printInOrder(root.left)
        print(root.val, end = " ")
        printInOrder(root.right)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
 
    # Function call
    print("Inorder traversal of binary tree is")
    printInOrder(root)
    print("\n")

# Post Order

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
    
    #A function to do inorder tree traversal
    
def printPostOrder(root):
    if root:
        printPostOrder(root.left)
        printPostOrder(root.right)
        print(root.val, end = " ")


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
 
    # Function call
    print("Postenorder traversal of binary tree is")
    printPreOrder(root)

"""
PreOrder: When we find the nodes in in PreOrder, we follow the nodes
from the first Node and then go down to the left side until we are on
the last child node. 
"""




    

    


    
