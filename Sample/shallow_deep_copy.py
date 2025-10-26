# a=[[1,2],[3,4],[3,4]]
# a_copy=a 
# a_copy[1][1]=24 
# print(a)
# print(a_copy)

import copy

a=[[1,2],[3,4],[3,4]]
list=copy.deepcopy(a)
list[1][1]=34
print(list)
print(a)

a=[[1,2],[3,4],[3,4]]
list=copy.copy(a)
list[1][1]=34
print(list)
print(a)

