#!/usr/bin/python
import random


# players win if they both guess correctly. Plyer 1 knows what the sequence will be in advance, player 2
# does not.

def score_guesses(theanswer, guess1, guess2):
    if guess1 == guess2 == theanswer:
        return 1
    return 0

def get_player1_guess(sequence, history):
    """figure out what player 1 should guess given the sequence and history."""
    if not history:
        return sequence[1]
    pos = len(history)
    if history[pos - 1][1] != sequence[pos -1]: # incorrect last time, so previous player 1 is correct this time
        return history[pos- 1][0]
    # player 2 will guess 1 for sure, player 1 will also if it is correct, otherwise signal next answer
    if sequence[pos] == 1:
        return 1
    return sequence[pos +1]

def get_player2_guess(history, scored):
    """Figure out what player 2 should guess. Player2 only knows history and whetther he scored last round."""
    if not history:
        return 1
    pos = len(history)
    if not scored:
        return history[pos-1][0]
    return 1


if __name__ == '__main__':
    sequence = []
    history = []
    score = 0
    scored = False
    rounds = 10000
    for ii in range(rounds + 1):
        sequence.append(random.randint(0, 1))
    for ii in range(rounds):
        p1g = get_player1_guess(sequence, history)
        p2g = get_player2_guess(history, scored)
        guesses = (p1g, p2g)
        history.append(guesses)
        scored = score_guesses(sequence[ii], p1g, p2g)
        score += scored
        print('round', ii, 'guesses', guesses, 'theanswer', sequence[ii], 'scored', scored, 'score', score)


