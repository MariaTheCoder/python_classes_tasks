# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
#
# • Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.
#
# • Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the
# newline character (\n) to insert a blank line between each word-meaning
# pair in your output

glossary = {
    'programming language': 'a programming language is a set of instructions that enables humans to communicate with computers',
    'data types': 'variables can store data of different types, and different types can do different things. Python has the following data types built-in by default, such at str, int, bool etc.',
    'variables': 'variables are containers for storing data values.',
    'lists': 'lists are used to store multiple items in a single variable. Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.',
    'loops': 'python has two primitive loop commands: for and while loops',
}

for key, value in glossary.items():
    print(f"{key}: {value}")