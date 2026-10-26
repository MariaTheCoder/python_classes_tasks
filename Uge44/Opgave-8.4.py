# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message.

def make_shirt(size='L', text='I love Python'):
    print("\nThe size is:", size, "\nThe text says:", text)


make_shirt("M")
make_shirt("L")
make_shirt("XS", "I love Bramming")
