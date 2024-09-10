import random


print("Welcome to Sigma Rizzler")
print("Ready to start?")
receivedText = input("yes to start/exit to quit: ")
while( receivedText != "exit"):
    receivedText = input("What did she message you: ")
    if receivedText == "exit":
        break
    print(receivedText)
    messageArray = ["you are cute", "Hey whatre you up to", "Lets grab a drink", "How do you like your coffee?", "pass me your number so we can make plans"]
    randomMessage = messageArray[random.randint(0, 3)]
    print("Send her this: ")
    print(randomMessage)
print("Goodbye Rizzler, goodluck and see you soon;)")
    
