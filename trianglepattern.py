'''n=int(input("Enter a number: "))
for i in range (1,n+1):
    for j in range (1,n+1):
        if (j<=i):
            print(" *",end="")
        else:
            print("  ",end="")
    print()

n=int(input("Enter a number: "))
for i in range (1,n+1):
    for j in range (n,0,-1):
        if (j<=i):
            print("* ",end="")
        else:
            print("  ",end="")
    print()

n=int(input("Enter a number: "))
for i in range (n,0,-1):
    for j in range(1,n+1):
        if (j<=i):
            print(" *",end="")
        else:
            print("  ",end="")
    print()

n=int(input("Enter a number: "))
for i in range (n,0,-1):
    for j in range(n,0,-1):
        if (j<=i):
            print(" *",end="")
        else:
            print("  ",end="")
    print()'''
            
'''n=int(input("Enter a number: "))
for i in range (1,n+1):
    for j in range (n,0,-1):
        if (j<=i):
            print("* ",end="")
        else:
            print("  ",end="")
    print()'''


#assignment 
# pattern 1
'''n=int(input("Enter a number: "))
for i in range (1,n+1):
    for j in range (1,(2*n)):
        if (j>=i and j<=i+(n-1)):
            print(" *",end="")
        else:
            print("  ",end="")
    print()'''
# pattern 2 did not understand the pattern diagram


# pattern 3
'''n=int(input("Enter a number: "))
for i in range (1,n+1):
    temp='A'
    for j in range (1,n+1):
        if (j<=i):
            print(temp,end=" ")
        else:
            print("  ",end="")
        temp=chr(ord(temp)+1)
        
    print()'''

#pattern4
'''n=int(input("Enter a number: "))
temp='A'
for i in range (1,n+1):
    for j in range (1,n+1):
        if (j<=i):
            print(temp,end=" ")
        else:
            print("  ",end="")
    temp=chr(ord(temp)+1)
        
    print()'''

#pattern5
'''n=int(input("Enter a number: "))
temp=chr(ord('A')+n-1)
for i in range (1,n+1):
    temp2=temp
    for j in range (1,n+1):
        if (j<=i):
            print(temp2,end=" ")
        else:
            print("  ",end="")
        temp2=chr(ord(temp2)+1)
    temp=chr(ord(temp)-1)
        
    print()'''

#pattern 6 
'''n=int(input("Enter a number: "))
for i in range (1,n+1):
    for j in range (n,0,-1):
        if (j<=i):
            print("* ",end="")
        else:
            print("  ",end="")
    print()'''

#pattern 7
'''n=int(input("Enter a number: "))
for i in range (1,n+1):
    temp=1
    for j in range (n,0,-1):
        if (j<=i):
            print(temp,end=" ")
            temp=temp+1
        else:
            print("  ",end="")
    print()'''

#pattern8
#1.
'''n=int(input("Enter a number: "))
for i in range (n,0,-1):
    temp=1
    for j in range(n,0,-1):
        if (j<=i):
            print(temp,end=" ")
            temp=temp+1
        else:
            print("  ",end="")
    print()'''

#2.
'''n=int(input("Enter a number: "))
for i in range (n,0,-1):
    temp='A'
    for j in range(n,0,-1):
        if (j<=i):
            print(temp,end=" ")
            temp=chr(ord(temp)+1)
        else:
            print("  ",end="")
    print()'''

#pattern 9
'''n=int(input("Enter a number: "))
temp=n*2
for i in range (n,0,-1):
    for j in range (1,(2*n)):
        if (j>=i and j<temp):
            print("* ",end="")
        else:
            print("  ",end="")
    temp=temp-1
    print()'''

#pattern 10
'''n=int(input("Enter a number: "))
temp=n*2
for i in range (n,0,-1):
    temp2=1
    for j in range (1,(2*n)):
        if (j>=i and j<temp):
            print(temp2,end=" ")
            temp2=temp2+1
        else:
            print("  ",end="")
    temp=temp-1
    print()'''

#pattern11
'''n=int(input("Enter a number: "))
temp=n*2
for i in range (n,0,-1):
    temp2='A'
    for j in range (1,(2*n)):
        if (j>=i and j<temp):
            print(temp2,end=" ")
            temp2=chr(ord(temp2)+1)
        else:
            print("  ",end="")
    temp=temp-1
    print()'''

'''n=int(input("Enter a number: "))
for i in range (1,n+1):
    for j in range (1,n+1):
        if (j==1 or j==i or i==n):
            print(" *",end="")
        else:
            print("  ",end="")
    print()'''



'''n=int(input("Enter a number: "))
for i in range (1,n+1):
    for j in range (n,0,-1):
        if ( j<=i):
            print("* ",end="")
        else:
            print("  ",end="")

    for j in range (2,n+1):
        if ( j<=i):
            print("* ",end="")
    print()'''

