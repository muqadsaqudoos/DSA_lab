from collections import deque
class Queues:
    def __init__(self):
        self.queues = []
        self.count = 0

    def is_empty(self):
        return self.count == 0
    
    def enqueque(self,data):
        self.queues.append(data)
        self.count += 1 

    def dequeue(self):
        if self.is_empty():
            return "Queue Underflow"
        data = self.queues[0]
        del self.queues[0]
        self.count -= 1
        return data
    
    def display(self):
        for i in range(len(self.queues)):
            print(self.queues[i],end= " ")
        print()


    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queues[0]
    

def main():
    root = Queues()
    print(root.dequeue())
    root.display()

main()
    
    


        

    

