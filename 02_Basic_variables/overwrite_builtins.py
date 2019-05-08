

def print(arg):
    pass

print('a')


'''
Result:
<Nothing>

Because you overwrote the print function 
you can do the following now instead of print:

import sys
sys.stdout.write(str(arg))

or the real solution is the usage of builtins module as 
Python stores the built-in functions in builtins module:
'''

import builtins
builtins.print('print from builtins')

'''
Result:
print from builtins
'''
