# 1st
# li=[1,4,7,5,6,8]
# print(li[3])
# print(li[4])
# print(li[1:3])
# print(li[-1])
# print(li[:-1])
# print(len(li))
# print(li.count(4))
# li.append(500)
# print(li)
# li.sort()
# print(li)
# li.remove(6)
# print(li)
# li.extend([2,0,4,6])
# print(li)
# li.sort()
# print(li)
# li.reverse(8)
#create a list 10 elements.print one by one
#crea a li  with 5 first nums.fin the sum and avg
#create a list 


#2st
# l1=[1,2,6,8,0,3,5,97,89,69]
# for i in l1:
#     print(i)

# 3rd
# l2=[1.4,2.5,3.5,4.5,6.8]
# sum=l2[0]+l2[1]+l2[2]+l2[3]+l2[4]
# print("sum is:",sum)
# avg=sum%len(l2)
# print("average is :",avg)

#4th
# l4=list(map(int,input("enter six digits"),split()))
# for i in range(l4):
#     if(i%2==0):
#         print(i)

#5th
# l5=list(map(int,input("enter numbers:").split()))
# prod=1
# sum=0
# for i in range(len(l5)):
#     sum+=l5[i]
#     prod*=l5[i]
# if prod<750:
#     print("product",prod)
# else:
#     print("sum",sum)
    
#6th for elements
# numbers=[elements for elements in "pragati college"]
# print(numbers)

# #7th
# l=["And","Or","Not","That"]
# city=[]
# for n in l:
#     if "T" in n:
#         city.append(n)
# print(city)

#8th
# l6=[2**x for x in range(2,20)]
# print(l6)

# #9th
# l7=[a for a in range(10,101,10)]
# print(l7)

# #10th
# s={1,2,3,4,6}
# print(s)
# s.add(5)
# print(s)
# s.remove(6)
# print(s)
# s.update([8,9])
# print(s)
# s.remove(9)
# print(s)
# s.discard(8)
# print(s)

# #11th
# s2={1,2,3,4,5}
# s3={6,7,8,9,0}
# print(s2 | s3)
# print(s2 & s3)
# print(s2-s3)
# print(s3-s2)

# #12th
# s4={1,2,3}
# s5={1,3,5,7,2}
# print(s5.issuperset(s4))
# print(s4^s5) #symmetric difference
# print(s4.symmetric_difference(s5))

# t=(11,3,5)
# print(type(t))

d={1:"a",2:"b"}
d.setdefault(3,"d")
print(d)
print(type(d))