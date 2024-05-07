class HashTable:
    def __init__(self, size):
        self.table = [None] * size 
        self.S = size # Total number of slots in the table
        self.n = 0 # Current number of elements present in the table
    def __del__(self):
        del self.table
        
        
    # Destructor
    def isEmpty(self):
        if self.n == 0:
          return "the table is empty"
         
    # Checks whether the hash table is empty or not
    def isFull(self):
        if self.s == self.n:
            return "the table is full"
    # Checks whether the hash table is full or not
    def loadFactor(self):
        return self.n/self.S
    # Calculates & returns the load factor of the hash table (n/S)
    def getHashValue(self, name):
        temp = 0
        for char in name:
            temp += ord(char)
        return temp
    
    def insert(self,name):
        if self.isEmpty():
            return "the table is empty"
        hash = self.getHashValue(name)
        hashValue = hash%self.S
        i = hashValue
        while i<self.S:
              print(i,end=" ")
              if self.table[i] == name:
                self.n+=1
                return True
            
              i+=1
            
        return False
    
    def search(self,name):
        if self.isEmpty():
            return "the table is empty"
        hashValue = self.getHashValue(name)
        hash = hashValue%self.S
        i = hash
        while i <self.S:
            print(i,end=" ")
            if self.table[i] == name:
                return True
            i+=1

        return False
    

    def display(self):
        i = 0
        while i<self.S:
            if self.table[i] == None:
                print("Empty",i)
            else:
                print(i,self.table[i])
            i+=1

    def remove(self,name):
        if self.isEmpty():
            return "the table is empty"
        hashValue = self.getHashValue(name)
        hash = hashValue%self.S
        i = hash
        while i < self.S:
            if self.table[i] == name:
                self.table[i] = None
                self.n-=1
                return True
            i+=1
        return False
    


def main():
    
   
    size = int(input("Enter the size of the hash table: "))
    hash_table = HashTable(size)

    while True:
        print("\n0: Exit")
        print("1: Insert")
        print("2: Search")
        print("3: Remove")
        print("4: Display")
        print("5: Load Factor")
        
        choice = input("Enter your choice: ")

        if choice == "0":
            print("Exiting the program.")
            break

        elif choice == "1":
            name = input("Enter a name to insert: ")
            if hash_table.insert(name):
                print("True")
            else:
                print("False")

        elif choice == "2":
            name = input("Enter a name to search: ")
            if hash_table.search(name):
                print("True")
            else:
                print("False")

        elif choice == "3":
            name = input("Enter a name to remove: ")
            if hash_table.remove(name):
                print("True")
            else:
                print("False")
        elif choice == "4":
            print("Displaying hash table:")
            hash_table.display()

        elif choice == "5":
            print("Load factor:", hash_table.loadFactor())

        else:
            print("Invalid choice. Please enter a valid option.")


main()
        
        
        
            
        
        
       
      


        
            
                
    

        
        
            



