#Perform Basic Set Operations

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1)
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))


#Union of Sets

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2))

#Intersection of Sets

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.intersection(set2))

#Difference of Sets

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.difference(set2))
print(set2.difference(set1))

#Find Common Elements in Two Lists

set1=[1,2,3,4,5]
set2=[2,3,8,1,9]
common_sets=set(set1 ) & set(set2)
print("Common elements in th List is:",common_sets)


#Count Unique Words

words1="Welcome to Python Training Python first day"
count=words1.split()
unique1=set(count)
uni_list=len(unique1)

print(unique1)
print("count of unique words are:",uni_list)

#Set Intersection Update


set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.intersection(set2))
set1.intersection_update(set2)
print(set1)

#Set Difference Update


s = {1, 2, 3, 4, 5}
remove_items = {2, 4}
s.difference_update(remove_items)
print(s)


