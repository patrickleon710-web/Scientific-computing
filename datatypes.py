# Part 1: Understanding Python Basics (10 Marks) Task 1: Python Data Types in Action Write a Python script (datatypes.py) that: Creates at least one variable of each data type: int, float, complex, list, tuple, dict, set, and bool. Prints the type of each variable using Python’s built-in type() function. Converts the integer variable to a float and vice versa, printing the results. Hint: Use int(), float(), complex(), and type() functions. GitHub Submission: Commit the script as datatypes.py in a folder named python_basics in your local Git repository. Push the changes to your GitHub remote repository.

age = 20
height = 164.5
complex_num = 5 + 3j
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_set = {1, 2, 3, 4, 5}
bool_num = True

print(my_list)

print('Age is type:', type(age))
print('Height is type:', type(height))
print('Complex_num is type:', type(complex_num))
print('My_list is type:', type(my_list))
print('My_tuple is type:', type(my_tuple))
print('My_dict is type:', type(my_dict))
print('My_set is type:', type(my_set))
print('Bool_num is type:', type(bool_num))

float_age = float(age)
int_height = int(height)
print(f'New age({float_age}) is of type:', type(float_age))
print(f'New height({int_height}) is of type:', type(int_height))