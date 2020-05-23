class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node('head')

    def add(self, element, index = -1):
        if index == -1:
            node = self.head
            while node.next != None:
                node = node.next
            node.next = Node(element)
        else:
            new_element = Node(element)
            node = self.head
            for i in range(index):
                node = node.next
            prev = node.next
            node.next = new_element
            new_element.next = prev

    def remove(self, index = -1):
        if index == -1:
            node = self.head
            while node.next.next != None:
                node = node.next
            node.next = None
        else:
            node = self.head
            for i in range(index):
                node = node.next
            node.next = node.next.next

    def __str__(self):
        result = []
        node = self.head
        while node.next != None:
            node = node.next
            result.append(str(node.data))
        return ', '.join(result)
