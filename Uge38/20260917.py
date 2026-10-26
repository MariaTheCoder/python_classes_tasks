# While loops

# x = 3

# while x <= 5:
#    print(x)

# We never increment the value of x so the loop will continue for all eternity (or until our program crashes)
# We may need to stop our program manually.

x = 1

while x <= 24:
    print(x)
    x += 1

# Let's look at an example with while true
#
#DANGER! Infinite loop in line 21 and 22.

# while True :
#    print("Hello World")

# Let's avoid infinite loops and look at this example instead:

while True:
    name = input("Enter your name: ")
    if name == "Q":
        break

# We break the loop by saying, if our given input equals "Q" then we want to quit the loop / exit the loop.
# For each time we go through the loop, the unit where the value of the variable name is stored in memory gets
# overwritten by whatever the user typed in. It is the same memory storage being used many times over and over again.
# Any existing values get overwritten, in other words. 