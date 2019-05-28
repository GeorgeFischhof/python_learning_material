
# Unicode in Python
# =================

# https://docs.python.org/3/library/unicodedata.html


# Unicode names from
# http://unicode.org/charts/
# can be used ;-)


print('PI: \N{GREEK SMALL LETTER PI}')
# ==> will print the greek letter PI


print('Snake: \N{SNAKE}')
# works as well ;-) and used in textual environments as
# Python symbol


# Python interprets the unicode characters well
# =============================================

import unicodedata

bengali_text = "১২৩৪৫.৬৭৮৯০"
print('bengali_text:', bengali_text, '\n')


print('Name of characters in bengali text:')
for character in bengali_text:
    print(unicodedata.name(character))

'''
BENGALI DIGIT ONE
BENGALI DIGIT TWO
BENGALI DIGIT THREE
BENGALI DIGIT FOUR
BENGALI DIGIT FIVE
FULL STOP
BENGALI DIGIT SIX
BENGALI DIGIT SEVEN
BENGALI DIGIT EIGHT
BENGALI DIGIT NINE
BENGALI DIGIT ZERO
'''

print()
print('bengali_text as float:', float(bengali_text))
# ==> 12345.6789
