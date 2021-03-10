import random
possible_words=['hello','world','secret','word','phone','lamp','mask','singer','bird','stand','bag','bottle','couch']
guesses=''
tries=8
characters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def get_word(possible_words):
    word=random.choice(possible_words)
    return word

def hangman(tries,word,guesses):
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
                hangman(8,get_word(possible_words),'')
            elif repeat=="n":
                print("Goodbye!")
                exit()
            else:
                print("Invalid Input")
                exit()    
        guess=input("Guess a Character of the Word: ")
        if guess.isalpha()==False:
            print("enter only letters")
        elif len(guess)>1:
            print("enter only a single letter")
        else:
            guesses=guesses+guess
            guesses=guesses.lower()
        if guess in word:
            if guess in characters:
                characters.remove(guess)
                print(characters)
                print("Correct, Keep Going!")
            elif guess not in characters:
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
                hangman(8,get_word(possible_words),'')
            elif repeat=="n":
                print("Goodbye!")
                exit()
            else:
                print("Invalid Input")
                exit()    
    
        

if __name__=="__main__":
    hangman(tries,get_word(possible_words),guesses)