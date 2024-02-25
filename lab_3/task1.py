class node:
    def __init__(self,val):
        self.val = val
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    #insertion
    def insert_at_head(self,val):
        newNode = node(val)
        if self.head is None:
            self.head = newNode
            return
        newNode.next = self.head
        self.head = newNode 

    def insert_at_tail(self,val):
        newNode = node(val)
        if self.head is None:
            self.head = newNode
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = newNode


    def insert_before(self,val,key):
        
        if self.head is None:
            return
        if self.head.val == key:
            newNode = node(val)
            newNode.next = self.head
            self.head = newNode
            return
        temp =  self.head
        temp2 = self.head
        while temp is not None:
            if key == temp.val :
                newNode = node(val)
                newNode.next = temp
                temp2.next = newNode
                return
            temp2 = temp
            temp = temp.next
        """
    def insert_after(self,val,key):
        if self.head is None:
            return 
        elif self.head.val == key:
            self.head.next = node(val)
        temp1 = self.head
        temp2 = self.head.next
        while temp2 is not None:
            if temp1.val == key:
                newNode = node(val)
                newNode.next = temp2
                temp1.next = newNode
            temp1 = temp1.next
            temp2 = temp2.next
        
"""


    #Remove
    def remove_at_head(self):
        if self.head is None:
            return
        temp = self.head
        self.head = temp.next
        del temp

    def remove_at_tail(self):
        if self.head is None:
            return
        if self.head.next is None:
            del self.head
        temp = self.head 
        temp2 = self.head
        while temp.next is not None:
            temp2 = temp
            temp = temp.next 
        del temp
        temp2.next = None

    def remove_before(self,key):
        if self.head is None or self.head.val == key:
            return 
        elif self.head.next.val == key:
            temp = self.head
            self.head = temp.next
            del temp
            return

        else:
            temp1 = self.head
            temp2 = self.head.next
            while temp2.next is not None:
                if temp2.next.val == key:
                    temp1.next = temp2.next
                    del temp2
                    return 
                
                temp1 = temp1.next
                temp2 = temp2.next

            
        
    def remove_after(self,key):
        if self.head is None and self.head.val == key:
            return
        temp1 = self.head
        temp2 = self.head.next
        while temp2 is not None:
            if temp1.val == key:
                temp1.next = temp2.next
                del temp2
                return 
            temp1 = temp1.next
            temp2 = temp2.next 
        if temp1.val == key :
            del temp2
            temp1.next = None
 
        
    #transversing
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.val,end = " ")
            temp = temp.next

    def search(self,key):
        
        if self.head is None:
            return False
        temp = self.head
        while temp is not None:
            if key == temp.val:
                return True
            temp = temp.next
        return False
    
    def update(self,key,val):
        if self.head is None:
            return
        temp = self.head
        while temp is not None:
            if temp.val == key:
                temp.val = val
                return
            temp = temp.next

    

    def count(self):
        if self.head is None:
            return 0
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next
        return count
    def get_middle(self):
        if self.head is None:
            return None
        temp1 = self.head
        temp2 = self.head
        while temp2 is not None and temp2.next is not None:
            temp1 = temp1.next
            temp2 = temp2.next.next

        return temp1.val

    def remove(self,val):
        if self.head is None:
            return
        if self.head.val == val:
            self.head = self.head.next

        current = self.head
        while current.next is not None and current.next.val != val:
            current = current.next
        if current.next is not None:
            current.next = current.next.next

        
            
    
    
    #task 2
    def remove_kth_node(self,key):
        if self.head is None:
            return False
        elif key == 1:
            self.head = self.head.next
            return True
        else:
            prev = None
            count = 1
            temp = self.head
            while temp is not None and count!=key:
                prev = temp
                temp = temp.next
                count += 1
            if temp:
                prev.next = temp.next
                return True
            return False     

"""
     #task3
    def combine(self, list1, list2):
        if list1.head is None and list2.head is None:
            return 
        elif list1.head is None :
            self.head = list1.head
            return 
        elif list2.head is None :
            self.head = list2.head
            return 
        else:
            self.head = list1.head
            temp = list1.head
            while temp.next is not None:
                temp = temp.next
            temp.next = list2.head
                

        #task 5
    def removeDuplicates(self):
            if self.head is None:
                return
            l = []
            temp = self.head
            prev = None
            while temp:
                if temp.val in l:
                    self.remove(temp.val)
                l.append(temp.val)
                temp = temp.next
            


    def reverse(self):
        if self.head is None:
            return None
        l = []
        temp = self.head
        while temp is not None:
            l.append(temp.val)
            temp = temp.next

        for i in range(len(l)-1,-1,-1):
            print(l[i],end= " ")


    def recursion_reverse(self,head):
        if not head:
            return 
      
        self.recursion_reverse(head.next)
        print(f"\n{head.val}")
        
            
        
    def mergeShuffle(self, list1, list2):
        if list1.head is None and list2.head is None:
            return 
        elif list1.head is None :
            self.head = list1.head
            return 
        elif list2.head is None :
            self.head = list2.head
            return 
        else:
            while list11 is not None:
                self.head.next = list1.head
                self.head.next = list2.head
                list1 = list1.next
                list2 = list2.next
                
                
                

    
"""            
                
            
            
                
            
def main():
    root = linkedList()
    root.insert_at_tail(5)    
    root.insert_at_tail(10)    
    root.insert_at_tail(20)    
    root.insert_at_tail(23)    
    root.insert_at_tail(25)
    print(root.remove_kth_node(0))
    root.display()
main()

