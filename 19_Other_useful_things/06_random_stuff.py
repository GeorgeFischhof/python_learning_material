
# https://docs.python.org/3/library/random.html

import random

# random.random()
# Return the next random floating point number in the range [0.0, 1.0) (1.0 is not included)
print('random.random() \n', random.random())


# random.randint(a, b)
# Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1)
print('random.randint(1, 10) \n', random.randint(1, 10))


# random.choice(seq)
# Return a random element from the non-empty sequence seq. If seq is empty, raises IndexError
# with random.choices() we can create a weighted random
fruits = ('apple', 'banana', 'lemon', 'orange')
print('random.choice(fruits) \n', random.choice(fruits))


# lottery (the oldest hungarian lottery: 5 numbers from 90)
print('numbers for oldest hungarian lottery \n', random.sample(range(1, 91), 5))


# shuffling cards
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]

# mixing cards returns the mixed list
print('random.sample(cards, len(cards) \n', random.sample(cards, len(cards)))

# mixing cards inplace (!)
random.shuffle(cards)
print('cards after random.shuffle(cards) \n', cards)


# random reproducibility
random.seed('any number or string')
print('repeated - first execution')
for index in range(5):
    print(random.randint(1, 10), end=' ')
print()

random.seed('any number or string')
print('repeated - second execution')
for index in range(5):
    print(random.randint(1, 10), end=' ')

