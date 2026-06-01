#EduBot - AI Educational Assistant
#Created by: Surayya

from search import find_answer

def greet_user():
    print("Hello! I am EduBot.")
    print("I am here to help you learn")
    name = input("What is your name? ")
    print(f"Nice to meet you, {name}! Lets learn together!")
    return name

def chat():
    name = greet_user()
    print ("\nYou can ask me anything! Type 'bye' to exit.\n")

    while True:
        question = input(("You: "))
        if question.lower() == "bye":
            print(f"Goodbye, {name}! Happy learning!")
            break
        answer = find_answer(question)
        print(f"EduBot: {answer}\n")

chat()
