import random

class WordDatabase:
    def __init__(self, words):
        self.words = words

    def get_random_word(self):
        return random.choice(self.words)
