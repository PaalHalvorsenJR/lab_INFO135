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

    def add_at_beginning(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


linked_list = LinkedList()
linked_list.add(1)
linked_list.add(2)
linked_list.add(3)
linked_list.add(4)
linked_list.add_at_beginning(0)


print(linked_list.head.data)
print(linked_list.head.next.data)
print(linked_list.head.next.next.data)
print(linked_list.head.next.next.next.data)





    

        

         

