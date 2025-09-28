
List=[1,2,3,4,9,"aaa"]
L=[]
for i in List:
    print(i)
    L=i
print("\n\n")
# List=["apple","orange","avacado","apricot"]
# print(List)
# print(List[0])
# for i in List: 
#    if i[0]=="a":
#       print(i)

List=["apple","orange","Avacado","apricot","pineapple","banana"]
new_list=[]
for i in List:
    #  if("a","e","i","o","u" in i[0]):
    if i[0] in "aeiou":
      new_list.append(i)
print(new_list)

print()
# count of letters in a word
a=input("enter a word: ")
