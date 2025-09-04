#questions using for loop

#to print all natural numbers till n 
num=int(input("Enter a number : "))
for i in range (1,num+1):
    print(i)


#to print all natural numbers in reverse order
num1=int(input("Enter a number : "))
for i in range (num1,0,-1):
    print(i)

#to print the character from a to z 
a=ord('a')
z=ord('z')
for i in range (a,z+1):
    print(chr(i))

#all even numbers till 100
for i in range (1,101):
    if (i%2==0):
        print(i)

#sum of all odd numbers till n
n=int(input("Enter a number : "))
for i in range (1,n+1):
    if(i%2!=0):
        print(i)

#the counting of the digits of the number  
numb=(input("Enter a number : "))
count =0
for i in numb:
  count=count+1
print("The digits in the number : ",count)

#the sum of the digits 
num4=(input("Enter a number : "))
sum =0
for i in num4:
  sum=sum+int(i)
print("The sum of digits of the number : ",sum)



