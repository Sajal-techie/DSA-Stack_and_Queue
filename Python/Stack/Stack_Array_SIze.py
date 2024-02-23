class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size

    def isFull(self):
        return self.size == len(self.stack)

    def push(self, data):
        if self.isFull():
            print("Stack Overflow")
        else:
            self.stack.append(data)
            print(data, "pushed to stack")

    def isEmpty(self):
        return not self.stack

    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
        else:
            print(self.stack.pop(), "popped from stack")

    def size(self):
        print(len(self.stack))

    def peek(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print(self.stack[-1], "top")

    def display(self):
        if self.isEmpty():
            print("empty Stack")
        else:
            print(self.stack, "--> top")


stack = Stack(5)
stack.push(1)
stack.push(2)
stack.peek()
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.display()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.peek()
stack.display()