class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)
        print(data, "'inserted to queue' ")

    def isEmpty(self):
        return not self.queue

    def dequeue(self):
        if not self.isEmpty():
            print(self.queue.pop(0), "'deleted from queue'")
        else:
            print("Queue is Empty ")

    def front(self):
        if not self.isEmpty():
            print(self.queue[0])
        else:
            print("Queue is Empty!")

    def rear(self):
        if not self.isEmpty():
            print(self.queue[-1])
        else:
            print("queue is empty")

    def size(self):
        print("size:", len(self.queue))


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.front()
queue.rear()
queue.size()
queue.dequeue()
queue.size()
queue.dequeue()
queue.dequeue()