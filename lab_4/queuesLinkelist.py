class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    def is_empty(self):
        return self.front is None
    
    def enqueue(self,data):
        newNode = Node(data)
        if self.is_empty():
            self.front = self.rear = newNode
            self.count += 1
            return
        self.rear.next = newNode
        self.rear = newNode
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            return "Queue Underflow"
        temp = self.front.data
        self.front = self.front.next
        self.count -= 1
        return temp

    def display(self):
        temp = self.front
        while temp is not None:
            print(temp.data,end=" ")
            temp = temp.next

        print()

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.front.data
        

def main():
    root = Queue()
    root.enqueue(9)
    root.enqueue(8)
    root.enqueue(7)
    print(root.peek())
    root.display()
    print(root.dequeue())
    print(root.count)
main()
