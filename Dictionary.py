student={'name':'John','age':25,'courses':['Math','Compsci']}
#print(student['courses'])
#print(student.get('name'))

#Updated our dictio
student.update({'name':'Jane','age':26,'phone':'555-5555'})
#remove
del student['age']
#pop
age=student.pop('age')
#look to items of dict
print(student.items())
#look to value and key
for key in student.items():
	print(key,value)
