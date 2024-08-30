import random


print("hello world")
receivedText = input("What she messaged you: ")
print(receivedText)
messageArray = ["you are cute", "Hey whatre you up to", "Lets grab a drink"]
randomMessage = messageArray[random.randint(0, 2)]
print("Send her this: ")
print(randomMessage)
