a = [1, 2, "jeff", 4, 5, 6, 7]
print(a)
# to print an element in a list(they are zero indexed)
print(a[4])
# to access list from behind
print("accessed from behind", a[-3])
print(len(a))
# access first a certain position
print(a[1:3])
print(a[1::2])
# to edit a value in the list a
a[0] = "new"
print(a)
# to append / add a new value to a list
a.append(3.5)
print(a)
# to add a new value at a specific index
a.insert(0, "newer")
print(a)
# to delete a value specified inside brackets
a.remove("jeff")
print(a)
# to get length / no of objects  of a list
print(len(a))
# to count occurrences of a value in a list
print(a.count("new"))
