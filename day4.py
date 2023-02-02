# #dictionary comprehension

#1st
d={n:n*n for n in range(1,5)}
print(d)

# # #2nd
# # old={'rice':40,'daal':80,'oil':110}
# # new={product:price*5 for(product,price) in old.items()}
# # print(new)

# # #3rd with checks
# # real={'sam':20,'sai':25,'thon':19}
# # new={name:age for (name,age) in real.items() if age>=20}
# # print(new)

# #create a list with 8 customers names display a dict which has customer names along with discounts for them from aparticular shop.
# import random
# customerlist=['murali','guna','mani','kasi','venkat','sekhar','anand','krishna']
# customerdisc={customer:random.randrange(1,50) for (customer) in (customerlist) }
# print(customerdisc)

# # #list into dict
# # l1=['manoj','reddy','rahul','sai']
# # l2=[24,23,22,12,10]
# # d={a:b for(a,b) in zip(l1,l2)}
# # print(d)


# # #5 percentages
# # l1=['manu','teja','sai','gowtham','prasad']
# # l2=[400,450,444,428,498]
# # percentage=[]
# # for i in range(len(l2)):
# #     percentage.append(l2[i]/500*100)
# # print(percentage)
# # studentper={a:b for(a,b) in zip(l1,percentage)}
# # print(studentper)

# #random percentage
# # l1=['manu','teja','sai','gowtham','prasad']
# # l2=[]
# # l3=[]
# # for i in range(len(l1)):
# #     l2.append(random.randrange(250,500)/500*100)
# # print(l2)
# # percent={a:b for (a,b) in zip(l1,l2)}
# # print(percent)

# #strings
# # n="hi i'am ms"
# # print(n)
# # m='hi i\'am ms'
# # print(m)

# # print('a'<'b')
# # print(max('a','b','c'))

# # a=("electroNics ece")
# # print(a.upper())
# # print(a.lower())
# # print(a.capitalize())
# # print(a.casefold())
# # print(a.replace('s','z'))
# # print(a.strip())
# # print(a.split())
# # print(a.center(45,'*'))
# # print(a.count('e'))
# # print(a.count('e',5,len(a)))
# # print(a.endswith('e',0,len(a)))
# # print(a.find('N',0,len(a)))
# # print(a.islower())
# # print(a.isupper())

# # get an string as input along with a character find out and
# # display wheather the particular character is in the string or not

# # s1=input("enter a string")
# # s2=input("enter a character")
# # if s2 in s1:
# #     print("string contains:")
# # else:
# #     print("doesnot contains")

# # check wheather the given string is palindrome


# s2=input("enter a string")
# count=0
# if (len(s2)//2==0):
#     for i in range(len(s2)//2):
#         if s2[i]==s2[-(i+1)]:
#             count=+1
#         if count==len(s2)//2:
#             print(s2,"is a palindrome")
#         else:
#             print(s2,"is no a palindrome")
# else:
#     for j in range(len(s2)-1//2):
#         if s2[j]==s2[-(j+1)]:
#             count=+1
#         if count==len(s2)-1//2:
#             print("is a palindrome")
#         else:
#             print("is not palindrome")

        






# # after one string as input check if the given string cntains space or not 
# # if yes count no of spaces in the string
# # s3=input("enter a string")
# # count=0
# # for i in s3:
# #     if i==" ":
# #         count=+1
# # print(count)

# modules
# import math
# print(math.ceil(12.5))
# print(math.floor(12.5))
# print(math.sqrt(5))
# print(math.factorial(3))
# print(math.pow(2,3))
# print(math.fmod(10,3))
