#BEFORE BEGIN
# WORK THOSE BUILT IN FUNCTIONS ON PYTHON SHELL.
#ABS absolute value ----1----
a=abs(-7)
print(a)
abs(-7.01)
#ex
mylist=[1,2,3,-1,-2,-3]
# turn my list to positive numbers
mynewlist=[abs(i) for i in mylist]
print(mynewlist)
#ALL ----2----
a=all('hey') #return True
print(a)
all([False,0]) # return False.Even there is one False in list you get FALSE.
#basic idea,these two ex are same.basic idea If list is empty you can get TRUE so on second ex u get 'not empty' output.
if len(mylist) !=0:
	print('not empty')
if mylist:
	print('Not empty')  

listsame=[1,1,1]
listdiff=[1,2,3]
all([x == 1 for x in listsame])
# u get an output True because 1 in listsame
all([ x == 10 for x in listsame])
# u get an output False because 10 is not in list listsame.

#ANY ----3---Return True if any element of the iterable is true. If the iterable is empty, return False.
print(any([""]))
print(any(["",False,0]))
print(any(["",False,0,1]))
# check any one name is Joe
names=['John','Joe','James']
print(any([x == 'Joe' for x in names])) # U get an output True or False
a=[x == 'Joe' for x in names] # IF U DO NOT USE ANY U CAN GET AND OUTPUT FALSE TRUE FALSE CHECK ALL OF ELEMENTS IN LIST
print(a)
#DIFFERENCE BETWEEN ALL AND ANY
all([]) # U GET AN OUTPUT TRUE DICTIONARIES ETC THEY ARE ALL SAME RESULT
any([]) # U GET AN OUTPUT FALSE

# ASCII() # ---4---
ascii(1)
ascii('Hey')
ascii({})
#BIN ---5---Convert an integer number to a binary string prefixed with “0b”. 
bin(-4)
# It returns string.
#BOOL  # ---6---Return a Boolean value, i.e. one of True or False.
bool(1)
bool(0)
bool(1 == 2) 
#BREAKPOINT #breakpoint is related  to the debugger  
#when you want to break  a program and open up  the program in the middle of the program
for i in range(10):
	print('i=',i)

    if i == 5:
       breakpoint()

 # BYTEARRAY  --8--Return a new array of bytes
 bytes()
 bytearray()
 #STRING
 bytes('hey','UTF-8')
 #INTEGERS
 bytes(1)
 bytes(4)  
 #ITERABLES
 bytes([1,2,3])
 bytearray([1,2,3])
 y=bytearray([1,2,3])
 y.append(4)
 #ignore non ascii charecters Imagine PONCRRA is russian,u can ignore
 #non ascii character by ignore
 bytearray('POCCNRA','ascii','ignore')
#CALLABLE --9--Return True if the object argument appears callable, False
callable('Hey') # u get false.
# functions,classes,methods,instances are CALLABLE
#bools is class
hasattr(bool,'__call__') # U get True because it is class
#CHR Return the string representing a character whose Unicode code point is the integer i.
chr(0)
chr(1114112)

# @classmethod Transform a method into a class method.
def __init__(self,features):
	self.features=features
def __repr__(self):
	return f 'Car ({self.features})'

@classmethod
def truck(cls):
	return cls(['4x4','Big Tires'])
#COMPILE
x='5'
code=compile(" x == '5'",'','eval')
result=eval(code)
print(result)
# X equals to 5 so it evaluates to TRUE
#Complex #imaginary number
#takes two arguemnts real and imag
complex()
complex(1) # U get an output (1+0j
#DELATTR
#It does not work on dictionaries
#It works on classes
class Jeep:
	hp=300
	model='Wrangler'
print('Jeep',Jeep.__dict__)
delattr(Jeep,'hp')
print('Jeep after',Jeep.__dict__)
# delete hp from the jeep.
if not attr.startswith('__'):
   print(attr,'=',value)
delattr(x, 'foobar') is equivalent to del x.foobar.
# DEL METHODE IS MORE EFFICIENT THAN DELATTR

#DICT HOW TO CREATE A DICTIONARY
dict() # create an empty dictio
a=dict(a=1,b=2) # how to create an dictionary
b=dict(a=1,'b':{'c':5})
#mapping
#create an dictionary to existing dict
a=dict({'a':1,'b':2})
a=dict({'a':1,'b':2,c=3})

