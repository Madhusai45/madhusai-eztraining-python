##                          DLL
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None

    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next

obj=dll()
n1=Node(100)
obj.head=n1
n2=Node(200)
n2.previous=n1
n1.next=n2
obj.display()

             insertion of DLL
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def insert_start(self):
        n=Node(300)
        temp=self.head
        temp.previous=n
        n.next=temp
        self.head=n
    
    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next

obj=dll()
n1=Node(100)
obj.head=n1
n2=Node(200)
n2.previous=n1
n1.next=n2
obj.insert_start()
obj.display()

insert at pos
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def insert_pos(self,pos):
        n=Node(300)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
            n.previous=temp
            n.next=temp.next
            temp.next.previous=n
            temp.next=n


    
    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next

obj=dll()
n1=Node(100)
obj.head=n1
n2=Node(200)
n2.previous=n1
n1.next=n2
obj.insert_pos(2)
obj.display()


        delete at begining
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def delete_begining(self):
        temp=self.head
        self.head=temp.next

        temp.next=None


    
    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next

obj=dll()
n1=Node(100)
obj.head=n1
n2=Node(200)
n2.previous=n1
n1.next=n2
obj.delete_begining()
obj.display()


#  delete at end
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def delete_end(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next

        prev.next=None


    
    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next

obj=dll()
n1=Node(100)
obj.head=n1
n2=Node(200)
n2.previous=n1
n1.next=n2
obj.delete_end()
obj.display()

             delete at position
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def delete_pos(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None

        temp.next=None


    
    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next

obj=dll()
n1=Node(100)
obj.head=n1
n2=Node(200)
n2.previous=n1
n1.next=n2
obj.delete_pos(2)
obj.display()

                 circular linked list
  delete at end
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def delete_end(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next

        prev.next=None


    
    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next

obj=dll()
n1=Node(100)
obj.head=n1
n2=Node(200)
n2.previous=n1
n1.next=n2
obj.delete_end()
obj.display()

#              delete at position
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def delete_pos(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None

        temp.next=None


    
    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next

obj=dll()
n1=Node(100)
obj.head=n1
n2=Node(200)
n2.previous=n1
n1.next=n2
obj.delete_pos(2)
obj.display()
  delete at end
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def delete_end(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next

        prev.next=None


    
    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next

obj=dll()
n1=Node(100)
obj.head=n1
n2=Node(200)
n2.previous=n1
n1.next=n2
obj.delete_end()
obj.display()

#              delete at position
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class circular:
    def __init__(self):
        self.head=Node(None)
        self.tail=Node(None)
        self.head.next=self.tail
        self.tail.next=self.head


    def add(self,data):
        newNode=Node(data)
        if self.head.data is None:
            self.head=newNode
            self.tail=newNode
            newNode.next=self.head
        else:
            self.tail.next=newNode
            self.tail=newNode
            self.tail.next=self.head
    def display(self):
        current=self.head
        if self.head is None:
            print("List is Empty")
        else:
            print("Nodes of the Circular list:")
            print(current.data,"-->")
            while(current.next!=self.head):
                current=current.next
                print(current.data,"-->")     

class circularLinkedList:
    c1=circular()
    c1.add("S")
    c1.add("a")
    c1.add("s")
    c1.add("s")
    c1.display()
