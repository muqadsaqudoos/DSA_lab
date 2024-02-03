class Term:
    def __init__(self, coffiecient, degree):
        self.coffiecient = coffiecient
        self.degree = degree

    def __str__(self):
        return f"{self.coffiecient}x^{self.degree}"




class Polynomial:
    def __init__(self):
        self.a = []        

    def __str__(self):
        pstr = ""
        for i in range(0, len(self.a)-1):
            pstr += f"{self.a[i]}"
            pstr += f"+"
        pstr += f"{self.a[-1]}"
        return pstr
    
    def addTerm(self,cofficients,power):
        
        b = Term(cofficients, power)
        self.a.append(b)

    def getDegree(self):
        return (self.a[0].degree)
    
    def getCofficient(self,power):
         for i in range(0, len(self.a)):
            if power == self.a[i].degree:
                return self.a[i].coffiecient

    def evaluate(self, value):
        sum = 0
        for i in range(0, len(self.a)-1):
            sum += (self.a[i].coffiecient)*value**(self.a[i].degree)

        sum += self.a[-1].coffiecient
        return sum
    
    def __add__(self,other):
        b = Polynomial()
        for i in range(0,len(self.a)):
            b.addTerm(self.a[i].coffiecient + other.a[i].coffiecient,self.a[i].degree)

        return b 
    
    def derivative(self):
        b = Polynomial()
        for i in range(0,len(self.a)):
            if self.a[i].degree != 0 :
                b.addTerm(self.a[i].degree*self.a[i].coffiecient,(self.a[i].degree)-1)

        return b
    
    def antiDerivative(self,constant):
        b = Polynomial()
        for i in range(0, len(self.a)):
            b.addTerm((self.a[i].coffiecient)//(self.a[i].degree+1),self.a[i].degree+1)
        b.addTerm(constant,0)
        return b
    
    def addtoCofficient(self,coffiecient,power):
        for i in range(0, len(self.a)):
            if power == self.a[i].degree:
                self.a[i].coffiecient =  self.a[i].coffiecient+coffiecient
                return self
            

    def setCofficient(self,newCoffiecient,power):
       for i in range(0, len(self.a)):
            if power == self.a[i].degree:
                self.a[i].coffiecient = newCoffiecient
                return self
            

    def __mul__(self,other):
        b = Polynomial()
        for i in range(0,len(self.a)):
            b.addTerm(self.a[i].coffiecient * other.a[i].coffiecient,self.a[i].degree+other.a[i].degree)

        return b
    
    def __sub__(self,other):
        b = Polynomial()
        for i in range(0,len(self.a)):
            b.addTerm(self.a[i].coffiecient - other.a[i].coffiecient,self.a[i].degree)

        return b
    
    def clear(self):
        for i in range(0,len(self.a)):
            self.a[i].coffiecient = 0

        return self


                
            

            
        
            

        
            
    




   
            




def main(): 
    p1 = Polynomial()
    p1.addTerm(4, 5)
    p1.addTerm(7, 3)
    p1.addTerm(-1, 2)
    p1.addTerm(9, 0)
    print(p1)
    print(p1.getDegree())
    print(p1.getCofficient(0))
    print(p1.evaluate(2))
    p2 = Polynomial()
    p2.addTerm(2, 5)
    p2.addTerm(8, 3)
    p2.addTerm(1, 2)
    p2.addTerm(5, 0)
    print(p2)
    print(p1+p2)
    n = (p1.derivative())
    print(n)
    print(n.antiDerivative(9))
    print(p1.addtoCofficient(2,3))
    print(p1.setCofficient(2,3))
    print(p1*p2)
    print(p1-p2)
    print(p1.clear())





main()