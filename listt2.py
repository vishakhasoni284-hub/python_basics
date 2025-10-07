# Q1 max number
'''numbers=[10,20,4,45,99]
maxx=0
for i in range(1,len(numbers)):
    if(numbers[i]>numbers[maxx]):
        max=numbers[i]
print(max)'''

# Q2 total of every element
'''numbers = [10, 20, 30, 40]
total=0
for i in range(0,len(numbers)):
    total=numbers[i]+total
print(total)'''


# Q3 reversing the list
'''numbers = [1, 2, 3, 4, 5]
rever=0
listt=[]
for i in range(len(numbers)-1,-1,-1):
    temmp=numbers[i]
    listt.append(temmp)
print(listt)'''

# Q4 sorting in ascending order without sort function
'''l=[9,5,2,1,4,6,7]
maxx=0
i=0
j=0
while(i<len(l)-1):
    j=j+1
    if(l[i]>l[j]):
        maxx=l[i]
        l[i]=l[j]
        l[j]=maxx
    if(j==len(l)-1):
        j=i
        i=i+1
print(l)'''

# Q5 remove duplicates 
'''numbers = [1, 2, 2, 3, 4, 4, 5]
i=0
duplicate=[]
unique=[]
while(i<len(numbers)):
    if numbers[i] not in unique :
        unique.append(numbers[i])
    else:
        duplicate.append(numbers[i])
    i=i+1
        
print(unique)
print(duplicate)'''

# Q6 program to find all pairs of numbers in a list that add up to a specific target sum.
'''l1 = [1, 2, 3, 4, 3, 5, 6]
i=0
j=0
l2=[]
while(i<len(l1)-1):
    j=j+1
    if(l1[i]+l1[j]==6):
        l2.append((l1[i],l1[j]))
    if(j==len(l1)-1):
        i=i+1
        j=i

print(l2)'''

#Q7 program to flatten the nested loop
'''nested_list = [1, [2, 3], [4, [5, 6], 7], 8]
flattened_list = []
for i in nested_list:
    if(type(i)==list):
       for j in i:
        if(type(j)==list):
           for k in j:
              flattened_list.append(k)
        else:
            flattened_list.append(j)
    else:
        flattened_list.append(i)
print(flattened_list)'''


# Q8 program to find the sum of the elements in a list, excluding the largest and smallest element.

'''l= [1, 2, 3, 4, 5]
smllest=l[0]# if I took element and not index then I have to assign elemets only
largest=l[0]
total=0
i=0
while(i<len(l)):
    if(l[i]>largest):
        largest=l[i]
    if(l[i]<smllest):
        smllest=l[i]
    total=total+l[i]
    i=i+1
new_total=total-(smllest+largest)
print(new_total)'''
   
# Q9 a Python program to check if a list is a palindrome
'''numbers = [1, 2, 3, 2, 1]
i=0
j=len(numbers)-1
detective=0
while(i<len(numbers)//2):
    if(numbers[i]!=numbers[j]):
        detective=detective+1
    i=i+1
    j=j-1
if(detective==0):
    print("its a palindrome")
else:
    print("not a palindrome")'''

