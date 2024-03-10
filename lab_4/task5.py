class Process:
    def __init__(self, processId, processName, processExecTime):
        self.processId = processId
        self.processName = processName
        self.processExecTime = processExecTime

class Scheduler:
    def __init__(self, processArray, processArrayLength, timeQuantum):
        self.processArray = processArray
        self.processArrayLength = processArrayLength
        self.timeQuantum = timeQuantum
    def assignProcessor(self):
        
        
class Queues:

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
    arr = [Process(1, "notepad", 20), Process(13, "mp3player", 5), Process(4, 
    "bcc", 30), Process(11, "explorer", 2)]
    s = Scheduler(arr, 4, 5)


