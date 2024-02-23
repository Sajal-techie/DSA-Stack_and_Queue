class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.ref = self.top
        self.top = new_node
        print(new_node.data, "pushed in stack")

    def isEmpty(self):
        return self.top is None

    def pop(self):
        if not self.isEmpty():
            print(self.top.data, "popped from stack ")
            self.top = self.top.ref
        else:
            print("linked list is empty")

    def peek(self):
        if not self.isEmpty():
            print(self.top.data)
        else:
            print("linked list is empty")


stack = Stack()
stack.push(4)
stack.push(5)
stack.pop()
stack.peek()
