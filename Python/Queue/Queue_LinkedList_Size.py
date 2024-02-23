class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class Queue:
    def __init__(self, max_size=None):
        self.front = None
        self.back = None
        self.size = 0
        self.max_size = max_size

    def isFull(self):
        return self.size == self.max_size

    def isEmpty(self):
        return self.size == 0

    def enqueue(self, data):
        if not self.isFull():
            new_node = Node(data)

            if self.front is None:
                self.front = new_node
                self.back = new_node
            else:
                self.back.ref = new_node
                self.back = new_node
            self.size += 1
            print(new_node.data, "'enqueued'")
        else:
            print("Queue is Full")

    def dequeue(self):
        if not self.isEmpty():
            print(self.front.data, "'dequeued'")
            self.front = self.front.ref
            self.size -= 1
        else:
            print("Empty Queue")

    def peek(self):
        if self.isEmpty():
            print("Queue Empty")
        else:
            print(self.front.data, "'Front'")

    def rear(self):
        if self.isEmpty():
            print("queue empty")
        else:
            print(self.back.data, "'Rear'")

    def display(self):
        if self.front is None:
            print("Queue is Empty")
        else:
            n = self.front
            print("front -->", end=" ")
            while n is not None:
                print(n.data, ",", end=" ")
                n = n.ref
            print("<-- back")


queue = Queue(4)
queue.enqueue(5)
queue.enqueue(2)
queue.enqueue(1)
queue.enqueue(9)
queue.enqueue(0)
queue.display()
queue.peek()
queue.rear()
queue.dequeue()
queue.display()
queue.peek()
queue.rear()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.enqueue(4)
queue.dequeue()
queue.display()
queue.peek()
queue.rear()