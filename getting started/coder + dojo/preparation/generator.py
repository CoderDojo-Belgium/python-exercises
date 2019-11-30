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
input block size: 2
output block size: 1
comparison: exact match
'''

# generate test cases
cases = [
    ('Coder', 'Dojo'),
    ('Micro', 'bit'),
    ('Mine', 'craft'),
    ('Spider', 'man'),
    ('Wonder', 'woman'),
]

# configure test files
infile = open(os.path.join(evaldir, '0.in'), 'w', encoding='utf8')
outfile = open(os.path.join(evaldir, '0.out'), 'w', encoding='utf8')

# generate unit tests
for word1, word2 in cases:

    # add unit test to input file
    print(word1, file=infile)
    print(word2, file=infile)

    # add unit test to output file
    print(word1 + word2, file=outfile)

# output settings
print(settings, file=outfile)
