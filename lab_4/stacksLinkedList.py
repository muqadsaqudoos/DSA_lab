class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stacks:
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self,data):
        newNode = Node(data)
        if self.is_empty():
            self.top = newNode
            self.count += 1
            return
        newNode.next = self.top
        self.top = newNode
        self.count +=1 

    def pop(self):
        if self.is_empty():
            return "Stack underflow"
        temp = self.top.data
        self.top = self.top.next
        self.count -= 1
        return temp

    def display(self):
        temp = self.top
        while temp is not None:
            print(temp.data,end=" ")
            temp = temp.next
        print()

    def is_empty(self):
        return self.top is None
        
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.top.data
def main():
    root = Stacks()
    """
    root.push(4)
    root.push(5)
    root.push(6)
    print(root.count)
    root.display()

    print(root.pop())
    print(root.count)
    print(root.pop())
    print(root.count)
    root.pop()
    root.is_empty()
    """
    print(root.pop())
main()




