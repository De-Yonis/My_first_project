import random

def vocab_file():
    VocabD = {}
    with open("spanish.txt") as f:
        for line in f:
            (key, value) = line.split(",")
            VocabD[key] = value.rstrip()
    return VocabD


def game():
    response = input("Type Yes below to start:\n").lower()
    if response == "yes":
        VocabD = vocab_file()
        question_list = list(VocabD.keys())
       
        
        random.shuffle(question_list)
        correct = 0
        wrong = 0
    
        for word in question_list:
            presented = "{}"
            print(" ")  
            print(presented.format(word))
            inputAnswer = input("Answer: ").capitalize()

            if inputAnswer == (VocabD[word]):
                print("Great, thats correct \n")
                correct += 1
            else:
                print("Wrong mate")
                print("The correct answer is", VocabD[word])
                wrong += 1

        tally = "You have {} Correct and {} Wrong"
        print(" ")
        print(tally.format(correct, wrong))
        repeat = input("Shall we go again?:\n ").lower()
        if repeat == "Yes":
            again()
        else:
            print("See you later")
    else:
        print("See you later")


def again():
    return game()


print("Hello and Welcome to the quiz Yonis")
game()
