from math import *
""""
######Drawing a shape######
"""
print('###########################################################')
print("      /|")
print("     / | ")
print("    /  |")
print("   /   |")
print("  /    |")
print(" /_____|")
print('###########################################################')
"""
### Variables & datatypes ###
"""
print('###########################################################')
character_name = 'Tom' #python string
character_age = 50 #python integer
is_male = False #python boolean
print('There once a man named ' + character_name) #concatening
print('He was ' + str(character_age) + ' years old. ')
character_name = 'Mike'
print('He really liked the named ' + character_name)
print('But did not like being 70.')
print('###########################################################')
"""
Working with strings
"""
print('###########################################################')
phrase = 'Giraffe Academy'
print(phrase.lower()) #string to lowercase
print(phrase.upper()) #string to uppercase
print(phrase.isupper()) #to chec if string is uppercase
print(phrase.upper().isupper()) #string to uppercase and checking if it is uppercase
print(len(phrase)) #string length
print(phrase[0]) # string's first character
print(phrase.index('G')) #first index where 'G' is found if it doesn't find anything raise exception (to avoid exception use find instead)
print(phrase.find('X')) #X is not found in phrase, but it returns -1 instead exception (which is what index would do)
print(' ----------- ')
print(phrase.index("Acade"))#Index first character of word found (it return 8 (position of letter 'A' in phrase)
print(' ----------- ')
print(phrase.replace('Giraffe', 'Elephant')) # it replaces word Giraffe by Elephant in phrase
print('###########################################################')
"""
Working with numbers
"""
print('###########################################################')
my_num = 5 # python integer
print(my_num) #printing python integer
print(str(my_num)+ ' my favorite number') #to show an integer and a String together the integer has to be cast to string (str function)
print(abs(my_num)) #Absolute value of a number
print(pow(3, my_num)) #Power of a number (base, power)
print(max(my_num, 2)) #it returns the max
print(min(my_num, 2)) #it returns the min
print(round(2.7)) # round up
print(floor(2.7)) # round down
print(ceil(3.6)) # round up
print(sqrt(36)) #square root of a number
print('###########################################################')
"""
Getting input from users
"""
print('###########################################################')
name = input('Enter your name: ')
age = input('Enter your age: ')
print('hello '+ name + '!' + 'you are '+ age)


print('###########################################################')
"""
###Building a basic calculator###
"""
print('###########################################################')
num1 = input('Enter a number: ')
num2 = input('Enter another number: ')
result1 = int(num1) + int(num2)
print(result1)
result2 = float(num1) + int(num2)
print(result2)
print('###########################################################')

print('###########################################################')
"""
###Madlib games###
"""
print('###########################################################')
color = input('Enter a color: ')
plural_noun = input ('Enter a Plural Noun: ')
celebrity = input('Enter a celebrity: ')

print('Roses are: '+ color)
print(plural_noun + ' are blue')
print('I love '+ celebrity)
print('###########################################################')




