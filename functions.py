# Module containing all useful functions for the game

import data
import random

def pick_word():
    random_index = random.randrange(len(data.words))
    return data.words[random_index]

def encode_word(word, letters):
    return "".join([letter if letter in letters else '_' for letter in word])
