class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


emails = []
command = input()
while command != 'Stop':
    command = command.split(' ')
    sender = command[0]
    receiver = command[1]
    content = command[2]
    email = Email(sender, receiver, content)
    emails.append(email)

    command = input()
command = input()
#send_emails = list(map(lambda x: int(x), command.split(', ')))
send_emails = [int(x) for x in command.split(', ')]
for x in send_emails:
    emails[x].send()

for email in emails:
    print(email.get_info())
