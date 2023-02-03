#import random as r
# a='hello world'
# print(r.sample(a,2))


# a=[1,2,3,45,6]
# r.shuffle(a)
# print(a)

# a=["welcome","back"]
# print(r.choices(a,k=3))

# a=r.random()
# print(a)

# a=["a","b","c","d"]
# print(r.choices(a,key=10))

#calender program
# import calendar
# print("full calender")
# print(calendar.calendar(2023))
# print("month calender:")
# print(calendar.month(2023,2))
# print("seting wednesday as first day :")
# calendar.setfirstweekday(calendar.FRIDAY)
# print(calendar.month(2021,12))

# #date time
# import datetime
# a=datetime.datetime.now()
# print(a)

# sv=a.strftime("%y")
# fy=a.strftime("%Y")
# print("sv",sv)
# print("fy",fy)

#functions
#1.predefined 
# #2.user definrd

# for code reusebility we use functions
# if we want to use a particular concepts multiple times in our program instead of writing the same code 
# multiple times we can write it once include that inside a function  and can call the function
# where ever we need iter


# types:
# 1.functios without argument without return ValueError
# 2.without arguments with return value
# 3.with arguments without return value
# 4.with arguments with return value

#1st type:
# def samp(): #define
#     print("hello")
#     print("world")
# samp()
# print("dead")
# samp()

#2nd 
# def multi():
#     num1=int(input("number1:"))
#     num2=int(input("number2:"))
#     num3=int(input("number3:"))
#     num4=int(input("number4:"))
#     prod=num1*num2*num3*num4
#     return prod

# res=multi()
# print(res)

# #3rd type:
# def multi(n1,n2,n3):
#     prod=n1+n2+n3
#     return prod
#res=multi(3,4,5)
#print(res)
#                    or
# def add(n1,n2,n3):
#     sum=n1+n2+n3
#     return sum
# n1=int(input("enter a number1:"))
# n2=int(input("enter a number2:"))
# n3=int(input("enter a number3:"))
# res1=multi(n1,n2,n3)
# print(res1)
#                         #or
# def add(n[0],n[1],n[2]):
#     sum=n[0]+n[1]+n[2]
#     print(sum)
# l=list(map(int,input("enter numbers:").split()))
# add(l[0],l[1],l[2])

#lemons programs using function type1
#find factors of given num using funs type 2
#print mulitple table for the given number using functions type3
#find the sum of digits of given number using type4

# 1st

def lemons():
    lemon=int(input("enter no.of lemons"))
    if lemon>20:
        print("ed")
    elif lemon<20:
        print("nd")
    else:
        print("got")
lemons()

#4th

# n=int(input("enter a number"))
# for i in range(1,21):
#     print(n,'x',i,'=',i*n)

# def digits():
#     sum=0
#     while n!=0:
#         rem=n%10
#         sum=sum+rem
#         n=n//10
#     return sum
# n=int(input("enter a number"))
# res=digits(n)
# print(n)



#      recursive function
# a function which calls itself
# def disply():
#     n=int(input("enter a number"))
#     if n==5:
#         disply()
#     else:
#         print("over")
# disply()
# #  
# def fact(n):
#     if n==0:
#         return 1
#     return n*fact(n-1)

# result=fact(0)
# print(result)

# n=84
# for i in range(n):
#     j=i*(i-1)
# print(j)

n=int(input("enter a number"))
a=0
b=1
sum=0
count=1
while(count<=n):
    print(sum,end=" ")
    count+=1
    a=b
    b=sum
    sum=a+b




