# ZeroDivisionError
# ValueError
# IndexError
# KeyError
# TypeError

a=1
b=0
c=[1,2,3,4,5]
d=int(r)
try:
#     print(a/b)
    print(a)

except ZeroDivisionError as e:
      print(e)
      print("Zero can't be divided")
except IndexError as e:
     print(e)
     print("Index not found")
except Exception as e:
     print(f"An unexpected error occured {e}")
else:
     print("Executed in try block")
finally:
     print("Completed")

# raise


