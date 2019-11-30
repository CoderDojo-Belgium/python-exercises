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
tab name: echo
python input without prompt: true
block count: multi
input block size: 1
output block size: ends with
comparison: exact match
'''

# generate test cases
cases = [
    'CoderDojo',
    'Scratch',
    'Micro:bit',
    'Arduino',
    'Unity',
    'Arduino',
    'Minecraft',
]

# configure test files
infile = open(os.path.join(evaldir, '0.in'), 'w', encoding='utf8')
outfile = open(os.path.join(evaldir, '0.out'), 'w', encoding='utf8')

# generate unit tests
for index, word in enumerate(cases):

    # add unit test to input file
    print(word, file=infile)

    # add empty line as a separator between outputs
    if index:
        print(file=outfile)

    # add unit test to output file
    for _ in range(len(word)):
        print(word, file=outfile)

# output settings
print(settings, file=outfile)
