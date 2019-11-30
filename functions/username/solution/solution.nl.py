def eerste_letter(naam):

    """
    >>> eerste_letter('Sansa')
    'S'
    >>> eerste_letter('Jon')
    'J'
    """

    return naam[0]

def gebruikersnaam(voornaam, familienaam):

    """
    >>> gebruikersnaam('Sansa', 'Stark')
    'sstark'
    >>> gebruikersnaam('Jon', 'Snow')
    'jsnow'
    """

    return (eerste_letter(voornaam) + familienaam).lower()

if __name__ == '__main__':
    import doctest
    doctest.testmod()
