

class DbList:

    class Node:
        prev_node = None
        next_node = None
        value = None

        def __init__(self, value, next_node, prev_node):
            self.value = value
            self.next_node = next_node
            self.prev_node = prev_node

    head = None
    tail = None
    length = 0

    def add(self, value):
        self.length += 1
        if not self.head:
            self.head = self.Node(value=value, next_node=None, prev_node=None)
            return value
        elif not self.tail:
            self.tail = self.Node(value=value, prev_node=self.head, next_node=None)
            self.head.next_node = self.tail
        else:
            self.tail = self.Node(value=value, next_node=None, prev_node=self.tail)
            self.tail.prev_node.next_node = self.tail
            return value

    def _del(self, index, reverse):
        val = None
        if index == 0:
            val = self.head.value
            self.head = self.head.next_node
            self.head.prev_node = None
        elif index == self.length-1:
            val = self.tail.value
            self.tail = self.tail.prev_node
            self.tail.next_node = None
        elif reverse:
            i = self.length-1
            node = self.tail

            while i != index:
                node = node.prev_node
                i -= 1

            val = node.value
            node.prev_node.next_node, node.next_node.prev_node = node.next_node, node.prev_node
            del node
            return val
        else:
            i = 0
            node = self.head

            while i != index:
                node = node.next_node
                i += 1

            val = node.value
            node.prev_node.next_node, node.next_node.prev_node = node.next_node, node.prev_node
            del node
            return val

    def delete(self, index):
        val = None
        if self.head:
            if index > self.length // 2:
                val = self._del(index, True)
            elif index <= self.length // 2:
                val = self._del(index, False)
        self.length -= 1
        return val

    def __iter__(self):
        node = self.head

        while node:
            yield node.value
            node = node.next_node


if __name__ == '__main__':
    dbl = DbList()
    dbl.add(123)
    dbl.add(10)
    dbl.add(0)
    dbl.add(14)
    dbl.add(38)

    dbl.delete(4)

    for i in dbl:
        print(i)