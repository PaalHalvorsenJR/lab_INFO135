class Node: 
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

def add(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        
        last_node.next = new_node
       

node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)

node1.next = Node2
Node2.next = Node3





