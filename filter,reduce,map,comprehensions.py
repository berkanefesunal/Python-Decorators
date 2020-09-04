k=lambda x: x**2
print(k(2))

# two parameters
lambda x,y:x+y
#find max value
mx=lambda x,y:x if x>y else y
print(mx(8,5))

#MAP
# BIr liste elemanlarina belirledigin bir degeri uygular
n=[4,3,2,1]
print(list(map(lambda x: x**2,n)))
# we don't need to use lambda function instead we can write like
#print(list(map(square,n)))
p=[1,2,3,4]
print([x**2 for x in n ])

# filter
n=[4,3,2,1]
print(list(filter(lambda x:x>2, n)))

#reduce
n=[4,3,2,1]
#print(reduce(lambda x,y:x*y,n))

# COMPREHENSIONS
nums=[1,2,3,4,5,6,7,8,9,10]
my_list=[n*n for n in nums]
print(my_list)

my_list=[n for n in nums  if n%2== 0]
my_list=filter(lambda x: n % 2=0,nums)
#I want a (letter,num) pair for each  letter in 'abcd ' and each number 'abcd'
#my list=[]
#for letter in 'abcd':
	#for num in range(4):
		#my_list.append((letter,num))
	#print(my_list)	

# alternative way
my_list=[(letter,num) for letter in 'abcd' for num in range(4)]
print (my_list)
#Dictionary Comprehensions
names=['Bruce','Clark','Peter','Logan','Wade']
heros=['Batman','Superman','Spiderman','Wolverine','deadpool']
print zip(names,heros)
#I want a dict {'name':'hero'} for each name hero in zip (names,heros)
my_dict={}
for name,hero in zip(names,heros):
	my_dict[name]=hero
print(my_dict)	

#alternative way
my_dict={name:hero for name,hero in zip(names,heros)}
# I do not want peter in list
y_dict={name:hero for name,hero in zip(names,heros) if name != 'Peter'}

#SET COMPREHENSIONS
my_set=set()
for n in nums:
	my_set.add(n)
print(my_set)

#alternative
my_set={n for n in nums}
print(my_set)

#Generator expressions
nums=[1,2,3,4,5,6,7,8,9,10]
def gen_func(nums):
	for n in nums:
		yield n*n
my_gen=gen_func(nums)

my_gen=(n*n for n in nums)
print(my_gen)		

