'''f=open("data.txt","w")# w is a access mode top write  #defaults is r #if r then not w and if w not r
#out=f.read()
#print(out)
out=f.write("vishhhh")
print(out)
f.close()
'''
'''with open ("data.txt","r+") as f:
    out =f.read()
    k=f.write(" lalalala")  

print(out)
'''
'''f=open("data.txt","r+")
for i in range(1,11):
        x=2*i
        y=str(x) + " "
        f.write(y)
        f.write("\n")

f=open("prime.txt","r+")
k=open("notprimme.txt","r+")
detective=0
for i in range(2,41):
        for j in range(2,i):
                if(i%j==0):
                        detective=detective+1
        if(detective==0):
            y=str(i)
            f.write(y)
        else:
            s=str(i)
            k.write(s)
               '''
'''f=open("data.txt","r+")
k=open("newdata.txt","r+")
def func( data):
    return ''.join(reversed(data))
out=f.readlines()
j=list(out)
out_map=map(func,j)
k.write(out_map)
next(out_map)
            '''
'''def func(x):
    with open("newdata.txt","a") as f:
        x.split()
        f.write(x)


with open("data.txt","r") as k:
    a=k.readlines()
    print(a)

out=list(map(func,a))
print(out)
'''

import csv
