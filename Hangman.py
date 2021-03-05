import random
possible_words=['hello','world','secret','word','phone','lamp','mask','singer','bird','stand','bag','bottle','couch']


def hangman():
    word=random.choice(possible_words)
    guesses=''
    tries=8
    characters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    while tries>0:
        failed=0
        for character in word:
            if character in guesses:
                print(character)
            else:
                print("_")
                failed=failed+1
        if failed==0:
            print("Congrats, You Won!")
            print(f"The Word was: {word} ")
            repeat=input("Would you like to Play Again?(y/n): ")
            if repeat=="y":
                hangman()
            elif repeat=="n":
                print("Goodbye!")
                exit()
            else:
                print("Invalid Input")
                exit()
        guess=input("Guess a Character of the Word: ")
        guesses=guesses+guess
        if guess in word:
            
            if guess in characters:
                characters.remove(guess)
                print(characters)
                print("Correct, Keep Going!")
            elif guess not in characters:
                print("You Already Guessed That, Try Again")
                tries=tries+1
        if guess not in word:
            tries=tries-1
            
            print(f"You have {tries} tries remaining.")
            if guess in characters:
                characters.remove(guess)
                print(characters)
                print("Wrong Guess")
            elif guess not in characters:
                print("You Already Guessed That, Try Again")
                tries=tries+1
        if tries==0:
            print("You Lost :(")
            repeat=input("Would you like to Play Again?(y/n): ")
            if repeat=="y":
                hangman()
            elif repeat=="n":
                print("Goodbye!")
                exit()
            else:
                print("Invalid Input")
                exit()
        

if __name__=="__main__":
    hangman()