#Iterable
a=dict([('a',1),('b',2)])
a=dict([('a',1),('b',2),c=3])# If u want to add c for example.
#zip
zip(['a','b'],[1,2])
# we have a dict with iterable
a=dict(zip(['a','b'],[1,2]))
#add element to dict 
a=dict(zip(['a','b'],[1,2],c=3))
# DIR()Without arguments, return the list of names in the current local scope.
#DIVMOD()
divmod(10,2)
#  u get result (5,0).
#bölme işleminden kalan, o sayının  modu olur
print(10//4)
print(10%4)
# both of them are same.
#Enumerate Return an enumerate object # Her bir iteme sayi verir.
seasons=['Spring','Summer','Fall','Winter']
list(enumerate(seasons))
list(enumerate(seasons, start=1)) # Starts from 1
# U CAN CREATE A DICTIONARY ALSO
dict(enumerate(seasons))
for i,j in enumerate(['Canada','USA','USSR']):
	print(i,j)
# Start at 5
for i,j in enumerate(['Canada','USA','USSR'],5):
	print(i,j)

#EVAL(expression,globals=None,locals=None)
#Eval basics
eval("5 + -1")
eval("5 * -1")
#Eval with functions
eval('abs(-1)')
eval(print"print('hello world')")
# you can just give expressions to eval not statements
eval=('a=5')
# you get an error because you give statements here
eval=('5+25')
# you do not get an error because it is expression
#sonuc ureten bir ifade evale girebilir
#Exec()
# one mandatory argument and two optional arguments
#Exec fonksiyonu parametre olarak  statemens alabilir
exec=('a=5')
a=20 # Bir deger tanimladik.
exec('a=3') # artik bu ustteki a degeri 3 olur
# global isim alani yerine local yere gonderme
ia={}
exec('a=3',ia)
# Bu sayede global alandaki A degiskeni ayni kalirken ia'ya 3 atanir
#exec(object[,globals[,locals]])
exec('print(1)')
exec("print(max(10,1))")
exec("print(min(10,1)")
exec('def testFunc():print(min(10,1)')
testFunc()
exec("y=5")

exec("print(1)","__builtins__":None)
# you get  type error because with builins none we remove  built in function print
#so you can add it back
exec("print(1)","__builtins__":None,{"print ":print})

#FILTER
#filter(function,iterable)
#The filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.
ages=[0,0,5,17,18,24]
def myFunc(x):
	return x>= 18
print(list(filter(myFunc,ages)))	
ages=[0,0,5,17,18,24]
def myFunc(x):
	return x>= 18
print(list(filter(None,ages))) # U get as result 5,17,18,24 0 is false value
#FLOAT
#Return a floating point number constructed from a number or string x.
float(-1)
float('+1.23')
#Format
format(5,)
#Frozen set
#The frozenset() function returns an unchangeable frozenset object (which is like a set object, only unchangeable).
mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist)
print(x)
print(type(x))
x[0]='Horse'
print(x)
# Burada frozenset objesine donustu ve hicbir degisme islemi olmuyor itemler icin bu enson yazdigimizda hata alirsin
frozenset({'hey'})
# output olarak  frozenset({'y','e','h'}) alirsin
# we can not have set in another set but we can have frozenset
set([1,2,frozenset([5])])
#getattr() The getattr() function returns the value of the specified attribute from the specified object.
class Jeep:
	hp=300
	model='Land rover'
print(getattr(Jeep,'model'))

print(Jeep.hp) # this is another method
#GLOBALS()
#The globals() method returns the dictionary of the current global symbol table.
#A symbol table is a data structure maintained by a compiler which contains all necessary information about the program.
#These include variable names, methods, classes, etc.
a=5
b=5
# if  I run global() I will see that a and b are on global scope

#HASATTR()
#The hasattr() function returns True if the specified object has the specified attribute, otherwise False.
class Person:
  name = "John"
  age = 36
  country = "Norway"

x = hasattr(Person, 'age')
#HASH()
#Return the hash value of the object (if it has one). Hash values are integers. 
#They are used to quickly compare dictionary keys during a dictionary lookup. 
#Numeric values that compare equal have the same hash value (even if they are of different types, as is the case for 1 and 1.0).
# YOU CAN NOT PASS HASH FUNC TO DICT SET AND LIST
hash(6)
#Hash(set('6')),hash([]) u get an error.
#always returns int even you type STR
#HELP()
help(print)
#when u not define module 
help("Math")

#hex(x)
#Convert an integer number to a lowercase hexadecimal string prefixed with “0x”. 
#If x is not a Python int object, it has to define an __index__() method that returns an integer.
a=hex(255) # integer to hexedecimal STRING
prin(type(a)) # type=STRING
#u can write binary code also
bin(4) # binary code bulma
hex(0b100)
#format
format(25,'#X') #output 0X19
format(25,'X') # output 19
#ID()
#return the identity of  an object LOCATION IN MEMORY
id('test')
# Bir sayi aliriz bu Python hafizasindaki yeridir
a=5
b=5
a == b 
id(a),id(b) #  A ve B ayni hafizada cunku ikisinide 5 sayisina esitledik
# Listeler icin bu gecerli degildir
# listelerde Id numaralari farkli olacadir
#Sozlukler icinde bu olmayacadir. id rakamlari farkli olacadir.

