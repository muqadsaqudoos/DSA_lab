class Stacks:
    def __init__(self):
        self.stacks = []
        self.count = 0

    def push(self,data):
        self.stacks.append(data)
        self.count += 1

    def pop(self):
        if self.is_empty():
            return "Stack underflow"
        data = self.stacks[-1]
        del self.stacks[-1]
        self.count -= 1
        return data
    
    def is_empty(self):
        return self.count == 0
    
    def display(self):
        for i in range(len(self.stacks)):
            print(self.stacks[i],end = " ")

        print()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stacks[-1]

    

def main():
    root = Stacks()
    root.push(5)
    root.push(10)
    root.push(15)
    print(root.count)
    root.display()
    print(root.peek())
    root.pop()
    print(root.count)
    print(root.peek())

main()


