# About commenting the code

## Don’t say the obvious

Bad:

```python
# increments x by 2
x = x + 2
```

Good:

```python
# compensate for border on both the sides
x = x + 2
```

## Make Comments Unnecessary

Bad:

```python
# process documents
...
```

Good:  
(create a function instead of commenting the code)

```python
docs = process_documents(...)
```
