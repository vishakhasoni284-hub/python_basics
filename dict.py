'''a=[3,5,7,11,16,27]
target =21
mydictionary={}
for i in range (0,len(a)):
    data=a[i]
    if(data not in mydictionary):
        mydictionary[data]=i
for x in mydictionary:
    val=mydictionary[x]
    if(target-x in mydictionary):
        print("we found the value : ",target-x ,":",mydictionary[target-x])'''


#counting the frequency of the numbers of list through dictionary 
'''lst = [2,3,2,5,3,3]
dicti={}
for i in lst:
    found=0
    for j in dicti:
        if(j==i):
            found=1
            dicti[i]=dicti[i]+1
            break
    if(found==0):
        dicti[i]=1
print(dicti)'''

#frequency of elemets 
'''lst = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
dicti={}
for i in lst:
    found=0
    for j in dicti:
        if(j==i):
            found=1
            dicti[i]=dicti[i]+1
            break
    if(found==0):
        dicti[i]=1
print(dicti)'''


#printing the same keys in two dictionaries in another dictionary 
'''dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'a': 10, 'b': 25, 'c': 30}
dict3={}
for i in dict1:
    for j in dict2:
        if i==j:
            if dict1[i]==dict2[j]:
                dict3.update({i:dict1[i]})
print(dict3)'''