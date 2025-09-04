# Implementing a linked list ADT 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):

        new_Node = Node(data)
        new_Node.next = self.head