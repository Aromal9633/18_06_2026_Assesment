#Perform basic dictionary operations

dict={"name":"Aromal","Age":26,"Job":"IT"}
print(dict)

#Perform dictionary operations

dict1={"name":"Aromal","Place":"Trivandrum","Age":26}
print(dict1)
print(dict1["name"])
print(dict1["Age"])
print(dict1["Place"])
dict1["name"]="Aromal Rajesh"
dict1["job"]="IT"
print(dict1)

#Dictionary from Lists


keys = ["name", "age", "job"]
values = ["Aromal", 26, "IT"]

my_dict = {k: v for k, v in zip(keys, values)}
print(my_dict)


#Clear dictionaries


my_dict = {"name": "Aromal", "age": 26, "job": "IT"}
my_dict.clear()
print(my_dict)

#Merge two Python dictionaries into one

dict1={"name":"Aromal","Age":26}
dict2={"place":"Trivandrum","Native":"Kerala"}

dict1.update(dict2)
print(dict1)

#Delete a list of keys from a dictionary


my_dict = {"name": "Aromal", "age": 26, "job": "IT", "place": "Kerala"}

keys_to_remove = ["age", "place"]
for key in keys_to_remove:
    if key in my_dict:
        del my_dict[key]

print(my_dict)


#Rename key of a dictionary

my_dict = {"name": "Aromal", "age": 26, "job": "IT", "place": "Kerala"}

my_dict["fullname"]=my_dict.pop("name")

print(my_dict)

#Invert Dictionary

my_dict = {"a": 1, "b": 2, "c": 3}
inverted={}
for k,v in my_dict.items():
    inverted[v]=k
print(inverted)

#Access Nested Dictionary


students = {
    "s1": {"name": "Aromal", "age": 26, "place": "Trivandrum"},
    "s2": {"name": "John", "age": 24, "place": "Chennai"}
}

print(students["s1"]["name"])


#Print the value of key ‘history’ from nested dic

student={"name":"Aromal","Marks":{"comp":50,"history":60,"Chem":90}}
print("Marks obtained by student for history is:",student["Marks"]["history"])

#Initialize dictionary with default values

keys = ['a', 'b', 'c']
d = dict.fromkeys(keys, 0)
print(d)

d = {}
for k in ['a', 'b', 'c']:
    d[k] = 0

print(d)

#Delete a list of keys from a dictionary


d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
keys_to_remove = ['a', 'c']
for key in keys_to_remove:
    d.pop(key)
print("List after Deleting:",d)


#Check if a value exists in a dictionary


d = {'a': 1, 'b': 2, 'c': 3}

value_to_check = 2
if value_to_check in d.values():
    print("Exists")
else:
    print("Not exists")

#Rename key of a dictionary

d = {'a': 1, 'b': 2, 'c': 3}
d['d']=d.pop("a")
print(d)


#Get the key of a minimum value

d = {'a': 10, 'b': 5, 'c': 8}
min_key = min(d, key=d.get)
print(min_key)

#Sort Dictionary by Keys


dict1 = {"d": 3, "c": 5, "b": 1, "a": 2}
sorted_dict = dict(sorted(dict1.items()))
print(sorted_dict)


#Sort Dictionary by Values

d = {'a': 10, 'b': 5, 'c': 8}

sorted_dict = dict(sorted(d.items(), key=lambda item: item[1]))
print(sorted_dict)
