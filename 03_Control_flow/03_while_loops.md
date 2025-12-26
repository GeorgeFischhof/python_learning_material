# While loops

A `while` loop repeats code until a condition is met.  
Unlike `for` loops, the number of iterations may be unknown.  
A `while` loop always consists of a condition and a block of code.

A `while` loop is executed if and only if the condition is true,  
in contrast to a `for` loop that always has a finite, countable number of steps  
(even if that countable number is zero :-) )

## example

```
start = int(input("start: "))      # ask the numbers from the user
finish = int(input("finish: "))
step = int(input("step: "))

number_to_print = start
while number_to_print < finish:
    print(number_to_print)
    number_to_print = number_to_print + step
```

**result:**

```
start: 3
finish: 16
step: 5
3
8
13
```
