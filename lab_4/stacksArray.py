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

    def balancedParanthesis(self,eq):
        opening = ["(", "{" , "["]
        closing = [")", "}", "]"]
        for i in range(len(eq)):
            if eq[i] == "(" or eq[i] == "{" or eq[i] == "[":
                self.push(eq[i])
            elif (self.peek() == opening[0] and eq[i] == closing[0]) or (self.peek() == opening[1] and eq[i] == closing[1]) or (self.peek() == opening[2] and eq[i] == closing[2]):
                self.pop()

        if self.count == 0:
            print("Balanced Paranthesis")
        else:
            print("Not balanced paranthesis")

def stringWordsReverse(line):
    s = " "
    obj = Stacks()
    for i in range(len(line)):
        if line[i] == " ":
            while not obj.is_empty():
                s += str(obj.pop())
            s += " "

        else:
            obj.push(line[i])
    while not obj.is_empty():
        s += obj.pop()
    return s

    


        


            

def main():
    root = Stacks()
    print("Paranthesies")
    root.balancedParanthesis("[{(a + b) * (c - d)}")
    print()
    print("string Words Reverse")
    print(stringWordsReverse("Welcome to DSA"))
    
main()



