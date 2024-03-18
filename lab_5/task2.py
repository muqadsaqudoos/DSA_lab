def precedence(op):
    if op in "*/":
        return 2
    elif op in "+-":
        return 1
    else:
        return 0

def is_operand(ch):
    return ch.isalpha()

def infix_to_prefix(infix):
    stack = []
    prefix = ""
    infix = infix[::-1]
    for char in infix:
        if is_operand(char):
            prefix += char
        elif char == ")":
            stack.append(char)
        elif char == "(":
            while stack and stack[-1] != ")":
                prefix += stack.pop()
            if stack:
                stack.pop()
        else:
            while stack and precedence(stack[-1])>=precedence(char):
                prefix += stack.pop()

            stack.append(char)

    while stack:
        prefix += stack.pop()
    return prefix[::-1]


a = "(A+B)*(C+D)"
print(infix_to_prefix(a))
