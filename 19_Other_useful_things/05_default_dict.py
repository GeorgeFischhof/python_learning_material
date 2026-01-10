
# https://docs.python.org/3/library/collections.html#collections.defaultdict

from collections import defaultdict

colors = [("yellow", 1), ("blue", 2), ("yellow", 3), ("blue", 4), ("red", 1)]

numbers_by_color = defaultdict(list)

for key, value in colors:
    numbers_by_color[key].append(value)

print(numbers_by_color)
# defaultdict(<class "list">, {"yellow": [1, 3], "blue": [2, 4], "red": [1]})


#
# without defaultdict
#


colors_and_numbers = [("yellow", 1), ("blue", 2), ("yellow", 3), ("blue", 4), ("red", 1)]

# collect colors
colors = [pair[0] for pair in colors_and_numbers]

# we can not use fromkeys(colors, list()) here, because it would result several same lists
numbers_by_color = dict().fromkeys(colors)
# actually we can skip this step, and use
# for key in colors
# in next step

# add list as value for keys
for key in numbers_by_color:
    numbers_by_color[key] = list()

# add the word to appropriate list
for pair in colors_and_numbers:
    numbers_by_color[pair[0]].append(pair[1])

print(numbers_by_color)
# {"yellow": [1, 3], "blue": [2, 4], "red": [1]}
