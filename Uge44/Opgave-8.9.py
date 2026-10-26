# 8-9. Messages: Make a list containing a series of short text messages. Pass the
# list to a function called show_messages(), which prints each text message.

def show_messages(all_messages):
    for msg in all_messages:
        print(msg)


messages = []

while True:
    print("press q to end program")
    message = input("\nPlease enter a message: ")

    if message == "q":
        show_messages(messages)
        break

    messages.append(message)
