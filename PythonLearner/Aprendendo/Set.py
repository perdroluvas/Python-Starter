# Create sets and what to do with them

# Create a set from a list
my_list = [1, 2, 3, 4, 5, 6, 3, 2, 1]
my_set = set(my_list)
print(my_set)  # {1, 2, 3, 4, 5, 6}

# Check if an element is in a set
if 4 in my_set:
    print("4 is in the set!")

# Add an element to a set
my_set.add(7)
print(my_set)  # {1, 2, 3, 4, 5, 6, 7}

# Remove an element from a set
my_set.discard(2)
print(my_set)  # {1, 3, 4, 5, 6, 7}

# Create a set from another set
my_set_2 = {8, 9, 10}
my_set_3 = my_set.union(my_set_2)
print(my_set_3)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Create a set from another set and check if an element is in it
if 9 in my_set_3:
    print("9 is in the set!")
