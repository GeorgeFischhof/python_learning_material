
# Functions optional parameters with default value
# ================================================


def add_numbers(a, b, c=None):
    if c is not None:
        return a + b + c
    else:
        return a + b


print(add_numbers(2, 3))  # ==> 5
print(add_numbers(2, 3, 4))  # ==> 9
print()


def login(user='administrator', password='secret'):
    print('user =', user, ' password =', password)


login()                       # user = administrator  password = secret
login('user')                 # user = user  password = secret
login(user='user')            # user = user  password = secret
login(password='new_secret')  # user = administrator  password = new_secret

login(user='user', password='new_secret')  # user = user  password = new_secret
login(password='new_secret', user='user')  # user = user  password = new_secret
