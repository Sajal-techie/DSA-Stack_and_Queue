class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        print(new_node.data, "enqueued ")
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.ref = new_node
            self.rear = new_node

    def dequeue(self):
        print(self.rear.data, "dequeued ")
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.ref

    def isEmpty(self):
        if self.front is None:
            return True
        return False

    def frontt(self):
        print(self.front.data)

    def rearr(self):
        print(self.rear.data)


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.dequeue()
queue.frontt()
queue.rearr()