def dec2oct(n):
    if n == 0 :
        return "0"
    elif n == 1:
        return "1"
    return (dec2oct(n//8)) + str(n%8)

print(dec2oct(8))
print(dec2oct(25))
