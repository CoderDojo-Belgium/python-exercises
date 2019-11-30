# ask first and last name of a person
first_name = input('What is your first name? ')
last_name = input('What is your last name? ')

# generate username
username = (first_name[0] + last_name).lower()

# output username
print(username)
