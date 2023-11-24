from dataclasses import dataclass
@dataclass
class Move:
    src: int
    trg: int

def make_move(src: int, trg: int) -> Move:
    """Makes the new move between the given squares."""
    return Move(src, trg)

def source(m: Move) -> int:
    """Returns the 'from'-square in a move"""
    return m.src

def target(m: Move) -> int:
    """Returns the 'to'-square in a move"""
    return m.trg
