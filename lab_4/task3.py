class CircularQueue():

    def __init__(self, size): 
        self.size = size

        self.queue = [None for i in range(size)]
        self.front = self.rear = -1

    def enqueue(self, data):
        if self.isFull():
            return "It is Full"
        
        if self.front == -1:
            self.front = 0
        if self.rear+1 < self.size:
            self.rear += 1
            self.queue[self.rear] =data
        
    def dequeue(self):
        if self.isEmpty:
            return "it is empty"
        
        data = self.queue[self.front]
        self.front = self.front + 1
        
        return data
        
    def display(self):
        
        if self.isEmpty():
            return "It is empty"
        if self.front <= self.rear:
            for i in range(self.front,self.rear+1):
                print(self.queue[i],end =" ")
        print()

        
    
    def isEmpty(self):
        if self.front == self.rear == -1:
            return True
        return False
    
    
    def isFull(self):
        if self.rear+1 == self.size:
            return True
        return False
def main():
    ob = CircularQueue(5)
    ob.enqueue(14)
    ob.enqueue(22)
    ob.enqueue(13)
    ob.enqueue(-6)
    ob.display()
    print("Deleted value = ", ob.dequeue())
    print("Deleted value = ", ob.dequeue())
    ob.display()
    ob.enqueue(9)
    ob.enqueue(20)
    ob.enqueue(5)
    ob.display()
main()
