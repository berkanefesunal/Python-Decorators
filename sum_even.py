
def odd_even(x):
    if x % 2 == 0:
        print('{} is even '.format(x))
    else:
        print('{} is odd'.format(x))    
    
number=int(input('Please enter a number.'))
print(odd_even(number))


