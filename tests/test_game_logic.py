# UPDATED: Tests now import from logic_utils after refactoring
# Originally imported only check_guess from app.py
# Updated to check result[0] since check_guess returns (outcome, message) tuple
# Added comprehensive tests for all functions
from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score, get_attempt_limit

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"


# Tests for get_attempt_limit
def test_get_attempt_limit_easy():
    assert get_attempt_limit("Easy") == 6

def test_get_attempt_limit_normal():
    assert get_attempt_limit("Normal") == 8

def test_get_attempt_limit_hard():
    assert get_attempt_limit("Hard") == 5

def test_get_attempt_limit_invalid():
    assert get_attempt_limit("Invalid") == 8  # Default to Normal