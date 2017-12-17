
import random
import string
import uuid


def generate_uuid():
    return str(uuid.uuid4())


def generate_secret_key():
    """ generate a django secret_key """
    characters = string.ascii_lowercase + string.digits + '()=+-!^@&%#$'
    key = "".join(random.choice(characters) for x in range(50))
    return key


def generate_password():
    """ generate a random password """
    characters = string.ascii_letters + string.digits
    password = "".join(random.choice(characters) for x in range(random.randint(8, 16)))
    return password


def access(container, path, value=None):
    paths = path.split('/')
    key = paths[0]
    paths.pop(0)
    if len(paths) == 0:
        # leaf
        if value:
            container[key] = value
            return True
        else:
            if key in container:
                return container[key]
            else:
                return False
    else:
        # path
        path = ''.join('%s/' % p for p in paths)
        path = path[:len(path) - 1]
        if value:
            # set
            if type(container) is not dict:
                container = dict()
            if key in container:
                if type(container[key]) is not dict:
                    container[key] = dict()
            else:
                container[key] = dict()
            return access(container[key], path, value)
        else:
            # get
            if type(container) is not dict:
                return False
            else:
                if key not in container:
                    return False
                else:
                    return access(container[key], path, value)
