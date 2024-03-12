from task3 import CircularQueue
class Scheduler:
    def __init__(self, processArray, processArrayLength, timeQuantum):
        self.processArray = processArray
        self.processArrayLength = processArrayLength
        self.timeQuantum = timeQuantum
        self.process = CircularQueue(self.processArrayLength)


    def assignProcessor(self):
        for process in self.processArray:
            self.process.enqueue(process)
        
        
        while not self.process.isEmpty():
            
            current_process = self.process.dequeue()
            print(f"Execution time {current_process.processName} for",end=" ")
            if current_process.processExecTime > self.timeQuantum:
                print(f"{self.timeQuantum} units")
                self.process.enqueue(current_process)
                current_process.processExecTime -= self.timeQuantum
            else:
                print(f"{current_process.processExecTime} units")

            
            

            
            


            
