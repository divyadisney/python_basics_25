import pickle
items=[("Laptop",40000),("Mobile",30000),("Headset",2000)]
with open("my_products","wb") as my_file:
    pickle.dump(items,my_file)
    