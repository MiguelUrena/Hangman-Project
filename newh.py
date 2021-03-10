import random
import string
def hangman(word_1):
    guesses=''
    tries=8
    alphabet1 = string.ascii_lowercase
    characters=list(alphabet1)
    while tries>0:
        failed=0
        for character in word:
            if character in guesses:
                print(character,end=" ")
            else:
                print("_",end=" ") 
                failed=failed+1
        if failed==0:
            print("\n")
            print("Congrats, You Won!")
            print(f"The Word was: {word} ")
            exit()
        print("\n")
        guess=input("Guess a Character of the Word: ")
        guess=guess.lower()
        guesses=guesses+guess
        guesses=guesses.lower()
        if guess.isalpha()==False:
            print("enter only letters")
        elif len(guess)>1:
            print("enter only a single letter")
        else:
            if guess in word:
                print("Correct, Keep Going!")
                if guess not in characters:
                   print("you have already guessed this letter")
                else:
                   characters.remove(guess)
                   print(characters)
            if guess not in word:
                print("Wrong Guess")
                if guess not in characters:
                   print("you have already guessed this letter")
                else:
                    tries=tries-1
                    characters.remove(guess)
                    print(characters)
                    print(f"You have {tries} tries remaining.")
            if tries==0:
                print("\n")
                print("You Lost :(")
                print(f"The word was: {word}")
                repeat=input("Would you like to Play Again?(y/n): ")
                if repeat== 'y':
                    hangman(word_1)
                else:
                    exit()

if __name__=="__main__":
    possible_words=['hello','world','secret','word','phone','lamp','mask','singer','bird','stand','bag','bottle','couch']
    word=random.choice(possible_words)
    hangman(word)

            
            
            
    