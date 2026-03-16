#FIX: added necessary import statements
import random 

#FIX: refactored get_range_for_difficulty function
def get_range_for_difficulty(difficulty: str):
    if difficulty == "Easy":
        return 1, 20
    elif difficulty == "Normal":
        return 1, 100
    elif difficulty == "Hard":
        return 1, 500
    else:
        raise ValueError("Invalid difficulty level. Choose Easy, Normal, or Hard.")

#FIX: refactored parse_guess function 
def parse_guess(raw: str):
    """
    Parses the user's guess input and validates it.
    Returns a tuple (is_valid, value, message).
    """
    if raw is None or raw.strip() == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))  # Convert float-like strings to integers
        else:
            value = int(raw)
        return True, value, None
    except ValueError:
        return False, None, "Invalid input. Please enter a number."

#FIX: refactored check_guess function
def check_guess(guess: int, target: int):
    """
    Compares the user's guess to the target number.
    Returns a tuple (is_correct, message).
    """
    if guess < target:
        return False, "Too low!"
    elif guess > target:
        return False, "Too high!"
    else:
        return True, "Correct!"

#FIX: refactored update_score function
def update_score(current_score: int, is_correct: bool):
    """
    Updates the score based on whether the guess was correct.
    Returns the updated score.
    """
    if is_correct:
        return current_score + 1
    else:
        return max(0, current_score - 1)