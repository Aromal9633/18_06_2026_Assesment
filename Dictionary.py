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

