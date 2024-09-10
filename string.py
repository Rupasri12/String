# -*- coding: utf-8 -*-
"""String.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17LXNHKXVf5LDhZPG5MdH85ekHxnzoK38

**concepts**

- `Memory Allocation `
- `Indexing `
- `slicing `
- `skipping `
- `mutable or immutable -> prove it `
- `Built_in_functions in strings `
"""

a = 'data' # save in the Memory

print(a) # calling from the Memory

a = 'data' # saves in the memory

print(a[2])

# index with both the directions

a = 'data science' # save in the Memory
print(a[6]) # forward Index

print(a[-6]) # back ward index

"""- `slicing`

syntax -> s_p : e_p

"""

print(a[6])
print(a[9])

a = 'data science'

print(a[2:6])

print(a[2:9])

"""- `skipping `"""

a = 'data science' # save in the Memory

print(a[::2])

a = 'data science' # save in the Memory

print(a[::3])

"""**what is Mutable and Immutable**

- `Mutable -> if user can increase or decrease memory `
- `Immutable -> user cant increase or decrease memory`
"""

# trying to add

a  = 'kiran' # save in the memory

a[5] = 'j' # trying to allocate extra memory here


print(a)

# delete some memory from the existing memory

a = 'kiran' # save in the Memory

del a[2] # tring to delete character r here

print(a)

# from the above outcomes we can say that string in immutable

a = 'kiran it'

print(len(a))

print(len(dir(str)))

"""**String-Built-in-functions**"""

# capitalize -> it will capital the starting letter


a = 'sai kiRan' # saved in memory


a = a.capitalize() # function is applying

print(a)

# title -> it will capital each word starting letter into capital

a = 'pyThon iS easy lanGuage'

a = a.title()

print(a)

# lower -> small lettets

a = 'AmeriCA'

print(a.lower())

# upper -> capital letters

a = 'AmeriCA'

print(a.upper())

# islower

a = 'america'
print(a.islower())

# isupper

a = 'AMERICAA'

print(a.isupper())

# isalpha -> checks all are alphabets or not

a = 'america is'

print(a.isalpha())

# isnumeric -> only numbers

a = '1322'
print(a.isnumeric())

# isalnum -> we can have anything

a = '1234 '

print(a.isalnum())

# startswith

a = 'deep learning'

print(a.startswith('d'))

# endswith

a = 'deep learning'

print(a.endswith('g'))

# replace

a = 'kiran' # saves in the Memory

print(a.replace('r','j'))

# count -> is used to count the number of times a given repeating

a = 'data science'

print(a.count('i'))

# index -> used to find the index of a given character

a = 'data science'

print(a.index('a',2,8))

len('kiran')

# string and substring

a = 'python is very powerfull than go laguage in india'

print('n i' in a)

97 * 98

67*68

# operators in strings

python = 'ab'
Java = 'CD'

print(python > Java)

# I want to find ascii value of a given character

ord('F')

# I want to find character from a given ascii value

chr(70)

chr(100)

ord('z')

