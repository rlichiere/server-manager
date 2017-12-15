
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


