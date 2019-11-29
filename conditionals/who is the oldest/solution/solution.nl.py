# naam en leeftijd eerste persoon opvragen
naam1 = input()
leeftijd1 = input()

# naam en leeftijd tweede persoon opvragen
naam2 = input()
leeftijd2 = input()

# antwoord bepalen
if leeftijd1 < leeftijd2:
    antwoord = f'{naam1} is jonger dan {naam2}'
elif leeftijd1 > leeftijd2:
    antwoord = f'{naam1} is ouder dan {naam2}'
else:
    antwoord = f'{naam1} en {naam2} zijn even oud'

# antwoord uitschrijven
print(antwoord)
