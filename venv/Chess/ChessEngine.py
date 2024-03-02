"""
This  is responsible for staring all the information about the current state of a chess game.
It will also be responsible for determining the valid moves at the current state. Iw will keep a move log.
"""


class GameState():
    def __init__(self):
        """
        board is a 8x8 2d list, each element of the list has 2 characters.
        First letter is about color ("b" or "w"), second one is about type of
        the piece ('K', 'Q', 'R', 'B', 'N', 'P').
        "--" - represents empty space with no piece
        """
        self.board = [
        ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
        ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
        ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
        self.whiteToMove = True
        self.moveLog = []

class Move():
    def __init__(self, startSq, endSq, board):

class Test():
    def __init__(self):
        def test():


















