from models.node import Node

class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value, angle):
        new_node = Node(value, angle)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node

    def get_node(self, value):
        if not self.head:
            return None
        curr = self.head
        while True:
            if curr.value == value:
                return curr
            curr = curr.next
            if curr == self.head:
                break
        return None
