# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages() that prints each text message and
# moves each message to a new list called sent_messages as it’s printed. After
# calling the function, print both of your lists to make sure the messages were
# moved correctly.

sent_messages = []
typed_messages = []


def send_messages():
    for msg in typed_messages:
        sent_messages.append(msg)
        print(f'Message "{msg}" was sent!')


def show_messages():
    for msg in typed_messages:
        print(msg)


while True:
    print("press q to end program")
    message = input("\nPlease enter a message: ")

    if message == "q":
        show_messages()
        send_messages()
        break

    typed_messages.append(message)

print("typed_messages:", typed_messages)
print("sent_messages:", sent_messages)
