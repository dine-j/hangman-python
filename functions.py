# Module containing all useful functions for the game

import data
import random

def pick_word():
    random_index = random.randrange(len(data.words))
    return data.words[random_index]

def encode_word(word, letters):
    return "".join([letter if letter in letters else '_' for letter in word])

def print_best_scores(scores):
    score_table = "BEST SCORES - TOP 3:\n"
    if len(scores) < 3:
        top = len(scores)
    else:
        top = 3
    sorted(scores.items(), key=lambda x:x[1])
    best_players = scores.keys()
    i = 0
    while i < top:
        score_table += best_players[i] + " " + str(scores[best_players[i]]) + "\n"
        i += 1
    return score_table
