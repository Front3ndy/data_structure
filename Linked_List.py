class LinkedList:
    head = None

    class Node:
        element = None
        next_node = None

        def __init__(self, element, next_node=None):
            self.element = element
            self.next_node = next_node

    def append(self, element):
        if self.head is None:
            self.head = self.Node(element)
            return element

        curr = self.head

        while curr.next_node:
            curr = curr.next_node

        curr.next_node = self.Node(element)

    def insert(self, index, element):
        i = 0
        node = self.head
        prev_node = self.head

        while i < index and node.next_node:
            prev_node = node
            node = node.next_node
            i += 1
        prev_node.next_node = self.Node(element, node)

        return element

    def delete(self, index):
        i = 0
        node = self.head
        prev_node = self.head

        while i < index and node.next_node:
            prev_node = node
            node = node.next_node
            i += 1
        prev_node.next_node = node.next_node

    def get(self, index):
        i = 0
        node = self.head
        prev_node = self.head

        while i < index and node.next_node:
            prev_node = node
            node = node.next_node
            i += 1
        return prev_node.next_node.element

    def show_list(self):
        while self.head.next_node:
            print(self.head.element)
            self.head = self.head.next_node
        print(self.head.element)



if __name__ == '__main__':
    l = LinkedList()
    l.append(3)
    l.append(4)
    l.append(6)
    l.append(10)
    l.append(8)
    print(l.get(3))