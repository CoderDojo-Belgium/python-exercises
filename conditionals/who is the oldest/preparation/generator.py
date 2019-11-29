import os
import random

# set fixed seed for generating test cases
random.seed(123456789)

# locate evaldir
evaldir = os.path.join('..', 'evaluation')
if not os.path.exists(evaldir):
    os.makedirs(evaldir)

# configuration settings
settings = '''--------------------------------------------------------------------
tab name: feedback
python input without prompt: true
block count: multi
input block size: 4
output block size: 1
comparison: exact match
<LANGUAGE code="nl">
    <fixed from="younger" to="jonger" />
    <fixed from="older" to="ouder" />
    <fixed from="then" to="dan" />
    <fixed from="and" to="en" />
    <fixed from="are the same age" to="zijn even oud" />
</LANGUAGE>
'''

def result(name1, age1, name2, age2):

    if age1 < age2:
        return f'{name1} is younger then {name2}'
    elif age1 > age2:
        return f'{name1} is older then {name2}'
    else:
        return f'{name1} and {name2} are the same age'

# generate test cases
persons = [
    ('Alice', 9),
    ('Bob', 11),
    ('Claire', 15),
    ('Dave', 37),
    ('Emily', 11),
    ('Frank', 16),
]
cases = [
    ('Alice', 9, 'Bob', 11),
    ('Dave', 37, 'Claire', 15),
    ('Bob', 11, 'Emily', 11),
]
while len(cases) < 10:

    first, second = random.sample(persons, 2)
    if first + second not in cases:
        cases.append(first + second)

# configure test files
infile = open(os.path.join(evaldir, '0.in'), 'w', encoding='utf8')
outfile = open(os.path.join(evaldir, '0.out'), 'w', encoding='utf8')

# generate unit tests
for case in cases:

    # add unit test to input file
    print(*case, sep='\n', file=infile)

    # add unit test to output file
    print(result(*case), file=outfile)

# output settings
print(settings, file=outfile)
