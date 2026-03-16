import pytest
from logic_utils import check_guess

@pytest.mark.parametrize(
    "guess, target, expected_result, expected_message",
    [
        (5, 10, False, "Too low!"),  # Guess is lower than the target
        (15, 10, False, "Too high!"),  # Guess is higher than the target
        (10, 10, True, "Correct!"),  # Guess matches the target
    ],
)
def test_check_guess(guess, target, expected_result, expected_message):
    """
    Test the check_guess function to ensure it correctly identifies
    whether the guess is too high, too low, or correct.
    """
    result, message = check_guess(guess, target)
    assert result == expected_result, f"Expected result {expected_result}, got {result}"
    assert message == expected_message, f"Expected message '{expected_message}', got '{message}'"
    
def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"
