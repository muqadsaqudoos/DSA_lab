def calculateGCD(A,B):
    if B==0 :
        return A
    
    return calculateGCD(B,A%B)
def main():
    print(calculateGCD(15,5))
main()