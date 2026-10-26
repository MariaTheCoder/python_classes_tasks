# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 99) by replacing your series of print()
# calls with a loop that runs through the dictionary’s keys and values. When
# you’re sure that your loop works, add five more Python terms to your glossary.
# When you run your program again, these new words and meanings should
# automatically be included in the output.

glossary = dict(
    programming_language='a programming language is a set of instructions that enables humans to communicate with computers',
    data_types='variables can store data of different types, and different types can do different things. Python has the following data types built-in by default, such at str, int, bool etc.',
    variables='variables are containers for storing data values.',
    lists='lists are used to store multiple items in a single variable. Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.',
    loops='python has two primitive loop commands: for and while loops'
)

glossary['string'] = 'a data type of type text'
glossary['boolean'] = 'a data type of type boolean, meaning it can only take one of two values: True or False'
glossary['integer'] = 'a data type of type numeric. Integers are whole numbers'
glossary['dictionary'] = 'dictionaries are used to store data values in key:value pairs.'
glossary[
    'python'] = 'python is a popular programming language. It was created by Guido van Rossum, and released in 1991.'
