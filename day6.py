# # #                                  EXCEPTION HANDLING                          
# # #When there is exception ,developer doesnot doesnot interrupt or exception in the flow .to acheive this we 
# # # are using exception handling  


# # # a=int(input("enter a number"))
# # # b=int(input("enter a number"))
# # # try:
# # #     print(a//b)
# # # except Exception as e:
# # #     print(e,"cannot be divided by zero")
# # # print("good")

# # # # a=int(input("enter a number"))
# # # # b=int(input("enter a number"))
# # # # try:
# # # #     print(a//b)
# # # # except Exception as e:
# # # #     print(e,"cannot be divided by zero")
# # # # finally:
# # # #     print("resource closed")

# # # a=82
# # # try:
# # #     b=int(input("enter a number:"))
# # #     print("resource opened")
# # #     print(a//b)
# # # except ZeroDivisionError as e:
# # #     print(e,"cannot be divided by zero")
# # # except ValueError as e:
# # #     print(e,"invalid input")
# # # except Exception as e:
# # #     print("other error",e)
# # # finally:
# # #     print("resource closed")

# # #even or odd using exception handling
# # a=10
# # if a%2=0:
# #     raise Exception("a should be even")
# # else:
# #     print("odd number")

# class birds:
#     def parts(self):
#         print("s")
# parrot=birds()
# parrot.parts()
# piegon=birds()
# piegon.parts()

#                                   constructer prog 
# class employees:
#     def __init__(self,name,id):
#         self.id=id
#         self.name=name
#     def display(self):
#         print("ID : %d \nName: is")
#         print(self.id,self.name)
# emp1=employees('madhu',100)
# emp2=employees('sai',100)
# emp1.display()
# emp2.display()
class computer():
    a=10
    b=20
    print("class variable inside in class",a)

    def config(self):
        c=100
        print("yes")
        print("instane access",self.b)
lenovo=computer()
print(lenovo.a)
print(lenovo.a+lenovo.b)
dell=computer()
print("dell",dell.a)
lenovo.config()