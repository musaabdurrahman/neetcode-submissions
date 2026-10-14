class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        elif index <= self.size // 2:
            curr = self.head
            for x in range(index):
                curr = curr.next
        else:
            curr = self.tail
            for x in range(self.size - 1 - index):
                curr = curr.prev
        return curr.val

        

    def addAtHead(self, val: int) -> None:
        if self.head == None:
            self.head = Node(val)
            self.tail = self.head
        else:
            new_node = Node(val)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size = self.size + 1


    def addAtTail(self, val: int) -> None:
        if self.tail == None:
            self.tail = Node(val)
            self.head = self.tail
        else:
            new_node = Node(val)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size = self.size + 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.size:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        elif index > 0 and index < self.size:
            if index <= self.size // 2:
                curr = self.head
                for x in range(index):
                    curr = curr.next
            else:
                curr = self.tail
                for x in range(self.size - 1 - index):
                    curr = curr.prev
            new_node = Node(val)
            temp = curr.prev

            new_node.prev = temp
            new_node.next = curr

            temp.next = new_node
            curr.prev = new_node

            self.size = self.size + 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        if index <= self.size // 2:
            curr = self.head
            for x in range(index):
                curr = curr.next
        else:
            curr = self.tail
            for x in range(self.size - 1 - index):
                curr = curr.prev

        if curr.prev is None:
            self.head = curr.next
        else:
            curr.prev.next = curr.next

        if curr.next is None:
            self.tail = curr.prev
        else:
            curr.next.prev = curr.prev

        self.size -= 1

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)