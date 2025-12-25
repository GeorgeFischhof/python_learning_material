
# String operations (string methods)

<https://docs.python.org/3.7/library/stdtypes.html#string-methods>


## Search and find related methods

- `str.startswith(prefix[, start[, end]])` <br/>
Return True if string starts with the prefix,
otherwise return False. prefix can also be a tuple of
prefixes to look for. With optional start,
test string beginning at that position.
With optional end, stop comparing string at that position

 - `str.endswith(suffix[, start[, end]])` <br/>
Return True if the string ends with the specified suffix,
otherwise return False. 

suffix can also be a tuple of suffixes to look for.
With optional start, test beginning at that position.
With optional end, stop comparing at that position.

- `str.find(sub[, start[, end]])` <br/>
Return the lowest index in the string where substring
sub is found within the slice s[start:end].
Optional arguments start and end are interpreted as
in slice notation. Return -1 if sub is not found.

Note: The find() method should be used only if you
need to know the position of sub.
To check if sub is a substring or not, use the in operator:
'Py' in 'Python' ==> True

- `str.rfind(sub[, start[, end]])` <br/>
Return the highest index in the string where substring
sub is found, such that sub is contained within
s[start:end]. Optional arguments start and end
are interpreted as in slice notation. Return -1 on failure


## Conversion and formatting methods


- `str.format(*args, **kwargs)` <br/>
Perform string formatting and interpolating operations.
The string on which this method is called
can contain literal text or replacement
fields delimited by braces {}

```python
print("The sum of 1 + 2 is {0}".format(1+2))
# ==> "The sum of 1 + 2 is 3"
```

```python
number = 5
print('I have {number} apples'.format(number=number))
# ==> 'I have 5 apples'
```

See Format String Syntax for a description of the
various formatting options that can be specified
in format strings.
<https://docs.python.org/3.7/library/string.html#formatstrings>

From 3.6 there is f-string, which implements format:
```python
number = 5
print(f'I have {number} apples')
# ==> I have 5 apples
```


- `str.join(iterable)` <br/>
Return a string which is the concatenation
of the strings in iterable,
and the the separator will be str

```python
print(''.join(('1', '2', '3')))  # ==> '123'
print('a'.join(('1', '2', '3')))  # ==> '1a2a3'
print('X '.join('apple')  # ==> 'aX pX pX lX e'
```

- `str.replace(old, new[, count])` <br/>
Return a copy of the string with all occurrences of
substring old replaced by new. If the optional
argument count is given, only the first count
occurrences are replaced


## Aligning

- `str.center(width[, fillchar])` <br/>
Return centered in a string of length width.
Padding is done using the specified fillchar
(default is an ASCII space).
The original string is returned if width is
less than or equal to len(s)

- `str.ljust(width[, fillchar])` <br/>
Return the string left justified in a string
of length width. Padding is done using the
specified fillchar (default is an ASCII space)
The original string is returned if width is
less than or equal to len(s).

- `str.rjust(width[, fillchar])` <br/>
Return the string right justified in a string
of length width. Padding is done using the
specified fillchar (default is an ASCII
space). The original string is returned
if width is less than or equal to len(s).

- `str.zfill(width)` <br/>
Return a copy of the string left filled
with ASCII '0' digits to make a string of length width


## Change cases

- `str.lower()` <br/>
Return a copy of the string with all the cased
characters [4] converted to lowercase.

The lowercasing algorithm used is described in
section 3.13 of the Unicode Standard.


- `str.upper()` <br/>
Return a copy of the string with all the cased
characters [4] converted to uppercase. Note
that s.upper().isupper() might be False
if s contains uncased characters


- `str.casefold()` <br/>
Return a casefolded copy of the string.
Casefolded strings may be used for caseless matching.

Casefolding is similar to lowercasing but more
aggressive because it is intended to remove all
case distinctions in a string. For example,
the German lowercase letter 'ß' is equivalent to "ss".
Since it is already lowercase, lower() would do
nothing to 'ß'; casefold() converts it to "ss".

