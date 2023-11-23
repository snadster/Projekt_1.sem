from move import *
from dataclasses import dataclass
import math
@dataclass
class Board:
    board: list[int]
    move: int

def make_board() -> Board:
    """Return a new board."""
    return Board([0,
                  1,1,1,1,1,
                  1,1,1,1,1,
                  1,1,0,2,2,
                  2,2,2,2,2,
                  2,2,2,2,2],
                 1)

def white_plays(b: Board) -> bool:
    """Check if it is white's turn to play.
    >>> white_plays(b)
    True
    >>> white_plays(b)
    False
    """
    return b.move % 2 == 1

def white(b: Board)-> list[int]:
    """Return a list containing the indices of every white piece.
    >>> white(b)
    [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    >>> white(b)
    []
    """
    white_indices = []
    for i in range(0, len(b.board)):
        if b.board[i] == white_piece:
            white_indices.append(i)
    return white_indices

def black(b: Board)-> list[int]:
    """Return a list containing the indices of every black piece.
    >>> black(b)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    >>> black(b)
    []
    """
    black_indices = []
    for i in range(0, len(b.board)):
        if b.board[i] == black_piece:
            black_indices.append(i)
    return black_indices

def is_game_over(b: Board) -> bool:
    """Determine whether the game is over.
    >>> is_game_over(b)
    True
    >>> is_game_over(b)
    False
    """
    res = False
    if list(filter(lambda x: x == black_piece, b.board)) == []:
        res = True
    if list(filter(lambda y: y == white_piece, b.board)) == []:
        res = True
    if legal_moves(b) == []:
            res = True
    return res

def copy(b: Board) -> Board:
    """Return a copy of the given board.
    >>> copy(b)
    Board(board=[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], move=1)
    """
    copy = [item for item in b.board]
    return Board(copy, b.move)

def move(m: Move, b: Board) -> None:
    """Update the board by simulating the given move."""
    if is_legal(m, b):
        if white_plays(b):
            b.board[target(m)] = white_piece
            b.board[source(m)] = empty_space
        else:
            b.board[target(m)] = black_piece
            b.board[source(m)] = empty_space
        if not(4 <= abs(source(m) - target(m)) <= 6):
            b.board[(source(m) + target(m))//2] = empty_space
    b.move = b.move + 1

def is_legal(m: Move, b: Board) -> bool:
    """Check if the given move is a legal move on the given
    board.
    >>> is_legal(m, b)
    False
    >>> is_legal(m,b)
    True
    """
    legal = False
    if 1 <= target(m) <= 25 and b.board[source(m)] != empty_space:
        if white_plays(b):
            if (row(source(m)) - row(target(m)) == 1 and source(m) - target(m) in (-6, -5, -4)):
                    legal = True
        else:
            if row(source(m)) - row(target(m)) == -1 and source(m) - target(m) in (6, 5, 4):
                legal = True
        if row(source(m)) - row(target(m)) in (0, 2):
            if source(m) - target(m) in (-12, -10, - 8, -2, 2, 8, 10, 12):
                legal = True
    return legal  

def row(n:int)->int:
    """Returns the row a piece is located on.
    >>> row(5)
    1
    """
    return math.ceil(n/5)
                

def legal_moves(b: Board) -> list[Move]:
    """Return a list containing all the legal moves
    from the given board.
    >>> legal_moves(b)
    [Move(src=1, trg=3), Move(src=2, trg=4), Move(src=3, trg=1), Move(src=3, trg=5)]
    """
    moves = []
    for i in range (1, 26):
        for j in range (1, 26):
            current_move = make_move(i, j)
            if is_legal(current_move, b):
                moves.append(current_move)
    return moves
        

    
    
white_piece = 2
black_piece = 1
empty_space = 0
b = make_board()
 
