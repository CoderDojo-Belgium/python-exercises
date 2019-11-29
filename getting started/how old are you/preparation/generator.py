import os
import pickle
import random

# set fixed seed for generating test cases
random.seed(123456789)

# locate evaldir
evaldir = os.path.join('..', 'evaluation')
if not os.path.exists(evaldir):
    os.makedirs(evaldir)

# configuration settings
settings = '''--------------------------------------------------------------------
python input without prompt: true
block count: multi
input block size: 2
output block size: 1
comparison: exact match
<LANGUAGE code="nl">
    <function from="years" to="jaar" />
    <function from="old" to="oud" />
</LANGUAGE>
'''

# generate test cases
cases = [
    ('Alice', 9),
    ('Bob', 21),
    ('Claire', 15),
    ('Dave', 37),
]

# configure test files
infile = open(os.path.join(evaldir, '0.in'), 'w', encoding='utf8')
outfile = open(os.path.join(evaldir, '0.out'), 'w', encoding='utf8')

# generate unit tests
for name, age in cases:

    # add unit test to input file
    print(name, file=infile)
    print(age, file=infile)

    # add unit test to output file
    print(f'{name} is {age} years old.', file=outfile)

# output settings
print(settings, file=outfile)