'''
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
'''
'''n=int(input("Enter a number: "))


for i in range (1,n+1):
    for j in range (n,0,-1):
        if ( j==i or i==n):
            print("* ",end="")
        else:
            print("  ",end="")

    for j in range (2,n+1):
        if ( j==i or i==n):
            print("* ",end="")
        else:
            print("  ",end="")
    print()'''

'''
        *
      *   *
    *       *
  *           *
* * * * * * * * *
'''

'''n=int(input("Enter a number: "))
for i in range (n,0,-1):
    for j in range (1,n+1):
        if (j==1 or j==i or i==n):
            print(" *",end="")
        else:
            print("  ",end="")
    print()'''

'''
 * * * * *
 *     *
 *   *
 * *
 *
'''

'''n=int(input("Enter a number: "))
for i in range (n,0,-1):
    for j in range (n,0,-1):
        if ( j<=i):
            print("* ",end="")
        else:
            print("  ",end="")

    for j in range (2,n+1):
        if ( j<=i):
            print("* ",end="")
    print()'''

'''
* * * * * * * * * 
  * * * * * * *
    * * * * *
      * * *
        *
'''

'''n=int(input("Enter a number: "))
temp=1
for i in range (1,n+1):
    for j in range (n,0,-1):
        if ( j<=i):
            print(temp,end="    ")
            temp=temp+1
        else:
            print("   ",end=" ")
    temp=temp+1
    for j in range (2,n+1):
        if ( j<=i):
            print(temp,end="    ")
    print()'''

'''n1=int(input("Enter a odd number : "))
temp=1
spacee=n1//2
for i in range (1,n1+1):
    print(" "*spacee + "* "*temp,end=" ")
    if(i<((n1//2)+1)):
        temp=temp+1
    else:
        temp=temp-1                                                   
    print()'''

'''
    *  
    * *
    * * *
    * * * *
    * * *
    * *
    *
'''

'''n1=int(input("Enter a odd number : "))
spacee=n1//2
temp=1
for i in range (1,n1+1):
    print("  "*spacee + "* "*temp,end=" ")
    if(i<((n1//2)+1)):
        temp=temp+1
        spacee=spacee-1
    else:
        temp=temp-1 
        spacee=spacee+1
    print()'''
'''
      * 
    * *
  * * *
* * * *
  * * *
    * *
      *
'''

'''n1=int(input("Enter a odd number : "))
spacee=n1//2
temp=1
for i in range (1,n1+1):
    print("  "*spacee + "* "*temp,end=" ")
    if(i<((n1//2)+1)):
        temp=temp+2
        spacee=spacee-1
    else:
        temp=temp-2 
        spacee=spacee+1
    print()'''

'''
      *  
    * * *
  * * * * *
* * * * * * *
  * * * * *
    * * *
      *
'''
#'''pattern 17
'''n1=int(input("Enter a odd number : "))
spacee=n1//2
temp=1
num=1
for i in range (1,n1+1):
    print("  "*spacee)
    for j in range(temp):
        print(num,end=" ")
        num
    if(i<((n1//2)+1)):
        temp=temp+2
        spacee=spacee-1
    else:
        temp=temp-2 
        spacee=spacee+1
    print()'''

#pattern 19
'''num=int(input("Enter a number : "))
temp=(num-1)
temp2=1
for i in range (1,2*num):
    count=1
    if(i<=num):
        for j in range(1,num+i):
            if(j>temp):
                print(count,end=" ")
                count+=1
            else:
                print(" ",end=" ")
        print()
        temp=temp-1
    else:
        for j in range(1,(2*num)-temp2):
            if(j>temp2):
                print(count,end=" ")
                count=count+1
            else:
                print(" ",end=" ")
        temp2=temp2+1
        print()'''


#or alterative of this code 
'''num = int(input("Enter a number: "))

for i in range(1, 2*num):
    if i <= num:
        spaces = num - i
        nums = 2*i - 1
    else:
        spaces = i - num
        nums = 2*(2*num - i) - 1

    # print spaces
    print("  " * spaces, end="")

    # print numbers
    for j in range(1, nums+1):
        print(j, end=" ")
    print()
'''

#pattern 20 -- 1
'''n=int(input("Enter a number : "))
for i in range(1,2*n):
    if(i<=n):
        spacee=i-1
        num_print = 2*(n-i)+1
    else:
        spacee=(2*n-1)-i
        num_print=2*i-(2*n-1)
    print("  "*spacee,end=" ")
    
    count=1
    for j in range(1,num_print+1):
        print(count,end=" ")
        count=count+1
    print()'''

#pattern 20 --2
'''n=int(input("Enter a number : "))
for i in range(1,2*n):
    if(i<=n):
        spacee=i-1
        num_print = 2*(n-i)+1
    else:
        spacee=(2*n-1)-i
        num_print=2*i-(2*n-1)
    print("  "*spacee,end=" ")
    
    count='A'
    for j in range(1,num_print+1):
        print(count,end=" ")
        count=chr(ord(count)+1)
    print()'''

