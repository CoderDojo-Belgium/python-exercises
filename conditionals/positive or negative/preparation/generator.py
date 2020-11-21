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
input block size: 1
output block size: 1
comparison: exact match
<LANGUAGE code="nl">
    <fixed from="odd" to="oneven" />
</LANGUAGE>
'''

# generate test cases
cases = [42, -13]
while len(cases) < 50:
    number = random.randint(-100, 100)
    if number not in cases and number != 0:
        cases.append(number)

# configure test files
infile = open(os.path.join(evaldir, '0.in'), 'w', encoding='utf8')
outfile = open(os.path.join(evaldir, '0.out'), 'w', encoding='utf8')

# generate unit tests
for number in cases:

    # add unit test to input file
    print(number, file=infile)

    # add unit test to output file
    print('positive' if number > 0 else 'negative', file=outfile)

# output settings
print(settings, file=outfile)
