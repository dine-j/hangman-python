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
    sorted(scores.items(), key=lambda x:x[1])
    best_players = scores.keys()
    i = 0
    while i < 3:
        score_table += best_players[i] + " " + scores[best_players[i]]
    return score_table
