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
tab name: username
python input without prompt: true
block count: multi
input block size: 2
output block size: 1
comparison: exact match
<LANGUAGE code="nl">
    <fixed from="username" to="gebruikersnaam" />
</LANGUAGE>
'''

def username(first_name, last_name):

    return (first_name[0] + last_name).lower()

# generate test cases
cases = [
    'Sansa Stark',
    'Jon Snow',
    'Gregor Clegane',
    'Arya Stark',
    'Tyrion Lannister',
    'Cersei Lannister',
    'Khal Drogo',
    'Eddard Stark',
    'Joffrey Baratheon',
    'Petyr Baelish',
    'Sandor Clegane',
    'Jaime Lannister',
    'Ramsay Bolton',
    'Theon Greyjoy',
    'Margaery Tyrell',
    'Oberyn Martell',
    'Bran Stark',
    'Yara Greyjoy',
    'Daario Naharis',
    'Jorah Mormont',
    'Tormund Giantsbane',
    'Stannis Baratheon',
    'Tommen Baratheon',
    'Samwell Tarly',
    'Robb Stark',
    'Jaqen Hghar',
    'Tywin Lannister',
    'Tyene Sand',
    'Grey Worm',
    'Loras Tyrell',
    'Myrcella Baratheon',
    'Jojen Reed',
    'Walder Frey',
    'Lady Crane',
    'Davos Seaworth',
    'Catelyn Stark',
    'Ellaria Sand',
    'Podrick Payne',
    'Meryn Trant',
    'Janos Slynt',
    'Rodrik Cassel',
    'Renly Baratheon',
    'Barristan Selmy',
    'Alliser Thorne',
    'Othell Yarwyck',
    'Greatjon Umber',
    'Syrio Forel',
    'Rickard Karstark',
    'Beric Dondarrion',
    'Eddison Tollett',
]

# configure test files
infile = open(os.path.join(evaldir, '0.in'), 'w', encoding='utf8')
outfile = open(os.path.join(evaldir, '0.out'), 'w', encoding='utf8')

# generate unit tests
for case in cases:

    # add unit test to input file
    first_name, last_name = case.split()
    print(first_name, file=infile)
    print(last_name, file=infile)

    # add unit test to output file
    print(username(first_name, last_name), file=outfile)

# output settings
print(settings, file=outfile)
