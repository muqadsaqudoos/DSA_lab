def precedence(op):
    if op in "*/":
        return 2
    elif op in "+-":
        return 1
    else:
        return 0

def is_operand(ch):
    return ch.isnumeric()

def infix_to_prefix(string):
    stack = []
    output = ""
    string = string[::-1]
    for char in string:
        if is_operand(char):
            output += char 
        elif char == "(":
            stack.append(char)
        elif char == ")":
            while stack and stack[-1] != "(":
                
                output += stack.pop()
            stack.pop()
        else:  
            while stack and precedence(stack[-1]) >precedence(char):
                output += stack.pop()
            stack.append(char)

    while stack:

        output += stack.pop()
    return output[::-1]


a = "(A+B)*(C+D)"
print(infix_to_prefix(a))
