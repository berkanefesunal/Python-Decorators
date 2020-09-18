
#list with mixed data types
my_list=[1,'Hello',3.4]
#nested list
my_list=['Mouse',[8,4,6],['q']]
#INDEXING
my_list = ['p', 'r', 'o', 'b', 'e']
print(my_list[0])
#indexing nested list
my_list=['Mouse',[8,4,6],['q']]
print(my_list[0][1])
print(my_list[1][0])
#NEGATIVE INDEXINNG
# Negative indexing in lists
my_list = ['p','r','o','b','e']

print(my_list[-1])

print(my_list[-5])
#SLICE LIST
my_list = ['p','r','o','g','r','a','m','i','z']
print(my_list[::])
#reverse
print(my_list[::-1])
#We can add one item to a list using the append() method or add several items using extend() method.
# Appending and Extending lists in Python
odd = [1, 3, 5]

odd.append(7)

print(odd)

odd.extend([9, 11, 13])

print(odd)
# + operator to combine two lists
# Concatenating and repeating lists
odd = [1, 3, 5]

print(odd + [9, 7, 5]) ## odd=[1,3,5,9,7,5]
#INSERT() SPESIFIK BIR YERE ELEMAN EKLEMEK ISTEDIGINDE
# Demonstration of list insert() method
odd = [1, 9]
odd.insert(1,3)

print(odd)
#DELETE IN LISTS
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

# delete one item
del my_list[2]

print(my_list)

# delete multiple items
del my_list[1:5]

print(my_list)

# delete entire list
del my_list

#REMOVE() &  POP() 
#We can use remove() method to remove the given item 
#pop() method to remove an item at the given index.
my_list = ['p','r','o','b','l','e','m']
my_list.remove('p')
print(my_list.pop(1))
#method to empty list.
my_list.clear()
Python List Methods
append() - Add an element to the end of the list
extend() - Add all elements of a list to the another list
insert() - Insert an item at the defined index
remove() - Removes an item from the list
pop() - Removes and returns an element at the given index
clear() - Removes all items from the list
index() - Returns the index of the first matched item
count() - Returns the count of the number of items passed as an argument
sort() - Sort items in a list in ascending order
reverse() - Reverse the order of items in the list
copy() - Returns a shallow copy of the list




