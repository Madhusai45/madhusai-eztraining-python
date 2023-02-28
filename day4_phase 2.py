stack=[]
def push():
    element=int(input("enter the element:"))
    stack.append(element)
    print(stack)
def pop_stack():
    if not stack:
        print("empty")
    else:
        e=stack.pop()
        print("removed element",e)
        print(stack)
while True:
    print("select operation 1.push 2.pop 3.quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop_stack()
    elif choice==3:
        break
    else:
        print("enter the current operation")


# #                   stack using linkked list
# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class stack:
#     def __init__(self):
#         self.head=None
#     def isempty(self):
#         if self.head==None:
#             return True
#     def push(self,data):
#         if self.head==None:
#             self.head=node(data)
#         else:
#             newnode=node(data)
#             newnode.next=self.head
#             self.head=newnode
#     def pop(self):
#         if self.isempty():
#             return None
#         else:
#             poppednode=self.head
#             self.head=self.head.next
#             poppednode.next=None
#             return poppednode.data
#     def peek(self):
#         if self.isempty():
#             return None
#         else:
#             return self.head.data
#     def display(self):
#         t=self.head
#         if self.isempty():
#             print("stack Underflow")
#         else:
#             while(t !=None):
#                 print(t.data,end=" ")
#                 t=t.next
#                 if (t!=None):
#                     print("-->",end=" ")
#             return
        
if __name__=="__main__":
    s=stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.display()
    print(s.peek())
    s.pop()
    s.pop()
    s.display()

s=input()
s1=[]
balanced=True
for char in s:
    if (char=="(" or char=="[" or char=="{"):
        s1.append(char)
    elif (char=="}"):
        if (len(s1) and s1.pop()!="{"):
            balanced=False
            break
    elif (char=="]"):
        if (len(s1) and s1.pop()!="]"):
            balanced=False
            break
    elif (char==")"):
        if (len(s1) and s1.pop()!=")"):
            balanced=False
    else:
        balanced=False
if (balanced==False or len(str)):
    print("not balanced")
else:
    print("balanced")

                        queue
queue=[]
def enqueue():
    ele=input("enter element")
    queue.append(ele)
    print(ele,"is added in q")
def dequeu():
    if not queue:
        print("q is Empty")
    else:
        e=queue.pop(0)
        print("removed element",e)
def display():
    print(queue)
while True:
    print("selct operation 1.add 2.remove 3.quit 4.show ")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeu()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("pls enter correct operation")

from queue import LifoQueue
s=LifoQueue(maxsize=3)
print(s.qsize())
s.put("a")
s.put("b")
s.put("c")
print(s.full())
print(s.qsize())
print(s.get())
print(s.get())
print(s.get())

print(s.empty())

import queue
l=queue.Queue(maxsize=6)
l.put(2)
l.put(5)
l.put(8)
print(l.get())
print(l.get())
print(l.get())

#      queue using linnked list
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class queue:
    def __init__(self):
        self.head=None
        self.last=None
    def enqueue(self,data):
        if self.last is None:
            self.head=node(data)
            self.last=self.head
        else:
            self.last.next=node(data)
            self.last=self.last.next
    def dequeue(self):
        if self.head is None:
            return None
        else:
            to_return=self.head.data
            self.head=self.head.next
            return to_return
a_queue=queue()
while True:
    print("enqueue <value>")
    print("dequeue")
    print("quit")
    do=input("what would you like to do ").split()
    op=do[0].strip().lower()
    if op=='enqueue':
        a_queue.enqueue(int(do[1]))
    elif op=='dequeue':
        dequeued=a_queue.dequeue()
        if dequeued is None:
            print("queue is Empty")
        else:
            print("Dequeued element",
                  int(dequeued))
    elif op=="quit":
        break    