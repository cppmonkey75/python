class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head=None
        self.tail=None
    
    def addNode(self, data):
        n  = Node(data)
        if self.tail:
            self.tail.next=n
        if not self.head:
            self.head=n
        self.tail=n 
    
    def deleteNode(self,key):
        if self.head is None:
            return
        if self.head.data==key:
            self.head=self.head.next
            return
        current_node = self.head.next
        prev=self.head
        while current_node:
            if current_node.data==key:
                prev.next=current_node.next
                return
            current_node=current_node.next
        return
    
    def display(self):
        current_node=self.head
        while current_node:
            if (current_node!=self.tail):
                print(current_node.data, end="=>")
            else:
                print(current_node.data)
            current_node=current_node.next

    
L=LinkedList()
L.addNode(1)
L.addNode(2)
L.addNode(3)
L.deleteNode(2)
L.deleteNode(1)
L.deleteNode(9)
L.addNode(4)
L.display()

        






