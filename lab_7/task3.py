import random
def getRandomNumber(s,e):
    return random.randint(s, e)
def size():
    
    dicty = {}
    for i in range(10,101,10):
        sum = 0
        for j in range(50):
            table = [False]*i
            sum1 = 0
            while True:
                a = getRandomNumber(1,101)
                index = a%i
                if table[index]:
                    break
                table[index] = True
                sum1+=1
            sum+=sum1

        avgSum=sum/i
        dicty[i] = avgSum
    
    return dicty


def main():
    print(size())


main()
            

            
                
            