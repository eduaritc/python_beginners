print('###########################################################')
""""
### Building a better calculator ###
"""
# num1 = float(input('Enter first number: '))
# op = input('Enter operator number: ')
# num2 = float(input('Enter second number: '))
# if op == '+':
#     print(num1 + num2)
# elif op == '-':
#     print(num1 - num2)
# elif op == '*':
#     print(num1 * num2)
# elif op == '/':
#     print(num1 / num2)
# else:
#     print('Invalid operator')
print('###########################################################')

print('###########################################################')
""""
### Dictionaries ###
"""
months_conversion = {
    0:'January',
    1:'February',
    'Mar': 'March',
    'Apr': 'April'
}
print(months_conversion[0])
print(months_conversion.get(1))
print(months_conversion['Mar'])
print('###########################################################')

print('###########################################################')
""""
### While loop ###
"""
i = 1
while i <=10:
    print(i)
    i+=1
print('done with loop')
print('###########################################################')

print('###########################################################')
""""
### Buildin a guessing game ###
"""
# secret_word = 'giraffe'
# guess = ''
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False
# while guess != secret_word and not(out_of_guesses):
#     if guess_count < guess_limit:
#         guess = input('Enter a guess: ')
#         guess_count+=1
#     else:
#         out_of_guesses = True
# if out_of_guesses:
#     print('Out of guesses, You lose :(')
# else:
#     print('you win!')
print('###########################################################')
print('###########################################################')
"""
### For loops ###
"""
for letter in "Giraffe Academy":
    print(letter)
friends = ['Jim', 'Karen', 'Kevin']
for index in range(len(friends)):
    print(friends[index])
for index in range(5):
    if index == 0:
        print('First iteration')
    else:
        print('Not first')
print('###########################################################')
print('###########################################################')
"""
### Exponent function ###
"""
def raise_to_power(base, pow):
    result = 1
    for i in range(pow):
        result *= base
    return result
print(raise_to_power(2, 4))
print('###########################################################')
print('###########################################################')
"""
### 2D lists and nested loops ###
"""
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(number_grid[2][1])
#printing rows
for row in number_grid:
    print(row)
#printing cols
for row in number_grid:
    for col in row:
        print(col)
print('###########################################################')
print('###########################################################')
"""
### Building a translator ###
"""
def translate(phrase):
    translation = ''
    for letter in phrase:
        if letter.lower() in 'aeiou':
            if letter.isupper():
                translation = translation + 'G'
            else:
                translation = translation + 'g'
        else:
            translation = translation + letter
    return translation
print(translate(input('Enter a phrase: ')))
print('###########################################################')
print('###########################################################')
"""
### Building a translator ###
"""
#print('Comments are fun')
print('###########################################################')