print('###########################################################')
print('--- Try / Except ---')
print('###########################################################')
""""
### Try/Except ###
THE MORE SPECIFIC THE ERROR WE CATCH IS, THE BETTER

"""
try:
    value = 10/0
    number = int(input('Enter a number '))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError as ve:
    print(ve)

print('###########################################################')
""""
### Reading files ###
THERE ARE LOADS OF MODES TO OPEN THE FILES, CHECK THE DOCUMENTATION OUT FOR MORE INFO
"""
print('###########################################################')
print('--- READING FILES ---')
print('###########################################################')

employee_file = open('employees.txt', 'r+')
print(employee_file.readable())
print(employee_file.readline())
# print(employee_file.readlines())
# print(employee_file.readlines()[0])
for employee in employee_file.readlines():
    print(employee)
employee_file.close()
print('###########################################################')
""""
### Writing files ###
We got the options a (add to the file), w(overwrite the file or create a new one)
"""
print('--- WRITING FILES ---')
print('###########################################################')
employee_file = open('employees.txt', 'a')
employee_file.write('\nRupali - Batch trainer')
employee_file.close()
""""
### Creating files ###
open a file with the option w
"""
print('###########################################################')
print('--- CREATING FILES FILES ---')
print('###########################################################')

employee_file = open('employees1.txt', 'w')
employee_file.write('Erica Ponce - Head of HR')
employee_file.close()

employee_file = open('index.html', 'w')
employee_file.write('<p>This is a html paragraph<p>')
employee_file.close()
print('###########################################################')

""""
### Modules and pip  ###
To import functionality from different files (Modules) - keyword IMPORT
"""
print('--- MODULES AND PIP ---')
print('###########################################################')

import math
print(math.pi) #using the module mat to print pi number
print('To know all of the available modules, visit: https://docs.python.org/3/py-modindex.html')
print('pip is gonna allow us to install external\n'
      '(third-party) modules to import them and use them\n'
      'you just need to use the command pip install <exter_library_name>\n'
      'on the command line'
      )
print('to uninstall a module, use the command uninstall <module_name>')
print('###########################################################')
print('###########################################################')
""""
### Classes and objects - see file (class) Student.py) ###
"""
print('--- CLASSES AND OBJECTS ---')
print('###########################################################')
from Student import Student
s1 = Student('Jim', 'Business', 3.1, False)
s2 = Student('Pa', 'Art', 2.5, True)
print(s1.name, s1.major, s1.gpa, s1.is_on_probation)
print(s2.name, s2.major, s2.gpa, s2.is_on_probation)
print('###########################################################')
""""
### Building a multiple choice quiz game ###
"""
print('--- BUILDING A MULTIPLE CHOICE QUIZ GAME---')
print('###########################################################')
from Question import Question
question_prompts =[
    'What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange',
    'What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow',
    'What color are strawberries?\n(a) yellow\n(b) Red\n(c) Blue'
]

questions = [
    Question(question_prompts[0], 'a'),
    Question(question_prompts[1], 'c'),
    Question(question_prompts[2], 'b')
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt+'\n')
        if answer == question.answer:
            score += 1
    print('You got ' + str(score) + '/' + str(len(questions)) + ' correct answers')
run_test(questions)
print('###########################################################')

""""
### Class/object function ###
Functions that we can use inside of a class an it can modify
information about an object or instance of such class
"""
print('--- CLASS/OBJECT FUNCTION ---')
print('###########################################################')
from Student import Student
s1 = Student('Jim', 'Business', 3.2, False)
s2 = Student('Pa', 'Art', 3.5, True)
print(s2.on_honor_roll())
print('###########################################################')

""""
### Inheritance ###
To reuse and extend or change functionality of one class in another class
"""
print('--- INHERITANCE ---')
print('###########################################################')

from Chef import Chef
from ChineseChef import ChineseChef
myChef = Chef()
myChef.make_special_dish()
myChineseChef = ChineseChef()
myChineseChef.make_special_dish()

print('###########################################################')
""""
### Python interpreter ###
To interact with python through a terminal or command line (in text mode)
it's like a terminal or command line which just accepts python commands
like print(), basic math operations, etc.
To use it. Just open you terminal or comand line and type python3
to get into the python mode
"""

print('###########################################################')

