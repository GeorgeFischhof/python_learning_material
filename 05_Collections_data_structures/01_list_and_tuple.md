# Lists

In Python you define a list by using brackets.<br/>
An empty list would simply be `fruits = []`<br/>
But it is much more readable if we
create it with the list constructor:

```python
fruits = list()
```

A list can have any number of elements of any type.<br/>
Elements can be repeated.<br/>
The elements can have different types.

The elements in the list are ordered by their index.<br/>
The index starts with 0 (zero).

To access a list element use the index between the brackets,<br/>
such as `fruits[0]`, `fruits[1]` and so on.

## example

```python
cities_and_zip_numbers = ["New York", 10001, "Los Angles", 90001, "Boston", 02101,]
cities_and_zip_numbers = list("New York", 10001, "Los Angles", 90001, "Boston", 02101,)
print(cities_and_zip_numbers[0])
print(cities_and_zip_numbers)

# the last comma is not a typo, it is allowed, in fact sometimes it is very good
```

# Tuples

Tuples are constant lists.<br/>
They are unchangeable (documentation calls them immutable).<br/>
Tuples are defined with parentheses:

```python
animals = ("elephant", "frog")
```

But it is much more readable if we
create it with the tuple constructor:

```python
animals = tuple("elephant", "frog")
```

Note: there is not too much sense in creating an empty tuple,<br/>
because after creation it is not changeable.

## example

```python
cities_and_zip_numbers = ("New York", 10001, "Los Angles", 90001, "Boston", 02101,)
cities_and_zip_numbers = tuple("New York", 10001, "Los Angles", 90001, "Boston", 02101,)
print(cities_and_numbers[0])
print(cities_and_numbers)
```

To get all elements of a list or tuple you can use a for cycle:

```python
for item in cities_and_zip_numbers:
    print(item)
```
