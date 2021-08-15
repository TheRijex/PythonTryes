# print(1 + 1)
# print("1"+ "1")
# age = 23
# print('Jack is ' + str(age) + ' years old.')
# print('Jack is ' + str(23) + ' years old')
name = 'Ivan'
age = 27
name_age ='My name is {0}. I\'m {1} years old.'.format(name, age)
print(name_age)
name_age ='My name is {}. I\'m {} years old.'.format('Jack', '27')
print(name_age)
name_age ='My name is {}. I\'m {} years old.'.format("Viktoria", "24")
print(name_age)

float_result = 1000 / 7
print(float_result)
print(f'The result of division is {float_result:1.3f}')
x = int(input('Enter number'))
if x % 2 == 0:
    print('Even')
else:
    print('Odd')