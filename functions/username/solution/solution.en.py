def first_letter(name):

    """
    >>> first_letter('Sansa')
    'S'
    >>> first_letter('Jon')
    'J'
    """

    return name[0]

def username(first_name, last_name):

    """
    >>> username('Sansa', 'Stark')
    'sstark'
    >>> username('Jon', 'Snow')
    'jsnow'
    """

    return (first_letter(first_name) + last_name).lower()

if __name__ == '__main__':
    import doctest
    doctest.testmod()
