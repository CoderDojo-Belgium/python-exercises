import os
import sys
import imp
import random
import string

# set fixed seed for generating test cases
random.seed(123456789)

# locate evaldir
evaldir = os.path.join('..', 'evaluation')
if not os.path.exists(evaldir):
    os.makedirs(evaldir)

# locate solutiondir
solutiondir = os.path.join('..', 'solution')
if not os.path.exists(solutiondir):
    os.makedirs(solutiondir)

# load functionality defined in sample solution
solution = imp.load_source(
    'solution',
    os.path.join(solutiondir, 'solution.en.py')
)
for name in dir(solution):
    if not (name.startswith('__') and name.endswith('__')):
        globals()[name] = eval('solution.{}'.format(name))

# generate unit tests for functions first_letter and username
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

# generate test cases for function first_letter
sys.stdout = open(os.path.join('..', 'evaluation', '0.in'), 'w', encoding='utf-8')
for name in cases:

    # generate statement
    first_name, last_name = name.split()
    print(f'>>> first_letter({first_name!r})')

    # generate return value
    try:
        print(f'{first_name[0]!r}')
    except Exception as e:
        print('Traceback (most recent call last):\n{}: {}'.format(
            e.__class__.__name__, e))

    print()

# generate test cases for function username
sys.stdout = open(os.path.join('..', 'evaluation', '1.in'), 'w', encoding='utf-8')
for name in cases:

    # generate statement
    first_name, last_name = name.split()
    print(f'>>> username({first_name!r}, {last_name!r})')

    # generate return value
    try:
        print(f'{username(first_name, last_name)!r}')
    except Exception as e:
        print('Traceback (most recent call last):\n{}: {}'.format(
            e.__class__.__name__, e))

    print()


