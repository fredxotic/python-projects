def show_messages(send_messages,sent_messages):
    while send_messages:
        current_message = send_messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

def show_sent_messages(sent_messages):
    print("\nThe following messages have been sent:")
    for sent_message in sent_messages:
        print("✓",sent_message)

send_messages = ["Hello am feeling weird.","Hello, i want to do it.","Hello, am this close to doing it."]
sent_messages = []

show_messages(send_messages[:],sent_messages)
show_sent_messages(sent_messages)

print("\n",send_messages)
print(sent_messages)
