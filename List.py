
#Basic List operations


lst = [10, 20, 30]

lst.append(40)
lst.insert(1, 15)
lst.remove(20)

for i in lst:
    print(i)



#Perform List Manipulation

lst = [10, 20, 30, 40, 50]

print("Original List:", lst)

lst.append(60)
print("After Append:", lst)

lst.insert(2, 25)
print("After Insert:", lst)

lst.remove(30)
print("After Remove:", lst)

lst.pop()
print("After Pop:", lst)

lst.reverse()
print("After Reverse:", lst)

lst.sort()
print("After Sort:", lst)

print("Length of List:", len(lst))

print("Elements in List:")
for i in lst:
    print(i)

#Sum and average of all numbers in a list

numbers=[1,2,3,4,5,6,7]
sum=0
for i in numbers:
    sum+=i
print("Sum is ",sum)

average=sum/len(numbers)
print("Average is :",average)

#Reverse a list

list1=[1,2,3,4,5,6]
print("Reverse of the list1",list1[::-1])

#Turn every item of a list into its square

list1=[2,4,6,8,10]
square=[]
for i in list1:
    square.append(i*i)
print("List Item Square",square)

#Find Maximum and Minimum

list1=[2,3,4,5,6,7,8,9,10,11,12,13]
print("maximun is :",max(list1))
print("Minimum is :",min(list1))



#Count Occurrences

count_num=[2,3,4,5,3,4,5,6,3,2,3,4,5]
print(count_num.count(3))

#Sort a list of numbers

sort_num=[3,4,5,2,1,6,8,9,0,3,10]
sort_num.sort()
print(sort_num)

#Create a copy of a list

name=["Apple","Orange","Mango"]
copy_main=[]
for i in name:
    copy_main.append(i)
print("Copy Of the List ",copy_main)

#Combine two lists

list1=[2,4,6,8]
list2=[1,3,6,9]
combine=list1+list2
print(combine)

#Remove empty strings from the list of strings

str=["a","b","c","","d"]
#print(str)
empty=[]
for i in str:
    if i!="":
        empty.append(i)
print("Final output after removing empty:",empty)

#Remove Duplicates from list

items=['a','b','c','d','a','b']
dup=[]
for i in items:
    if i not in dup:
        dup.append(i)
print(dup)

#Remove all occurrences of a specific item from a list

items=[1,2,3,4,2,5,2,6,2,7,2,8,2]
while 2 in items:
    items.remove(2)
print("After removing specefic items:",items)


#List Comprehension for Numbers

num1 = [1, 2, 3, 4]
num2 = 5
comp = [num2 + i for i in num1]
print(comp)




#Access Nested Lists

list1=[[1,2,3],[4,5,6],[7,8,9]]

print(list1[0])
print(list1[1])
print(list1[2])
print(list1[0][1])

#Concatenate two lists index-wise

list1=[1,2,3,4,5,6]
list2=[10,11,12,13,14]

concat=list1[0]+list2[1]
print(f"Output is {list1[0]} + {list2[1]} ={concat}")

#Concatenate two lists in the following order

list1=[1,2,3,4]
list2=[5,6,7,8]

concat=list1+list2
print("Concatinated output is",concat)

#Iterate both lists simultaneously


first = [1, 2, 3, 4, 5]
second = [2, 3, 5, 6]
for a, b in zip(first, second):
    print(a, b)

#Add new item to list after a specified item

list1=["aromal","athul","amritha"]
index=list1.index("aromal")
list1.insert(index+1,"hpriya")
print(list1)

#Extend nested list by adding the sublist

list=[[1,2,3],[3,5,6]]
sublist=[9,10,11]

list.append(sublist)
print(list)

#Replace list’s item with new value if found


old_list = ["apple", "orange", "banana"]
for i in range(len(old_list)):
    if old_list[i] == "orange":
        old_list[i] = "grapes"

print(old_list)




     








