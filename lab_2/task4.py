class Node:
    def __init__(self, val , next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None


    def insert_at_head(self,val):
        node = Node(val,self.head)
        self.head = node


    def display(self):
        itr = self.head
        str = ""
        
        while itr:
            str += f"{itr.val} "
            itr = itr.next

        return str
    
    def insert_at_tail(self,val):
        node = Node(val)
        if self.head is None:
            self.head = node
            return 
        else:
            itr = self.head
            while itr.next is not None:
                itr = itr.next
            itr.next = node

    def insert_after(self,key,val):
        itr = self.head
        while itr:
            if itr.val == key:
                node = Node(val,itr.next)
                itr.next = node
            itr = itr.next

    def search(self,key):
        itr = self.head
        while itr:
            if itr.val == key:
                return True
            
            itr = itr.next
        return False                
    
    def insert_before(self,key,val):
        node = Node(val)
        if self.head is None:
            self.head = node
            return 
        
        else:
            current = self.head
            if current.next is not None and current.next.val != key:
                current = current.next

            node.next = current.next
            current.next = node 
              

def main():
    obj = LinkedList()
    obj.insert_at_head(2)
    obj.insert_at_head(3)
    obj.insert_at_tail(9)
    print(obj.search(9))
    obj.insert_after(3,4)
    obj.insert_before(2,4)
    print(obj.display())

main()



