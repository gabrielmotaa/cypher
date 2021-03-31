# Cypher

## An object oriented method for implemeting a Caesar Cypher

Author: Gabriel da Mota

This is a personal pratice code for testing the `str.maketrans` and `str.translate` methods in Python, the Numpy style docstrings and the `doctest` module.

## How to use it
Example, also provided in the code:

```python
c = Cypher("b")  # shift the alphabet by the letter b
encrypted = c.encrypt("This is my name")
print(encrypted)  # prints "Uijt jt nz obnf"
decrypted = c.decrypt(encrypted)
print(decrypted)  # prints "This is my name"
```

## Docstring
To test the docstring, run the command: `python3 -m doctest -v cypher.py`
