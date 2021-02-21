# Creating a empty set 
a = set()
print(type(a))


# Adding values to an empty set
a.add(4)
a.add(7)
a.add(6)
a.add(79)
a.add(40)
a.add(7) # Adding a value repeatedly does not changes a set
a.add(7)
a.add((2,5,69,100))

# Cannot add list or dictionary to set
# a.add([7,5,8,9])  # Trow an error  (This is list)
a.add((7,5,8,9))  # It runs properly ( This is Tuple)
# a.add({2:7})     # Trow an error  (This is Dictionari)
print(a)

print(len(a)) # Prints the length of this set 

# Removel of an item
a.remove((7, 5, 8,9))# Removes (7, 5, 8,9) frome the set a
a.remove(7) # Removes 7 frome the set a
print(a)


a.pop()
print(a)