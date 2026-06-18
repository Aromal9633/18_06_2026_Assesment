numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

numbers.append(60)
print("After append:", numbers)

numbers.insert(2, 25)
print("After insert:", numbers)

numbers.remove(40)
print("After remove:", numbers)

numbers.pop()
print("After pop:", numbers)

numbers.reverse()
print("After reverse:", numbers)

numbers.sort()
print("After sort:", numbers)

print("Length of list:", len(numbers))

if 30 in numbers:
    print("30 is present in the list")

print("Elements in list:")
for num in numbers:
    print(num)
