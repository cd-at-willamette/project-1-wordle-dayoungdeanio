########################################
# Name: D'Ante Dean
# Collaborators (if any): Nobody.
# Estimated time spent (hr):3 Days.
########################################

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import *  # ENGLISH_WORDS, is_english_word
import random

def get_random_word():
    # Generate a random five-letter word 
    word = ""
    while len(word) != 5:
        word = random.choice(ENGLISH_WORDS)
    return word

def wordle():
    secret_word = get_random_word()

    def enter_action():
        current_row = gw.get_current_row()

        # get the guessed word from the row
        word = ''.join([gw.get_square_letter(current_row, col) for col in range(N_COLS)]).lower()

        # check if the word is English 
        if not is_english_word(word):
            gw.show_message("Not in word list")
            return

        # Milestone 2: Color the boxes
        used_letters = list(secret_word)  # Copy of the secret word to track used letters
        correct_guesses = 0  # correct letters

        #Color the correct green
        for i in range(N_COLS):
            if word[i] == secret_word[i]:
                gw.set_square_color(current_row, i, CORRECT_COLOR)
                used_letters[i] = None  # Mark letter as used
                correct_guesses += 1  # the count of correct guesses

        # Color the misplaced letters yellow
        for i in range(N_COLS):
            if word[i] != secret_word[i]:
                if word[i] in used_letters:
                    gw.set_square_color(current_row, i, PRESENT_COLOR)
                    used_letters[used_letters.index(word[i])] = None  # Mark letter as used
                else:
                    gw.set_square_color(current_row, i, MISSING_COLOR)  # incorrect letter

        # Milestone 5: Color the keys on the virtual keyboard
        for i in range(N_COLS):
            letter = word[i].upper()
            current_color = gw.get_key_color(letter)
            
            if word[i] == secret_word[i]:
                # letter is correct , color it green
                gw.set_key_color(letter, CORRECT_COLOR)
            elif word[i] in secret_word:
                # letter is misplaced, color it yellow
                if current_color != CORRECT_COLOR:
                    gw.set_key_color(letter, PRESENT_COLOR)
            else:
                # letter is wrong, color it grey
                if current_color != CORRECT_COLOR and current_color != PRESENT_COLOR:
                    gw.set_key_color(letter, MISSING_COLOR)

        # Milestone 4: win or loss
        if correct_guesses == N_COLS:
            gw.show_message("Congratulations! You've guessed the word!")
            gw.set_current_row(N_ROWS)  # Disable further input by moving the current row past the last row
            return

        
        if current_row < N_ROWS - 1:
            gw.set_current_row(current_row + 1)
        else:
            gw.show_message(f"Game Over! The correct word was: {secret_word}")
            gw.set_current_row(N_ROWS)  # Disable further input by moving the current row past the last row

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup boilerplate
if __name__ == "__main__":
    wordle()
