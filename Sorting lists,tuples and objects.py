li=[9,1,8,2,7,3,6,4,5]
s_li=sorted(li)

print('sorted variable:\t',s_li)
print('Original variable:\t',li)
# If you want to sort elements without creating a new element
li.sort() # Orjinal liste sortlanir.
#Sorted functions returns a new sorted list
# but sort method just sort and returns none
#descend order HIGER TO LOWER 
s_li=sorted(li,reverse=True)

#tuple
#tuple has no sort method
# you can use sorted function
tup=(9,1,8,2,7,3,6,4,5)
s_tup=sorted(tup)
print('Tuple\t',s_tup)
#DICTIONARY
di={'name':'Corey','job':'programming','age':None,'os':'Mac'}
s_di=sorted(di)
print('Dict\t',s_di)

#SORTING BASED ABSOLUTE VALUE KEY PARAMETER
li=[-6,-5,-4,1,2,3]
s_li=sorted(li,key=abs) 
print(s_li)

class Employee():
	def __init__(self,name,age,salary):
		self.name=name
		self.age=age
		self.salary=salary
	def __repr__(self):
		return '({},{},${})'.format(self.name,self.age,self.salary)

e1=Employee('Carl',37,70000)
e2=Employee('Sarah',29,80000)
e3=Employee('John',43,90000)
employees=[e1,e2,e3]
def e_sort(emp):
	return emp.name
s_employees=sorted(employees,key=e_sort)
# burada  e_sort olarak tanimladigimiz fonksiyon isimlerini geri dondurdu
# daha sonrasinda bu fonksiyonu key ile beraber kullanarak 
#sorted fonksiyonuyla isimlerin sorted bir sekilde geri donmesini sagladik
#yine belirtelim sorted fonksiyon sort ise methottur
# burada eger yukaridaki fonksiyonu 'age olarak degistirirsem 
def e_sort(emp):
	return emp.age       # bu fonksiyonun sorted ile kullanimi bana yas acisindan sorted seklinde geri verilir
s_employees=sorted(employees,key=e_sort,reverse=True) # Reverse true ifadesi descending order seklinde  cikti almami saglar
#yani yukaridan asagiya dogru azalan

#LAMBDA
#Yukarida kullanmis oldugumuz fonksiyon e_sort bunu yazmak yerine lambda ile cok rahat kullanarak bunu yazabilirsin
s_employees=sorted(employees,key=lambda e:e.name)

#yukaridakilerin yani sira asagidaki modulu cagirip su sekilde de yazabilirsin
from operator import attrgatter 
s_employees=sorted(employees,key=attrgatter('age'))





