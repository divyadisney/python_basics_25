# string methods


# upper()
# lower()
# capitalize()
# split()  
# partition() 
# strip()
# isupper()
# isaplha()
# isalnum()
# swapcase -- swap upper to lover and viceverse

# a="Python fullstack developer in vscode"
# b="Python fullstack developer - in in vscode"
# print(a.capitalize())
# print(a.upper())
# print(b.split("-"))
# print(b.partition("-"))
# print(a.isalnum())
# print(a.title())
# print(a.swapcase())
# print(b.count("in"))
# print(len(a))

# c=["1","2","3"]
# print("".join(c))


# list methods

# append, extend, insert, remove, pop    
# sorted 
# l=["Python", 3.11,50]
# l.append("Apple")
# l.extend("123")
# l.insert(1,"orange")
# l.remove("3")
# l.pop(2)
# l.reverse()
# l.index("orange")

# print(l)


# Set methods

# union intersection difference issubset issuperset add remove
# a={"anna",10,20,"bob",23}
# b={10,4,20}

# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))
# print(a.issubset(b))
# print(a.issuperset(b))
# a.add("kevin")
# print(a)
# a.remove(23)
# print(a)

# dict methods
# get update key pop popitem

d={'Name': 'Ram', 'Age': '19', 'Country': 'India'}
print(d.items())
print(d)
print(d.get("Name"))
print(d.get("Course"))
print(d.keys())
d.update({"Age":20})
print(d)
d.update({"Course":"Python"})
print(d)
d.pop("Age")
print(d)

