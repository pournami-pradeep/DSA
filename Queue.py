class Queue:

    def __init__(self):
        self.queue = []
        self.length = 0
    

    def is_empty(self):
        if self.length == 0:
            return True
        return False
    

    def enqueue(self,data):
        self.queue.append(data)
        self.length += 1
        return


    def dequeue(self):
        if self.is_empty():
            print("Queue is empty...")
        data = self.queue[0]
        self.queue.pop(0)
        self.length -= 1
        print("poped successfully",data)
        return
    

    def get_rear(self):
        if self.is_empty():
            print("Queue is empty...")
        print("rear element is",self.queue[-1])
        return self.queue[-1]
    

    def get_front(self):
        if self.is_empty():
            print("Queue is empty...")
        print("front element is",self.queue[0])
        return self.queue[0]
    
    def print_queue(self):
        for items in self.queue:
            print("|",items,"|")
        return



# queue = Queue()
# queue.enqueue(5)
# queue.enqueue(9)
# queue.enqueue(15)
# queue.enqueue(20)
# queue.enqueue(15)
# queue.print_queue()
# queue.dequeue()
# queue.print_queue()
# print(queue.get_front())
# print(queue.get_rear())

