class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class Stack:
    def __init__(self, max_size=None):
        self.top = None
        self.size = 0
        self.max_size = max_size

    def push(self, data):
        if not self.isFull() or self.max_size is None:
            new_node = Node(data)
            new_node.ref = self.top
            self.top = new_node
            self.size += 1
            print(new_node.data, "pushed to Stack")
        else:
            print("Stack Overflow")

    def isFull(self):
        return self.size == self.max_size

    def isEmpty(self):
        return self.size == 0

    def pop(self):
        if not self.isEmpty():
            print(self.top.data, "Popped from Stack")
            self.top = self.top.ref
        else:
            print("Stack Underflow")

    def peek(self):
        print(self.top.data, "Top")

    def sizee(self):
        print(self.size, "size")

    def display(self):
        if self.isEmpty():
            print(" EMpty stack ")
        else:
            n = self.top
            print("top -->", end=" ")
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.ref
            print()


stack = Stack(4)
stack.push(1)
stack.sizee()
stack.peek()
stack.push(2)
stack.peek()
stack.push(4)
stack.push(6)
stack.push(8)
stack.display()
stack.sizee()
stack.peek()
stack.pop()
stack.peek()
stack.display()