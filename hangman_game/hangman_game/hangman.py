import random

class HangmanGame:
    def __init__(self, max_attempts=6, max_score=100):
        self.score = 0
        self.hidden_word = ""
        self.guessed_letters = ""
        self.feedback_message = ""
        self.game_over = False
        self.game_won = False
        self.game_lost = False
        self.max_attempts = max_attempts
        self.remaining_attempts = max_attempts
        self.max_score = max_score
        self.current_score = 0

    def generate_word(self):
        word_database = WordDatabase()
        self.hidden_word = word_database.get_random_word()

    def make_guess(self, letter):
        if letter in self.hidden_word:
            self.guessed_letters += letter
            self.feedback_message = "Correct guess!"
            self.update_score()
            self.update_progress()
            self.check_game_won()
        else:
            self.remaining_attempts -= 1
            self.feedback_message = "Incorrect guess!"
            self.check_game_lost()

    def is_game_over(self):
        return self.game_over

    def is_game_won(self):
        return self.game_won

    def is_game_lost(self):
        return self.game_lost

    def get_feedback_message(self):
        return self.feedback_message

    def get_hidden_word(self):
        return self.hidden_word

    def get_remaining_attempts(self):
        return self.remaining_attempts

    def get_current_score(self):
        return self.current_score

    def get_max_score(self):
        return self.max_score

    def update_score(self):
        self.current_score += 10

    def update_progress(self):
        progress = ""
        for letter in self.hidden_word:
            if letter in self.guessed_letters:
                progress += letter
            else:
                progress += "_"
        self.hidden_word = progress

    def check_game_won(self):
        if "_" not in self.hidden_word:
            self.game_over = True
            self.game_won = True

    def check_game_lost(self):
        if self.remaining_attempts == 0:
            self.game_over = True
            self.game_lost = True


class WordDatabase:
    def __init__(self):
        self.words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]

    def get_random_word(self):
        return random.choice(self.words)
