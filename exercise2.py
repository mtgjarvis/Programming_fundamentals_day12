names = ['Mark', 'James', 'Jill']

print('What is your name? ')
person_name = input()

def door_man(list_names):
    for item in names:
        if person_name == (item):
            return f'Hello {item}, welcome to the club'
    if person_name != (item):
            return f'You are not welcome here {person_name}!'

print(door_man(names))
