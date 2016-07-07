import sys
import data
import functions

def main():
    print("Welcome to the Hangman game!\nThe computer chose a word for you, and the word is:")
    word = functions.pick_word()
    guesses = []
    print(functions.encode_word(word, guesses)) 
    guesses.append(input("What's your guess?\n"))

if __name__ == '__main__':
    main()
