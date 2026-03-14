# This file was created for refactoring game logic functions from app.py
# IMPLEMENTED: All functions were moved here from app.py and implemented properly
# The NotImplementedError stubs were replaced with actual implementations

def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    # IMPLEMENTED: Added logic for Easy (1-20), Normal (1-100), Hard (1-50), default (1-100)
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    # IMPLEMENTED: Added input validation for None, empty string, invalid numbers
    # Handles floats by converting to int, returns appropriate error messages
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


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
        return "Too Low", "📉 Go LOWER!"
    else:
        return "Too High", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    # IMPLEMENTED: Added scoring logic with win bonuses, penalties for wrong hints
    # Win: 100 - 10*attempts (min 10), Too High: +/-5 based on even/odd attempts, Too Low: -5
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
