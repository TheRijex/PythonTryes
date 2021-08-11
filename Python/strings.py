first_name = "Jake"
print(first_name[2])
first_letters = first_name[:2]
last_letter = first_name[-1:]
print(last_letter)
print(first_letters)
new_first_name = first_letters + 'n' + last_letter
print(new_first_name)
greeting = "Hello!"
greeting = greeting[:5] +' '+ "Python!"
print(greeting)

#Multiplication
yummy = "Yum "
print(yummy * 5)
print(yummy.upper())
#upper/lower

long_string = "This is the long string"
print(long_string.split())
print(long_string.split('s'))
#hmm = long_string.split()
#print(type(hmm))