The casefolding algorithm is described in section 3.13 of the Unicode Standard.


- `str.capitalize()` <br/>
Return a copy of the string with its first
character capitalized and the rest lowercased.


- `str.title()` <br/>
Return a titlecased version of the string where
words start with an uppercase character and the
remaining characters are lowercase


- `str.swapcase()` <br/>
Return a copy of the string with uppercase
characters converted to lowercase and vice
versa. Note that it is not necessarily true
that s.swapcase().swapcase() == s.



## Remove characters

- `str.lstrip([chars])` <br/>
Return a copy of the string with leading characters removed
The chars argument is a string specifying
the set of characters to be removed.
If omitted or None, the chars argument defaults to removing whitespace


- `str.rstrip([chars])` <br/>
Return a copy of the string with trailing characters removed
The chars argument is a string specifying
the set of characters to be removed.
If omitted or None, the chars argument defaults to removing whitespace


- `str.strip([chars])` <br/>
Return a copy of the string with the leading and
trailing characters removed. The chars argument
is a string specifying the set of characters
to be removed. If omitted or None, the chars
argument defaults to removing whitespace.



## Splitting by delimiters

- `str.split(sep=None, maxsplit=-1)` <br/>
Return a list of the words in the string,
using sep as the delimiter string. If maxsplit is given,
at most maxsplit splits are done (thus, the list will
have at most maxsplit+1 elements). If maxsplit is not
specified or -1, then there is no limit on the number
of splits (all possible splits are made)


- `str.rsplit(sep=None, maxsplit=-1)` <br/>
Return a list of the words in the string,
using sep as the delimiter string. If maxsplit is given,
at most maxsplit splits are done, the rightmost ones.
If sep is not specified or None, any whitespace
string is a separator


- `str.splitlines([keepends])` <br/>
Return a list of the lines in the string, breaking at
line boundaries. Line breaks are not included in the
resulting list unless keepends is given and true



## Checking the content of a string

- `str.isalnum()` <br/>
Return true if all characters in the string are
alphanumeric and there is at least one character,
false otherwise


- `str.isalpha()` <br/>
Return true if all characters in the string are
alphabetic and there is at least one character,
false otherwise


- `str.isascii()` <br/>
Return true if the string is empty or all
characters in the string are ASCII,
false otherwise


- `str.isdecimal()` <br/>
Return true if all characters in the string
are decimal characters and
there is at least one character, false otherwise


- `str.isdigit()` <br/>
Return true if all characters in the string are
digits and there is at least one character,
false otherwise


- `str.isidentifier()` <br/>
Return true if the string is a valid identifier
according to the language definition

Note: Use keyword.iskeyword() to test for
reserved identifiers such as def and class


- `str.islower()` <br/>
Return true if all cased characters in the
string are lowercase and there is at least one
cased character, false otherwise


- `str.isnumeric()` <br/>
Return true if all characters in the string
are numeric characters, and there is at
least one character, false otherwise


- `str.isprintable()` <br/>
Return true if all characters in the string
are printable or the string is empty, false otherwise


- `str.isspace()` <br/>
Return true if there are only whitespace characters
in the string and there is at least one character,
false otherwise


- `str.istitle()` <br/>
Return true if the string is a titlecased
string and there is at least one character


- `str.isupper()` <br/>
Return true if all cased characters in the
string are uppercase and there is at least
one cased character, false otherwise



## Not so frequently used methods


- `str.count(sub[, start[, end]])` <br/>
Return the number of non-overlapping occurrences
of substring sub in the range [start, end].
Optional arguments start and end are interpreted
as in slice notation.


- `str.encode(encoding="utf-8", errors="strict")` <br/>
Return an encoded version of the string as a bytes object.
Default encoding is 'utf-8'.


- `str.expandtabs(tabsize=8)` <br/>
Return a copy of the string where all tab characters
are replaced by one or more spaces,
depending on the current column and the given tab size.
