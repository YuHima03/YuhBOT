import codecs

def write(path, type = 'str', *arg):
    try:
        with codecs.open(str(path), 'r') as file:
            pass
    except Exception as err:
        return err

def load(path, type = 'str', *arg):
    pass