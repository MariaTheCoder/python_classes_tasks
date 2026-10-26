# 8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function
# send_messages() with a copy of the list of messages. After calling the function,
# print both of your lists to show that the original list has retained its messages.


sent_messages = []
typed_messages = []


def send_messages(all_messages):
    for msg in all_messages:
        sent_messages.append(msg)
        print(f'Message "{msg}" was sent!')


# def show_messages():
#    for msg in typed_messages:
#        print(msg)


while True:
    print("press q to end program")
    message = input("\nPlease enter a message: ")

    if message == "q":
        # show_messages()
        send_messages(typed_messages)
        break

    typed_messages.append(message)

print("typed_messages:", typed_messages)
print("sent_messages:", sent_messages)
