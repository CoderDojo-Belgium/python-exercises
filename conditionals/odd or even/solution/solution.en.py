# ask name and age of the first person
name1 = input()
age1 = int(input())

# ask name and age of the second person
name2 = input()
age2 = int(input())

# determine the answer
if age1 < age2:
    answer = f'{name1} is younger then {name2}'
elif age1 > age2:
    answer = f'{name1} is older then {name2}'
else:
    answer = f'{name1} and {name2} are the same age'

# output the answer
print(answer)
