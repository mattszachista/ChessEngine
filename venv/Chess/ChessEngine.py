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

    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.piecMoved
        self.moveLog.append(move) # log the move
        self.whiteToMove = not self.whiteToMove


class Move():
    # maps keys to values
    # key : value
    """4 lines below making notations on chess board. Depending of white or black moves it can
    reverse notation."""
    ranksToRows = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g':6, 'h': 7}
    colsToFiles = {v: k for k,v in filesToCols.items()}

    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]

    def getChessNotation(self):
        # added to make this like real chess notation
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)


    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks[r]





















