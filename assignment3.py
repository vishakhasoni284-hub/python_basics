#program to print all natural numbers from 1 to n.
'''n=int(input("Enter a number : "))
i=1
while(i<=n):
    print(i)
    i+=1'''

#a program to print all natural numbers in reverse (from n to 1). 
'''numb=int(input("Enter a number : "))
while(numb>0):
    print(numb)
    numb-=1'''

#a program to print all alphabets from a to z.
'''a=ord('a')
z=ord('z')
while(a<=z):
    print(chr(a))
    a+=1'''

#a program to print all even numbers between 1 to 100.
'''evenum=1
print("Even numbers from 1 to 100: ")
while(evenum<=100):
    if(evenum%2==0):
        print(evenum)
    evenum+=1'''

#a program to find the sum of all odd numbers between 1 to n.
'''odddsum=1
sum=0
number=int(input("Enter a number : "))
while(odddsum<=number):
    if(odddsum%2!=0):
        sum=odddsum+sum
    odddsum+=1
print("Sum of all odd numbers from 1 to ",number," : ",sum)'''

#a program to count the number of digits in a number.
'''number2=int(input("Enter a number : "))
count=0
digit=0
while(number2>0):
    digit=number2%10
    number2=number2//10
    count+=1
print("Number of the digits in the given number : ",count)'''

#a program to calculate the sum of digits of a number.
'''number3=int(input("Enter a number : "))
sum=0
digit=0
while(number3>0):
    digit=number3%10
    number3=number3//10
    sum=sum+digit
print("sum of the digits in the given number : ",sum)'''

#a program to find the first and last digit of a number.
'''number4=int(input("Enter the number : "))
count2=0
digits2=0
while(number4>0):
    digits2=number4%10
    number4=number4//10
    count2+=1 
    if(count2==1):
        n1=digits2
    elif(digits2<10):
        n2=digits2
print("The first digit of the number : ",n2)
print("The last digit of the of the number : ",n1)'''

#a program to find the sum of first and last digit of a number.
'''number5=int(input("Enter the number : "))
count3=0
digits3=0
while(number5>0):
    digits3=number5%10
    number5=number5//10
    count3+=1 
    if(count3==1):
        n3=digits3
    elif(digits3<10):
        n4=digits3
sum=n3+n4
print("The sum of first digit = ",n4,"and last digit = ",n3," is : ",sum)'''

#a program to reverse the number 
'''number5=int(input("Enter a number : "))
anothernum=number5 #atoring in a new number
count4=0
digit4=0
while(number5>0):
    digit4=number5%10
    number5=number5//10
    count4=count4+1 
reversenum=0
while(anothernum>0):
   x=anothernum%10
   reversenum=x*(10**(count4-1))+reversenum
   anothernum=anothernum//10
   count4=count4-1
print("The reversed number is : ",reversenum)'''
       
    
