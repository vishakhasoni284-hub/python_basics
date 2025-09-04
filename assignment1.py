#ques 1
x=(int(input("Enter a number : ")))
if(x%2==0 ):
    print("even")
else:
    print("number is odd.")

#que2 
num1=(int(input("Enter three numbers : ")))
num2=(int(input()))
num3=(int(input()))

if(num1>num2):
 if(num1>num3):
  print( num1 ,"is greatest.")
 else:
  print(num3 ,"is the greatest.")
else:
 if(num2>num3):
  print(num2 ,"is greatest.")
 else:
  print(num3 , "is greatest.")

#que3
num=int(input("Enter a number : "))
if(num%4==0):
 print("A leap year.")
elif(num%400==0 and num%100 ==0):
 print("A leap year.")
else:
 print("Not a leap year.")


#que4
per=int(input("Enter you percentage : "))
if (per>=90):
    print("Grade A")
elif(per>=80):
    print("Grade B")
elif(per>=70):
    print("Grade C")
elif(per>=60):
    print("Grade E")
else:
    print("Child.")

#que5

#three ways 
#way1
ch='h'
if(ch=='a'or ch=='e'or ch=='i'or ch=='o'or ch=='u'):
    print("vowel")
else:
    print("consonant")

#way2
n='a'
if(n not in "aeiou"): #this means "a" in "a"
    print("consonant")
else:
    print("vowel")

#way3
ch='h'
if(ch!='a'or ch!='e'or ch!='i'or ch!='o'or ch!='u'):
    print("consonant")
else:
    print("vowel")

#Que6
n1=int(input("Enter two numbers : "))
n2=int(input())
ope=(input("Enter what operations from ' *, + , - , / ' do you want to perform: "))
if(ope=='*'):
    print(n1*n2)
elif(ope=='+'):
    print(n1+n2)
elif(ope=='-'):
    if(n1>n2):
      print(n1-n2)
    else:
      print(n2-n1)
else:
    print(n1/n2)

#que7
#to check if a number is positive , negative or zero
numb=int(input("Enter a number : "))
if(numb==0):
    print("Number is zero.")
elif(numb>0):
    print("Number is positive.")
else:
    print("Number is negative.")

#que8
#to check username and password\
uname=(input("Enter the username : "))
password=input("Enter the password : ")
if(uname=="admin"):
    if(password=="1234"):
        print("Login successfully.")
    else:
        print("Wrong password ,Login failed!")
else:
    print("Wrong username , Login failed!")

#que9
#to check if a triangle is valid or not
a=int(input("Enter three sides of a triangle : "))
b=int(input())
c=int(input())
if(a+b>c):
    print("Triangle is valid.")
elif(a+c>b):
    print("Triangle is valid.")
elif(c+b>a):
    print("Triangle is valid.")
else:
    print("Triangle is not valid.")

#que10
# Program to calculate Body Mass Index (BMI)

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

print("Your BMI is:", bmi)

if bmi < 18.5:
    print("You are Underweight")
elif bmi >= 18.5 and bmi < 24.9:
    print("You have Normal weight")
elif bmi >= 25 and bmi < 29.9:
    print("You are Overweight")
else:
    print("You are Obese")


#que11
#discount on a product
price=int(input("Enter MRP of the product : "))
if(price>1000):
    print("You get 10% ,discount on the product.")
    print("Updated price : " ,price-price/10)
elif(price<1000 and price>500):
    print("You get 5% , discount on the product.")
    print("Updated price : " ,price-price/20)
else:
    print("You do not get any discount on the product.")

#que12 
#name of the month and days , leap year for feb.
month= input("Enter name of the month : ")
if(month=="january" or month=="march" or month=="may" or month=="july" or month=="august"
   or month=="october" or month=="december"):
    print("This month has 31 days.")
elif(month=="february"):
    print("This month has 29 days.")
elif(month=="april" or month=="june" or month=="september" or month=="november"):
    print("This month has 30 days.")
else:
    print("No month exists with this name, check the spelling.")

#que13
#simple atm
balance=50000
task=input("Enter c to check balance : " \
"Enter a to add money :  " \
"Enter w to withdraw money : " )
if(task=="a"):
    addm=int(input("Enter money that you want to add : "))
    balance=balance+addm
    print("Your updated balance : ",balance)
elif(task=="w"):
    withdm=int(input("Enter money that you want to withdraw ; "))
    if(balance>withdm):
        balance=balance-withdm
        print("your updated balance is : ",balance)
    else:
        print("Insufficient balance")
elif (task=="c"):
    print("Your balance is : ",balance)
else:
    print("Enter correct character.")

#que14
# Age categorization 

age = int(input("Enter your age: "))

if age >= 0 and age <= 1:
    print("You are an Infant")
elif age >= 2 and age <= 4:
    print("You are a Toddler")
elif age >= 5 and age <= 12:
    print("You are a Child")
elif age >= 13 and age <= 19:
    print("You are a Teenager")
elif age >= 20 and age <= 59:
    print("You are an Adult")
elif age >= 60:
    print("You are a Senior")
else:
    print("Invalid age")

# Q15 
# Day of the week 

day = int(input("Enter a number (1-7): "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid number! Please enter between 1 and 7.")





