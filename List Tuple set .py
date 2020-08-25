

courses=["History","MAth","computer science",'algebra']
courses_2=['Art','education']

courses.insert(0,'Art') # istedigin indexe eklersin
courses.append('Biology') # listenin en sonuna ekler
courses.extend(courses_2) # Courses 2 listesinin elemanlari coursesa gider.
#Courses.append(courses_2) seklinde yazmak listeyi ekler elemanlarini eklemez
#print(courses)

#Remove something
courses=["History","MAth","computer science",'algebra']
courses.remove('MAth')
courses.pop() # this removes last item of the list.
#How to sort our lists
courses=["History","MAth","computer science",'algebra']
nums=[5,4,3,2]
courses.reverse()

courses.sort()#alphabetically sorted
nums.sort() # sorted by number.
#descending order sort
courses.sort(reverse=True)
nums.sort(reverse=True)
#Sorted method does not sort the list in place it returns sorted version of a list
courses=["History","Math","CompSci",'Algebra']
a=sorted(courses)
print(a)
#burada sorted ile olani yazdirsam return ayni olacak cunku sorted in place bir method degil
#dolayisiyla sorted methodunu bir degiskene atamam gerekiyor.
#Min MAX
nums=[1,2,5,3]
print(max(nums))
print(min(nums))
print(sum(nums))

#index
courses=["History","Math","CompSci",'Algebra']
print(courses.index('Art'))
print(courses.index[0])

# turn list to strings
course_str=','.join(courses)
print(course_str)

#lists are mutable
list_1=["History","Math","CompSci",'Algebra']
list_2=list_1

print(list_1)
print(list_2)
list_1[0]='Art'



#Sets
cs_courses={'History','Math','Physics','Computer science'}
print(cs_courses)
#it is used for membership tests.
print('Math'in cs_courses)
# we can do that with lists but sets are optimized for this
courses=["History","Math","CompSci",'Algebra']
art_courses={"history",'Math',"Art",'Design'}
#which courses are same ?
print(cs_courses.intersection(art_courses))
# which courses arent in art courses.
print(cs_courses.difference(art_courses))
#all of courses printed out as set
print(cs_courses.union(art_courses))

#HOW TO CREATE EMPTY LIST TUPLE Sets
#Empty lists
empty_list=[]
empty_list=list()

#empty tuples
empty_tuple=()
empty_tuple=tuple()

#empty sets
empty_set={}# this is a dictionary not set
empty_set=set()

