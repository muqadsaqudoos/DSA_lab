
def precedence(op):
    if op in "*/":
        return 2
    elif op in "+-":
        return 1
    else:
        return 0

def is_operand(ch):
    a = ["+","*","-","/","^","(",")","{","}","[","]"]
    if ch not in a:
        return True

def infix_to_postfix(string):
    stack = []
    output = ""
    i = 0
    while i < len(string):
        if is_operand(string[i]):
            output += string[i]
        elif string[i] == "(":
            stack.append(string[i])
        elif string[i] == ")":
            while stack and stack[-1] != "(":
                output += stack.pop()
            if stack:
                stack.pop()  
        else:  
            while stack and precedence(stack[-1]) >= precedence(string[i]):
                output += stack.pop()
            stack.append(string[i])
        i += 1

    while stack:

        output += stack.pop()
    return output


a = "(A+B/C*(D+E)-F)"
print(infix_to_postfix(a))



            

