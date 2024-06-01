class Node: 
    def __init__(self,data):
        self.data = data
        self.next = None

node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)

node1.next = Node2
Node2.next = Node3

