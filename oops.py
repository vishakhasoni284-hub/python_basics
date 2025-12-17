'''class HouseBuilding :
    colour="white"
    price=50000

    def info(self): #this info is a instance method (object is also called instance)
        print("house has price",self.price,HouseBuilding.price)

vishakha_house=HouseBuilding()
print(vishakha_house.colour)

h2=HouseBuilding()
print(h2.colour , h2.price , HouseBuilding.colour)
#class variables can be accessed via class name and object name both
h2.price=60000
print(h2.price)
h1=HouseBuilding()
#object can change class varible for itself but it will only change for the object
HouseBuilding.price=70000
h3=HouseBuilding()
print(h3.price)
print(h2.price)#because we changed for h2 =60000
print(h1.price)


vish_house=HouseBuilding()
vish_house.info() #two times 70000 because we used self.price and HouseBilding.price'''

'''class student_detail:
    student_name=""
    student_fees=50000
    student_email="@email.com"

    def stuinfo(self):
        print("student name : ",self.student_name,
               "student id : ",self.student_email,
               "student_fees : ",self.student_fees)
        
vishakha=student_detail()
vishakha.student_name="vishakha"
vishakha.stuinfo()'''

'''class GharMera:
    def __init__(self):
        print("constructor calling",self)

h1=GharMera()
print(h1)

h2=GharMera()
print(h2)'''

'''class GharMera:
    def __init__(self,colur,price):
        self.colur=colur
        self.price=price

        print("constructor colour",colur)
        print("constructor price",price)

h1=GharMera("black",50000)
h2=GharMera("green",50000)'''

'''class countcount :
    count=0
    def __init__(self):
        countcount.count=countcount.count+1 #we will not use self here we will use class name 
        #to update class variable 
        #if we use self.count that is call through an onject ( as self is for objects)
        # it will only change for every object that means count =0 and for every object it will
        #only remain 1 because every time we create new object count will become 0 as 
        # class variable will not change
        print("count value")

h1=countcount()
print(h1.count)
h2=countcount()
print(h2.count)
h3=countcount()
print(h3.count)'''

#inheritence 

'''class Animal :
    def __init__(self,name):
        self.name=name
    def info (self):
        print("Animal name : ",self.name)
class Dog(Animal):
    def sound(self):
        print(self.name,"barks")

d=Dog("Buddy")
d.info()
d.sound()
'''
'''class A:
    num=300
    def infoa(self):
        print("A class has data",self.num)
class B(A):
    amount=500
    def infob(self):
        print("B class has ",self.amount,self.num)
        self.infoa()

b1=B()'''

'''class UberCustomer :
    company="UBER PRIVATE LIMITED"

    def __init__(self,name,wallet):
        self.name=name
        self.wallet=wallet

    def info(self):
        print("information of uber is : ",self.name ,",",self.wallet)

class UberDriver(UberCustomer):
    def __init__(self,name,wallet):#we can keep name as d name and wallet as dwallet as well does not
                                   #matter with the name of variable but for simplicity we keep same name
        super().__init__(name,wallet)
    def info2(self):
        super().info()
        

uc1=UberCustomer("naina",899)
uc1.info()
ud1=UberDriver("Driver abhi ",976)
print(ud1.company)
ud1.info2()'''

'''class A:
    var1="name"
class B(A):
    var2="abc"
class C(B):
    var3="xyz"
obj1=A()
print(obj1.var1)
#print(obj1.var2) will print error

obj2=B()
print(obj2.var1)
print(obj2.var2)
#print(obj1.var3) will print error

obj3=C()
print(obj3.var1)
print(obj3.var2)
print(obj3.var3)'''




# Parent Class: Animal
'''class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Animal name:", self.name)

# Child Class: Dog
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # Call parent constructor #parent constructor has a patameter "name"
        self.breed = breed

    def details(self):
        print(self.name, "is a", self.breed)

d = Dog("Buddy", "Golden Retriever")
d.info()      # Parent method
d.details()   # Child method
'''

'''class A:
    var1="name"
    def __init__(self):
        print("hello")
class B(A):
    def __init__(self):
        super().__init__()
    var2="abc"
class C(A):
    def __init__(self):
        super().__init__()
    var3="xyz"
obj1=A()
obj2=B()
obj3=C()'''

'''class A1 :
    name1="name1"
class A2 :
    name2="name2"
class A3(A1,A2) :
    name3="name3"

obj1=A3
print(obj1.name1)'''

#method overriding
'''class Home :
    def info(self):
        print(" white colour")
class UserHome :
    def info(self):
        print("yellow colour ")
uh1=UserHome()
uh1.info()# child class phale khud main function check karta phir parent class main jata hai'''

'''class RBI :
    def __init__ (self,interestrate):
        self.interestrate =interestrate

    def info (self):
        print("RBI interstest is : ",self.interestrate+5,"%")
class HDFC(RBI):
    def __init__(self, interestrate):
        super().__init__(interestrate)

    def info2(self):
        print("HDFC interest is : ",self.interestrate,"%")

obj1=HDFC(5)
obj1.info()
obj1.info2()
'''

class C :
    __salary =500

    @property
    def getinfo(self):
        return self.__salary
c1=C()
print(c1.getinfo)