#INT()
int(5.5)
type(int('5'))
int(5.6) # bu calisir
int('5.6') # bu calismaz
int('11111') # bu da calisir
# can take  binary numbers
bin(5)# learn bin number
int(0b101) # output 5 because this is binary code of 5
#secondary argument
int('10',10)

#ISINSTANCE()
#Return True if the object argument is an instance of the classinfo argument,
isinstance('hey',str) # STRING MI TRUE VEYA FALSE DEGERI ALIRSIN
isinstance('hey',int) # False alirsin cunku string
isinstance(['hey'],list) # true alirsin cunku list
# ORNEGIN ELINDEKI BIR VERININ DATANIN LIST MI DICT MU OLDUGUNU KONTROL EDECESIN
data={1:'hey'}
if isinstance(data,dict):
	print('is dict')
if isinstance(data,list):
	print('is list')

# yukarida data typin neyse onu verrir dictionary veya iste  list vs

#ISSUBCLASS(class,classinfo)
#return true if class is a subclass
class Car:
	pass
class Buggatti(Car):
    pass
 class(BuggatiVeyron)   	
print(issubclass(BuggattiVeyron,Car))

#ITER
#The iter() function returns an iterator object.
iter([1,2,3,4,5],mySentinel)
import random
def x ():
	return random.randrange(1,10)
a=iter(x,5)
While True:
     print a.next()
# it stops when function returns to 5
#fonksiyon 5 olana kadar 1 ile 10 arasinda sayilari basar.

#LOCALS()
#update and return a dictionary representing the current
#local symbol table
#we dont have local variables here
def demo1():
	print('here no local variables is present',locals())
# here we have local variables	
def demo2():
	namme='Ankit'
	print('Here local variables are present',locals())

#output1
#Here no local variable  is present :  {}
#Here local variables are present :  {'name': 'Ankit'}
#Unlike from globals() this function can not modify the data of local symbol table.
# here no local variable is present 
def demo1(): 
    print("Here no local variable  is present : ", locals()) 
      
# here local variables are present 
def demo2(): 
     name = "Ankit"
     print("Here local variables are present : ", locals()) 
     print("Before updating name is  : ", name) 
       
     # trying to change name value 
     locals()['name'] = "Sri Ram"
       
     print("after updating name is : ", name) 
# BURADA LOCALS NAME ISE YARAMAZ VE SRI SRAM OLMAZ.

def printnames():
   name='Brendan'
   print('Name',name)
   print(locals())
   print('globals()',globals())

printnames() 

#MAP(function,iter) 
#returns a map object after applying  function all item of iterator
def addition(n):
     return n+n
 # we double all numbers using map
 numbers=(1,2,3,4)
 result=map(addition,numbers)
 print(list(result))    
 #The returned value from map() (map object) 
 #then can be passed to functions like list() (to create a list), set() (to create a set) .   
def touppercase(s):
	return s.upper()
map_iterator=map(touupercase,"abc")
print(list(map_iterator))	

def combine_list(list1,list2):
	return list1+list2
result2=map(combine_list,[1,2,3,4],[111,222,333,4444])
print(list(result2))
#output 112,224,336,4448
#MAX()
 #printing the maximum of 4,12,43.3,19,100
print("Maximum of 4,12,43.3,19 and 100 is :",end=" ")
print (max( 4,12,43.3,19,100 ) )
max(1,2,3,4)
max([1,2,3,4],default=100)
# you take 4
max([],default=100)
#you take 100
max('apple','dog')
#output is dog. because ASCII NUMBER
#ord(a) is lower than ord(d)
max('apple','dog',key=len)
def digitsum(num):
    sum=0
    while(num):
        sum+=num%10
        num=int(num/10)
    return sum

print('Maximum is',max([100,321,59,40],key=digitsum))

#yukarida ki olayi liste kullanmadanda yapabilirsin

#Memoryview()
# allos us to access  the internal data of an object that supports
#the buffer protocol without copyting
a=b'hey'
type(a)
memoryview(a)
bytearray(b'hey')
b[0:1].tobytes()

#MIN()
#The min() function returns the item with the lowest value, 
#or the item with the lowest value in an iterable.
min([1,2,3,4])
min('coffee','tea')
#coffee alirsin ASCI'ye gore bir output verir.
#ord('c') asci'ye gore yeri 99
#ord('t') ascii'ye gore  yeri 116 bu yuzden coffee birinci verilir
min("coffee",'tea',key=len) 
#burada  istedigin sayiyi alirsin
min('c','T')
# burada Asci'ye gore T alirsin cunku T harfi kucuk c'den once gleir
min('c','T',key=str.lower)

#NEXT()
#The next() function returns the next item in an iterator.
#You can add a default return value, to return if the iterable has reached to its end.
a=iter(['python','is','great'])
#next(a) her next dediginde bir sonraki itemi alirsin
next(a,'End of Iterator')

