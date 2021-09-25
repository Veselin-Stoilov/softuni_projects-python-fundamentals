command = input()
chat = []
while command != 'end':
    if 'Chat' in command:
        action, message = command.split()
        chat.insert(len(chat), message)
    elif 'Delete' in command:
        action, message = command.split()
        if message in chat:
            chat.remove(message)
    elif 'Edit' in command:
        action, msg_to_edit, edited_msg = command.split()
        if msg_to_edit in chat:
            for index, item in enumerate(chat):
                if item == msg_to_edit:
                    chat[index] = edited_msg
    elif 'Pin' in command:
        action, message = command.split()
        if message in chat:
            for index, item in enumerate(chat):
                if item == message:
                    chat.pop(index)
                    chat.insert(len(chat), message)
    elif 'Spam' in command:
        spam_message = command.split()
        spam_message = spam_message[1:]
        chat.extend(spam_message)
    command = input()
for text in chat:
    print(text)
