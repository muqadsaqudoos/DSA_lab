
def isPrime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return n
    

def digit(s,i,j):
    if len(s)<=1:
        return "Good"
         
    
    if int(s[i])%2 != 0:
        return "Not good"
    
    elif not isPrime(int(s[j])):
        return "Not good"
    
    else:
        return digit(s[2:],0,1)
  

print(digit("572727",0,1))
 


    


    





