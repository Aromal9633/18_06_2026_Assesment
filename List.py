
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


