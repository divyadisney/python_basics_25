import pickle
with open("my_products","rb") as new_file:
    readFile=pickle.load(new_file)
    print(readFile)