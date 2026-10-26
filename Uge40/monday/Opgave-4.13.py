# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
# simple foods, and store them in a tuple.

foods = ('fruit', 'scrambled eggs', 'toast', 'salad', 'fried vegetables')

# • Use a for loop to print each food the restaurant off ers.

print("\nOriginal foods at the restaurant:")
for food in foods:
    print(food)

# • Try to modify one of the items, and make sure that Python rejects the change.
# Un-comment the next line to see error
# foods[0] = 'hashbrowns'

# • The restaurant changes its menu, replacing two of the items with different
# foods. Add a line that rewrites the tuple, and then use a for loop to print
# each of the items on the revised menu

foods = ('fruit', 'scrambled eggs', 'toast', 'oatmeal', 'roasted potatoes')

print("\nModified foods at the restaurant:")
for food in foods:
    print(food)
