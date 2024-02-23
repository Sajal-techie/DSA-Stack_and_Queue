class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size

    def isFull(self):
        return self.size == len(self.queue)

    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, data):
        if not self.isFull():
            self.queue.append(data)
            print("enqueued", data)
        else:
            print("Queue is Full")

    def dequeue(self):
        if not self.isEmpty():
            print("dequeued", self.queue.pop(0))
        else:
            print("Queue Empty")

    def front(self):
        if not self.isEmpty():
            print("Front", self.queue[0])
        else:
            print("Queue is Empty")

    def rear(self):
        if not self.isEmpty():
            print("rear", self.queue[-1])
        else:
            print("Empty Queue")

    def display(self):
        if self.isEmpty():
            print("Empty queue")
        else:
            print("front -->", self.queue, "<-- rear")


queue = Queue(4)
queue.enqueue(3)
queue.enqueue(6)
queue.enqueue(1)
queue.enqueue(0)
queue.enqueue(5)
queue.display()
queue.front()
queue.rear()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.enqueue(1)
queue.dequeue()
queue.display()
queue.front()
queue.rear()