#ord()
#The ord() function returns the number representing the unicode code of a specified character.
x=ord('h')
print(x)
ord('a') # you get a unicode of letter.
chr(87) # you get  'a'

#pow() 
#Return the value of 4 to the power of 3 (same as 4 * 4 * 4):
x=pow(4,3)
#Return the value of 4 to the power of 3, modulus 5 (same as (4 * 4 * 4) % 5):
x = pow(4, 3, 5)
#bu alttaki ikisi esit
(5**2)%12
pow(5,2,12)

pow(5,5)
pow(5,3)
pow(5,3,124)
pow(5,3,123)
pow(5,2.2)

#PRINT
#ornegin bir dosya var o dosyaya bir sey yazacasin
f=open('print_test.txt','w')
print('i hope this appear in my life',file=f)
f.close()
quit()
# open print_test.txt # dosyayi aciyur

#repr()
#The repr() function returns a printable representation of the given object.
#goal is __repr__ goal is ambiguos
#goal is __str__ goal is to be readable
str(3) == str('3')
from decimal import  Decimal
a=Decimal(1.25)
# print yaparsan decimal ('1.25')

str(a)
# '1.25'

import datetime
today=datetime.datetime.today()
#REVERSE
#Reverse the sequence of a list, and print each item:
 alph=["a",'b','c','d']
 ralph=reversed(alph)
 for x in ralph:
  print(x)

  my_list=[1,2,3,4,5]
  reversed(my_list)
# we are returning iterator not reversed itself
# If you want to do that  
list(reversed(my_list))
# if  you use strings you can use join syntax.
"".join(reversed('hey'))

#round()
#The round() function returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.
#round(number,ndigits)
round(1.5) # 2 alirsin yuvarliyor
round(2) # 2 alirsin
round(1.25252525) # 1 alirsin
round(1.252252525)
round(1.252525,1)
round(25252525,2)# YUVARLAR  AMA SAG TARAFTA 2 RAKAM CIKTISI ALIR
# SET
#create an empty set
a=set()
a={1,'hey',[1,2]} # YOU CAN NOT ADD MUTABLE OBJECTS TO SET
a=[1,2,3,3,3,3,3,3]
set(a)
# burada unique elemenlari elde edersin yalnizca 1,2,3 elde edersin
list(set(a))

b=['joe',"joe",'james']
set(b)
# SADECE UNIQUE VALUELARI ALIRSIN.
#ADD TO SET

a={1,2,3}
a.add(4)
a.remove(1)

b=frozenset({2,3,4})
b.add(5) # FROZENSETLERE EKLEYEMEZSIN.
#sets are unrodered.

#setattr()
#Change the value of the "age" property of the "person" object:
class Person:
  name='John'
  age=36
  country='Norway'

setattr(Person,'age',40)  
#yukariya bir attribute ekleyebilirsin
setattr(Person,'country','world')
print(Person.__dict__)
The delattr() function, to remove an attribute

The getattr() function, to get the value of an attribute

The hasattr() function, to check if an attribute exist

### SLICE()
b=slice(2)
### SORTED()
#return a new sorted list from the item in iterable
sorted('hey') # 'e,h,y ' ciktsi alirsin
a=["c",'b','a','C']
# Burada C birinci gelir cunku AScII'ye gore C harfi kucuk c"den ondedir.
# STRINGS ARE SORTED BY ASCII DEGERLERINE GORE OLUR
b=[1,5,3]
sorted(b)
#1,3,5 sonucunu alirsin
b=[1,5,3,-1,-10,0]
sorted(b)
#[-10,-1,0,1,3,5] sonucunu elde edersin
sorted(b,key=abs) # absoltue valueslara gore sorted oluyur
c=['hey','im','home]'
sorted(c)
# ALFABETIK siraya gore cikti alirsin
sorted(c,key=len) #bu ise karakter sayisina gore alirsin

sorted(c,reverse=True)

#STATICMETHOD DECORATOR
class Car:
  def my_instance_method(self):
    return 'my_instance_method',self

  @classmethod
  def my_class_method(cls):
    return 'my_class_method',cls

  @statifmethod
  def my_static_method():
    return 'my_static_method'


#STRING METHOD
#SUM() 

{1:'foo',2:'bar'}
print(sum(d))
a=([5,5,5],10)
print(a[0])

### super()
#function is used  to give acces to methods and properties  or parent
#or sibling class
#the super() function returns an object that represent  the parent class
class Parent:
def __init__(self,txt):
  self.message=txt
  self.new=True
def printmessage(self):
   print(self.message)

class Child(Parent):
  def __init__(self,txt):
     super().__init__(txt)

x=Child('Hello,and welcome')
x.printmessage()           

    