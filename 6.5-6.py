import priorityqueue


class FifoWithPriorityQueue:
    def __init__(self):
        self.p_queue = priorityqueue.SimplePriorityQueue([])
        self.counter = 0

    def enqueue(self):
        self.p_queue.insert(self.counter)
        self.counter -= 1
        self.p_queue.print_queue()

    def dequeue(self):
        value = self.p_queue.extract_max()
        self.p_queue.print_queue()
        return value

    def print_fifo(self):
        self.p_queue.print_queue()


class StackWithPriorityQueue:
    def __init__(self):
        self.p_queue = priorityqueue.SimplePriorityQueue([])
        self.counter = 0

    def push(self):
        self.p_queue.insert(self.counter)
        self.counter += 1
        self.p_queue.print_queue()

    def pop(self):
        value = self.p_queue.extract_max()
        self.p_queue.print_queue()
        return value


fifo = FifoWithPriorityQueue()
fifo.enqueue()
fifo.enqueue()
fifo.enqueue()
fifo.dequeue()
fifo.enqueue()
fifo.enqueue()
fifo.dequeue()


stack = StackWithPriorityQueue()
stack.push()
stack.push()
stack.push()
stack.pop()
stack.push()
stack.push()
stack.pop()
