import random
import string

def random_email():
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choices(letters, k=8)) + "@mail.ru"

RANDOM_EMAL = random_email()