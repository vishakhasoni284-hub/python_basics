'''def func(x):
    return x+10
print(func(5))

a=lambda x: x+10
print(a(5))'''

'''def outer_func():
    def inner_func():
        print("inner hey")

    print("outer hey")
    return inner_func()
a=outer_func()
print("a : ",a)
'''
'''
out put :

outer hey
inner hey
a :  None

'''

'''def outer_func():
    def inner_func():
        print("inner hey")

    print("outer hey")
    return inner_func
a=outer_func()
print("a : ",a)'''

'''
output : 

outer hey
a :  <function outer_func.<locals>.inner_func at 0x000001455897A2A0>

'''