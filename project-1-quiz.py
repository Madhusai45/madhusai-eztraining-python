q1='''what is addition of 23 & 790
a.0
b.5
c.813
d.456'''

q2='''what is multiplication of 345*4556
a.1571820
b.1571805
c.1571827
d.1587182'''
q3='''what is subtraction of 23456 from 35688
a.12456
b.37887
c.39988
d.12232'''

q4='''what is biggest continent
a.asia
b.europe
c.australia
d.south america'''

questions={q1:"c",q2:"a",q3:"d",q4:"a"}
name=input("enter ur name:")
print("hello",name,"welcome to quiz")
score=0
for i in questions:
    print()
    print(i)
    skip=input("do you want to skip(yes/no):")
    if skip=="yes" :
        continue
    ans=input("enter your answer")
    if ans==questions[i]:
        print("wow ! u got it")
        score=score+1
        print("ur score is :",score)
    else:
        print("wrong answer")
        score=score-1
        print("ur score",score)
    skip2=input("do you want to quit (yes/n0):")
    if skip2=="yes":
        break
print("your total score is ",score)



