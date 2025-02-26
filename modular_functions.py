#Part 2: Functions & Modularity (10 Marks) Task 3: Writing Modular Python Code Create a Python script (modular_functions.py) that: Defines a function called calculate_area(shape, dimension1, dimension2=0), where: shape can be "circle", "rectangle", or "triangle". The function calculates and returns the area of the given shape. If shape is "circle", it uses dimension1 as the radius and calculates area using πr². If shape is "rectangle", it calculates area using length × width. If shape is "triangle", it calculates area using (1/2) × base × height. Calls the function multiple times to test different shapes and prints the results. Hint: Use math.pi for π in Python. GitHub Submission: Commit the script as modular_functions.py in the python_basics folder and push to GitHub.

import math
def calculate_area(shape, dimension1, dimension2=0):
    if shape == 'circle':
        area = math.pi * dimension1 ** 2
        return area
    elif shape == 'rectangle':
        area = dimension1 * dimension2
        return area 
    elif shape == 'triangle':
        area = 0.5 * dimension1 * dimension2
        return area
    else:
        return 'Invalid shape'


# user defined cases

while True:
    user_shape = input('Enter shape (circle, rectangle, or triangle): ').lower()
    if user_shape in ['circle', 'rectangle', 'triangle']:
        break
    else:
        print('Invalid shape. Please enter circle, rectangle, or triangle.')

while True:
    try:
        user_dimension1 = float(input('Enter dimension1: '))
        break
    except ValueError:
        print('Invalid input. Please enter a numeric value for dimension1.')

user_dimension2 = 0
if user_shape != 'circle':
    while True:
        try:
            user_dimension2 = float(input('Enter dimension2: '))
            break
        except ValueError:
            print('Invalid input. Please enter a numeric value for dimension2.')

area = calculate_area(user_shape, user_dimension1, user_dimension2)
print(f'Area of {user_shape}: {area}')

""" else:
    try:
        user_dimension1 = int(input('Enter dimension: '))
        user_dimension2 = 0
        if user_shape != 'circle':
            user_dimension2 = int(input('Enter second dimension: '))
    except ValueError:
        print('Invalid input. Please enter a number.') 
    else:
        area = calculate_area(user_shape, user_dimension1, user_dimension2)
        print(f'Area of {user_shape}: {area}')
 """
# test cases

""" print('Area of circle:', calculate_area('circle', 5, 0))
print('Area of rectangle:', calculate_area('rectangle', 5, 3))
print('Area of triangle:', calculate_area('triangle', 5, 3))
 """





