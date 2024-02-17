class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(item, "'pushed to stack'")

    def pop(self): 
        if not self.isEmpty():
            print(self.stack.pop(), "'popped from stack'")
        else:
            print("stack is empty")

    def peek(self):
        if not self.isEmpty():
            print(self.stack[-1])
        else:
            print("Stack is empty")

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        print("size", len(self.stack))
        return len(self.stack)


stack = Stack()
stack.push(1)
stack.push(2)
stack.size()
stack.peek()
stack.pop()
stack.pop()
stack.peek()
stack.push(6)
stack.push(7)
stack.pop()
stack.size()
stack.isEmpty()