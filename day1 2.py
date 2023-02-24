# l=[1,4,8,9]
# r=map(lambda x:x+1,l)
# print(list(r))
# res=map(lambda n:pow(n,2),l)
# # print(list(res))
# name="sam"
# (lambda name:print(name))(name)

# from math import sqrt


# l=[]
# for i in range(1,15):
#     if i%2==0:
#         l.append(i)
# print(l)
# rea=map(lambda n:sqrt(n),y)
# print(list(rea))

# from abc import ABC,@abstractmethod:


# class abstractdemo(ABC):
#     @abstractmethod 
#     def display(self):
#         None
#     def show(self):
#         None
# class demo(abstractdemo):
#     def display(self):
#         print("Absraction method")
#     def show (self):
#         print("2nd function")
# obj=demo()
# obj.display()
# obj.show()

# from calendar import c


# class parent:
#     def display(self):
#         print("parent class")
# class child(parent):
#     def show(self):
#         print("child class")
# c=child()
# c.display()
# c.show()


# class A:
#     n=30
# class B(A):
#     def calc(self):
#         c=self.n+70
#         print(c)
# obj=B()
# obj.calc()    


# class dad:
#     def adisplay(self):
#         print("dad class")
# class mom:
#     def bdisplay(self):
#         print("mom class")
# class child(dad,mom):
#     def cdisplay(self):
#         print("child class")
# c=child()
# c.adisplay()
# c.bdisplay()
# c.cdisplay()
#multilevel
# class grandparent:
#     def adisplay(self):
#         print("grandparent class")
# class parent(grandparent):
#     def bdisplay(self):
#         print("parent class")
# class child(parent):
#     def cdisplay(self):
#         print("child class")
# obj=child()
# obj.adisplay()
# obj.bdisplay()
# obj.cdisplay()

#hierical
# class parent:
#     def adisplay(self):
#         print("parent class") 
# class child1(parent):
#     def bdisplay(self):
#         print("child1 class")
# class child2(parent):
#     def cdisplay(self):
#         print("child2 class")
# o1=child1()
# o2=child2()
# o1.adisplay()
# o1.bdisplay()
# o2.adisplay()
# o2.cdisplay()


# #                        HYBIRD 
# class parent:
#     def adisplay(self):
#         print("parent class")
# class child1(parent):
#     def bdisplay(self):
#         print("child1 class")
# class child2(parent):
#     def cdisplay(self):
#         print("child2 class")
# class kid1(child1):
#     def ddisplay(self):
#         print("kid1 class")
# class kid2(child1):
#     def edisplay(self):
#         print("kid2 class")
# class kidd1(child2):
#     def fdisplay(self):
#         print("kidd1 class")
# class kidd2(child2):
#     def gdisplay(self):
#         print("kidd2 class")

# a1=kid1()
# a2=kid2()
# a3=kidd1()
# a4=kidd2()
# a1.adisplay()
# a1.bdisplay()
# a1.ddisplay()
# a2.adisplay()
# a2.bdisplay()
# a2.edisplay()
# a3.adisplay()
# a3.cdisplay()
# a3.fdisplay()
# a4.adisplay()
# a4.cdisplay()
# a4.gdisplay()

#                              HAPPY NUMBERS
num=int(input("enter a number"))
temp=num
while temp>1:
    sum=0
    digit=temp%10
    sum=sum+digit**2
    tem=temp//10
    sum=sum+tem**2
    temp=sum
    if sum==1:
        print("happy number")
        
print(sum)