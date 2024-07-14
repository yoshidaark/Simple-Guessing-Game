import random


def GuessingGame():
    filename = open('Words.txt', "r")
    wordlist = []
    for x in filename:
        wordlist.append(x)

    hiddenword = wordlist[random.randint(0, len(wordlist)-1)]
    displayword = hiddenword

    for _ in displayword:
        displayword = displayword.replace(displayword[random.randint(0, len(displayword)-2)], '?')

    print('Welcome to Word Guessing Game')
    guess = True

    while guess:

        print(displayword)

        userinput = input("Enter a letter or a word: ")
        input1 = userinput.lower()
        word = hiddenword.lower()
        if len(userinput) > 1:
            if input1 in hiddenword.lower():
                print("Guess is Correct!")
                guess = False
            else:
                print("Guess is not Correct!")

        else:

            if word.find(input1) > -1:
                displayword = displayword.replace(displayword[word.find(input1)], userinput, word.count(input1))
                print(word.find(userinput))
                print(f"{userinput} is a letter")

            else:
                print(f"{userinput} is not a letter")


GuessingGame()


