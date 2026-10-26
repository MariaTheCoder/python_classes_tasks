# 8-15. Printing Models: Put the functions for the example printing_models.py in a
# separate file called printing_functions.py. Write an import statement at the top
# of printing_models.py, and modify the file to use the imported functions.

from printing_functions import print_models

# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

result = print_models(unprinted_designs[:], completed_models)
print(result)
