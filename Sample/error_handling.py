# ZeroDivisionError
# ValueError
# IndexError
# KeyError
# TypeError

a=1
b=0
c=[1,2,3,4,5]
try:
    print(a/b)
    # print(c[5])

except Exception as e:
      print(e)
      print("Zero can't be divided")
except IndexError:
     print("Index not found")
else:
     print("Executed in try block")
finally:
     print("Completed")

# raise


