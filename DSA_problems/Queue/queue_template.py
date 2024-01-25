def print_after(func):
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)  # Call the original function
        self.print_queue()                    # Call print_queue after
        return result
    return wrapper

class Queue:
    def __init__(self):
        self.queue = []
        self.head = 0
        self.tail = -1
    
    @print_after
    def enqueue(self, value):
        self.tail += 1
        self.queue.append(value)

    @print_after
    def dequeue(self):
        if self.is_empty():
            return
        value = self.queue[self.head]
        self.head += 1
        return value


    
    def is_empty(self):
        if self.head > self.tail:
            return True

        return False

    def print_queue(self):
        for i in range(self.head, self.tail+1):
            print(self.queue[i], end = ", ")
        print()

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.dequeue()
q.dequeue()
q.dequeue()
q.enqueue(5)
q.dequeue()
q.dequeue()
q.enqueue(7)
q.enqueue(9)

