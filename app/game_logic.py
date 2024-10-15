def determine_winner(choice1: str, choice2: str) -> int:
    if choice1 == choice2:
        return 0
    if (choice1 == "rock" and choice2 == "scissors") or \
       (choice1 == "scissors" and choice2 == "paper") or \
       (choice1 == "paper" and choice2 == "rock"):
        return 1
    return -1