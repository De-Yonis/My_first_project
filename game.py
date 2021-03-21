import random

response = input(
    "Welcome Yonis to the spanish quiz type Yes below to start \n: ")
while response == "Yes":
    VocabD = {"Hola": "Hello", "Adiós": "Goodbye", "Por favor": "Please",
              "Gracias": "Thank you", "Lo siento": "Sorry", "Salud": "Bless you",
              "Sí": "Yes", "No": "No", "¿Quién?": "Who?", "¿Qué?": "What?",
              "¿Por qué?": "Why?", "¿Dónde?": "Where?"
              }

    question_list = list(VocabD.keys())  

    
    random.shuffle(question_list)
    correct = 0
    wrong = 0

    for words in question_list:
        presented = "{}"
        print(presented.format(words))
        inputAnswer = input("Answer: ")
        print(" ")

        if inputAnswer == (VocabD[words]):
            print("Great, thats correct")
            correct += 1
        else:
            print("Wrong mate")
            print(("The correct answer is - '{}'").format(VocabD[words]))
            wrong += 1

    present = "{} Correct and {} Wrong"
    print(present.format(correct, wrong))
    response = input("Go again?")

print(" ")
print("See you later")
