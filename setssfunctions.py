#initialisation of sets
'''myset=set({})
print(type(myset))

#most basic set
set1={1,2,3,4,5}
print(set1)

set2=set(("vishakha"))
print(set2)

set1.add(60)
print(set1)

set1.discard(4)
print(set1)

set1.update([99,88,77])
print(set1)'''

'''myset1={1,2,3}
myset2={3,4,5}
myset3=myset1.union(myset2)
print(myset3)
myset3.intersection(myset2)
print(myset3)
myset3=myset1.difference(myset2)
myset3.symmetric_difference(myset2)
print(myset3)'''


'''myset6={1,2,3,4}
myset7={3,4}
print(myset7.issubset(myset6))'''



#functions
'''def  test():
    a=100
    print("hey",a)
test()

def func(x):
    print("hey",x)
func("naina")
func("ram")

def funct(num):
    for i in range(1,11):
        print(f"table of {num} is : ",num*i)
funct(4)'''

'''def functi(a,b,c):
    print("a : ",a,"b : ",b,"c : ",c)
functi(10,20,30)'''

'''def shadi(x):
    print("hey shadi vale amount is :",x)
    return(x+200,"saree")
    print("gold chain")
out=shadi(100)
print("out: ",out)'''

#if a number is a prime or not through prime
def func(num):
    for i in range (2,num):
        if(num%i==0):
            return "not prime"
    return " prime"
print(func(6))

def lcm(num,num2):
    if(num2>num):
        while(i<=num):
            if(num%i==0):
                num=num//i

        
            

    