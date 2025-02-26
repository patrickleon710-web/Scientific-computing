#    2: Python Control Structures Challenge Create a Python script (control_structures.py) that: Asks the user for an integer input and checks if the number is even or odd. Uses a for loop to generate a list of even numbers from 1 to 50 and prints the list. Uses a while loop to print numbers from 10 down to 1 in reverse order. Bonus: Use a function to handle number classification (even/odd). GitHub Submission: Commit the script as control_structures.py in the python_basics folder and push it to your remote GitHub repo.

def even_odd():
    while True:
        try:
            num = int(input('Enter an integer: '))
            break
        except ValueError:
            print('Invalid input. Please enter an integer.')
    if num % 2 == 0:
        print('Even')
    else:
        print('Odd')

even_odd()



my_list = []
for i in range(1,51):
    if i % 2 == 0:
        my_list.append(i)
print(my_list)



i = 10
while i > 0:
    print(i)
    i -= 1

