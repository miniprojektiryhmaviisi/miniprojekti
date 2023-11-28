from database_initialization import initialize_database


def build():
    ''' alustaa tietokannat
    '''
    initialize_database()

if __name__ == "__main__":
    '''tämä avulla voi komentorivilla kutsua build()'''
    build()