#pattern 18
# --half pyramid 
'''n=int(input("Enter a number: "))
for i in range(1,n+1):
    count=1
    for j in range(1,n+1):
        if(j<=i):
            print(count,end=" ")
        count=count+1
    print()'''

# --inverted half pyramid 
'''n=int(input("Enter a number: "))
for i in range(n,0,-1):
    count=1
    for j in range(1,n+1):
        if(j<=i):
            print(count,end=" ")
        count=count+1
    print()'''

#  -- hollow half pyramid 
'''n=int(input("Enter a number: "))
for i in range (1,n+1):
    temp=1
    for j in range (1,n+1):
        if (j==1 or j==i or i==n):
            print(temp,end=" ")
        else:
            print("  ",end="")
        temp=temp+1
    print()'''

# --full pyramid 

'''n1=int(input("Enter a odd number : "))
temp=1
for i in range (1,n1+1):
    print("* "*temp,end=" ")
    if(i<((n1//2)+1)):
        temp=temp+1
    else:
        temp=temp-1                                                   
    spacee=n1//2
    temp2=1
    print("  "*spacee + "* "*temp2,end=" ")
    if(i<((n1//2)+1)):
        temp2=temp2+1
        spacee=spacee-1
    else:range 
        temp2=temp2-1 
        spacee=spacee+1
    print()'''

'''numberr=int(input("Enter a number : "))
n8=numberr
for i in range(1,numberr+1):
    for j in range (1,numberr+1):
        if(i==1 or i == n8 or j == 1 or j ==n8):
            print(" *",end=" ")
        else:
            print("  ",end=" ")
    print()'''

'''nn=int(input("Enter a number : "))
for i in range(1,nn+1):
    for j in range (1,nn):
        if(j<=nn-i or i==nn):
            print("* ",end=" ")
        else:
            print("  ",end=" ")
        
    for j in range(1,nn-1):
        if(j>=i-1 or i==nn):
            print("* ",end=" ")
        else:
            print("  ",end=" ")
    print()'''

'''n=int(input('Enter an even number : '))
temp=0
temp2=(n//2)-1
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i<=n//2):
            if(j<=(n//2)-temp or j>=(n//2+1)+temp):
                print("* ",end=" ")
            else:
                print("  ",end=" ")
                
        else:
            if(j<=(n//2)-temp2 or j>=(n//2+1)+temp2):
                print("* ",end=" ")
            else:
                print("  ",end=" ")
            
    print()
    if(i<=n//2):
        temp=temp+1
    else:
        temp2=temp2-1'''
    
'''
*  *  *  *  *  *  *  *  
*  *  *        *  *  *
*  *              *  *
*                    *
*                    *
*  *              *  *
*  *  *        *  *  *
*  *  *  *  *  *  *  *
'''
'''n= int(input('Enter an odd number : '))
temp=n//2
temp2=0
for i in range (1,n+1):
    for j in range(1,n+2):
        if(i<=n//2):
            if(j<((n//2)+2)-temp or j>=((n//2)+2)+temp):
                print("* ",end=" ")
            else:
                print("  ",end=" ")
        elif(i==n//2+1):
            print("* ",end=" ")
        elif(i>n//2+1):
            if(j<=((n//2)+1)-temp2 or j>=((n//2)+2)+temp2):
                print("* ",end=" ")
            else:
                print("  ",end=" ")
    print()
    if(i<=n//2):
        temp=temp-1
    else:
        temp2=temp2+1
'''
'''
*                          *  
*  *                    *  *
*  *  *              *  *  *
*  *  *  *        *  *  *  *
*  *  *  *  *  *  *  *  *  *
*  *  *  *        *  *  *  *
*  *  *              *  *  *
*  *                    *  *
*                          *
'''


#pascles pattern
'''n=int(input("Enter a number "))
listt1=[]
temp=1
for i in range(0,n):
    listt2=[]
    for j in range(0,n-i-1):
        print(" ",end="")
    for k in range(0,i+1):
        if(k==0 or k==i):
            print(1,end=" ")
            listt2.append(1)
        else:
            x=listt1[i-1][k-1]+listt1[i-1][k]
            print(x,end=" ")
            listt2.append(x)
        
    listt1.append(listt2)
    print()
print(listt1)'''

n=int(input("enter a odd number : "))
check=n+1
check2=1
if(n%2!=0):
    for i in range(1,n+1):
        for j in range(1,n+2):
            if(i<=(n//2)+1):
                if(j<=i or j>=check):
                    print("* ",end=" ")
                else:
                    print("  ",end=" ")
                
    
            else:
                if(j<=(n+1)-i or j>=check2+i):
                    print("* ",end=" ")
                else:
                    print("  ",end=" ")
        if(i<=(n//2)+1):
            check=check-1
        else:
            check=check2+1     
        print()
        
else:
    print("enter an odd number.")

