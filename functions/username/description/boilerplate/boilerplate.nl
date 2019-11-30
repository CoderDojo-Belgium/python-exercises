def eerste_letter(naam):

    """
    >>> eerste_letter('Sansa')
    'S'
    >>> eerste_letter('Jon')
    'J'
    """

def gebruikersnaam(voornaam, familienaam):

    """
    >>> gebruikersnaam('Sansa', 'Stark')
    'sstark'
    >>> gebruikersnaam('Jon', 'Snow')
    'jsnow'
    """

if __name__ == '__main__':
    import doctest
    doctest.testmod()
