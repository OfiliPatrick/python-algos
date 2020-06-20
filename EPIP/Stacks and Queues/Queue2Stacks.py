class Queue(object):

    def __init__(self):
        self.first_stack = []
        self.second_stack = []

    def printAll(self):
        for ele in self.first_stack:
            print(ele)


    def enqueue(self, ele):
        self.first_stack.append(ele)
    def dequeue(self):
        while self.first_stack:
            self.second_stack.append(self.first_stack.pop())
        if self.second_stack:  
            return self.second_stack.pop()
        else:
            return "empty queue"


my_queue = Queue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

my_queue.printAll()

print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())




    