import sys
import data
import functions
import pickle

def main():
    print("Welcome to the Hangman game!\n\nNote: You can quit anytime by entering \"exit\".")
    player_name = raw_input("What's your name?\n")
    
    try:
        with open("scores", 'r') as scores_file:
            scores = pickle.Unpickler(scores_file).load()
            scores_file.close()
    except IOError:
        scores_file = open("scores", 'w')
        scores = {}
        pickle.Pickler(scores_file).dump(scores)
        scores_files.close()

    print("Well, %s, the computer chose a word for you, and the word is:\n" % player_name)
    word = functions.pick_word()
    guesses = []
    while data.nb_rounds > 0 and word != functions.encode_word(word, guesses): 
        print(functions.encode_word(word, guesses) + "\nYou still have %d to figure it out. You used: " % data.nb_rounds + ' - '.join(guesses))
        while True:
            try:
                guess = raw_input("What's your guess?\n")
                if guess == "exit":
                    data.nb_rounds = -1
                    break
                assert guess.isalpha() and len(guess) == 1
                break
            except AssertionError:
                print("Sorry could you please enter a single character?\n")
        guesses.append(guess)
        data.nb_rounds -= 1

    if word == functions.encode_word(word, guesses):
        print("Congrats! You found: %s" % word)
        scores[player_name] = data.nb_rounds
        with open("scores", 'w') as scores_file:
            pickle.Pickler(scores_file).dump(scores)
            scores_file.close()
        functions.print_best_scores(scores)
    elif data.nb_rounds == 0:
        print("You didn't find it in 8 rounds! The word was %s" % word)
    elif data.nb_rounds == -1:
        print("I get it, you're bored. Thank you for playing!")

if __name__ == '__main__':
    main()
