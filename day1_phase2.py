#protected
class encap:
    _a=10
    c=20
    def encapfunction(self):
        _b=200
        print("Encap function -accessing protected")
        print(self._a+10)

    
obj=encap()
print(obj._a)
obj.encapfunction()
print(obj.c)

#private
class encap:
    __a=10
    print(__a)
    def encapfunction(self):
        print("Encap Function")
        print(self.__a)
obj=encap()
obj.encapfunction()
print(obj.__a)
 

#                polymorphism

#one item or same item used for different purposes  





# Method overloading
class moverload:
    def display(self,a=None,b=None):
        print(a,b)
obj=moverload()
print("without argument")
obj.display()

print("with argument")
obj.display(20,30)
print("with one argument")
obj.display(10)


#if a mehod is defective or cannot be used inside derived class it will



class peta():
    def placename(self):
        print("peta place name is prag")
    def student(self):
        print("yes-peta")
    def which_year(self):
        print("3rd year")
class bhimavaram():
    def placename(self):
        print("bhimavaram is placename")
    def student(self):
        print("yes-bvrm")
    def which_year(self):
        print("3rd year")
obj1=peta()
obj2=bhimavaram()
for details in (obj1,obj2):
    details.placename()
    details.student()
    details.which_year()


#                      singlelinked list
class node:
    def __init__(self,data):
        self.data= data
        self.next=None
class all:
    def __init__(self):
        self.head=None
    def display(self):

        if  self.head is None:
            print("Linked Listis Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next
obj=all()
n=node(10)
obj.head=n
n1=node(20)
obj.head.next=n1
n2=node(30)
n1.next=n2
obj.display()

#                   insertion
class node1:
    def __init__(self,data):
        self.data=data
        self.next=None
class single:
    def __init__(self):
        self.head=None
    def insert_beginning(self,data):
        nb=node1(data)
        nb.next=self.head
        self.head=nb
    def display(self):
        if self.head is None:
            print("Linked List")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next
obj1=single()
n=node1(10)
obj1.head=n
n1=node1(20)
obj1.head.next=n1
n2=node1(30)
n1.next=n2
n3=node1(40)
n2.next=n3
print("before insertion")
obj1.insert_beginning(100)
obj1.display()
print(" ")
print("after insertion")
obj1.insert_beginning(555)
obj1.display()
        
