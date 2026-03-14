# This file was created for refactoring game logic functions from app.py
# IMPLEMENTED: All functions were moved here from app.py and implemented properly
# The NotImplementedError stubs were replaced with actual implementations

def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    # IMPLEMENTED: Added logic for Easy (1-20), Normal (1-100), Hard (1-50), default (1-100)
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    # IMPLEMENTED: Added input validation for None, empty string, invalid numbers
    # Handles floats by converting to int, returns appropriate error messages
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # IMPLEMENTED: Fixed inverted hints bug - now correctly identifies high/low guesses
    # Returns tuple of (outcome, message) for proper hint display
    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess < secret:
        return "Too Low", "� Go HIGHER!"
    else:
        return "Too High", "📉 Go LOWER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    # IMPLEMENTED: Added scoring logic with win bonuses, penalties for wrong hints
    # Win: 100 - 10*attempts (min 10), Too High: +/-5 based on even/odd attempts, Too Low: -5
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score


def get_attempt_limit(difficulty: str):
    """Return the number of attempts allowed for a given difficulty."""
    attempt_limit_map = {
        "Easy": 6,
        "Normal": 8,
        "Hard": 5,
    }
    return attempt_limit_map.get(difficulty, 8)  # Default to Normal
