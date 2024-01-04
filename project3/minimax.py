from board import *
from move import *
from dataclasses import dataclass
from typing import Any

@dataclass
class Node:
    children: list[Any]
    parent: Any
    data: Board
    value: int #Den heuristiske værdi
    move: Move
    
def make_tree(r: Node, depth: int) -> None:
    """Make a tree with depth chosen by player."""
    if depth >= 1:
        _make_tree(r)
    elif depth >= 2:
        for child in r.children:
            _make_tree(child)
    elif depth >= 3:
        for grandchild in r.children.children:
            _make_tree(grandchild)
    elif depth >= 4:
        for grandchild1 in r.children.children.children:
            _make_tree(grandchild1)
    elif depth >= 5:
        for grandchild2 in r.children.children.children.children:
            _make_tree(grandchild2)
    elif depth >= 6:
        for grandchild3 in r.children.children.children.children.children:
            _make_tree(grandchild3)
    elif depth >= 7:
        for grandchild4 in r.children.children.children.children.children.children:
            _make_tree(grandchild4)
        
def _make_tree(n: Node) -> None:
    for m in legal_moves(n.data):
        add_child(n, m) 
        


def make_root(b: Board) -> Node:
    """Make the root of the tree.
    >>> make_root(b)
    Node(children=[], parent=None,
    data=Board(board=[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    move=1), value=0, move=None)
    """
    n = Node([], None, copy(b), 0, None)
    return n

def _max(n: int) -> bool:
    """Determine whether a node is a max node.
    _max(make_root(b))
    True
    """
    return layer(n) % 2 == 0

def layer(n: Node) -> int:
    """Return the current layer for a node.
    >>> layer(make_root(b))
    0
    """
    current_layer = 0
    current_node = n
    while n.parent != None:
        current_node = n.parent
        current_layer = current_layer + 1
    return current_layer 

def add_child(p: Node, m: Move) -> Node:
    """Add a child to the given parent. The order is irrelevant."""
    new_child = _child(p, m)
    p.children.append(new_child)
    if _max(p):
        highest = 0
        for c in p.children:
            if c.value > highest:
                highest = c.value
        p.value = highest
    else:
        lowest = 12
        for c in p.children:
            if c.value < lowest:
                lowest = c.value
        p.value = lowest
    return new_child

def _child(pap: Node, m: Move) -> Node:
    """Create an entirely new node."""
    new_board = _temp_board(m, pap.data)
    child = Node([], pap, new_board, heu(new_board), m)
    return child

def _temp_board(m: Move, b: Board) -> Board:
    """Return a temporary board of the present board."""
    c = copy(b)
    move(m, c)
    return copy(c)

def heu(b: Board) -> int:
    """Determine the value of a node. This is the heuristic function.
    The best value is 12 and the worst 0.
    >>> heu(b)
    0
    """
    counter = 0
    if white_plays:
        for opponent in black(b):
            counter = counter + 1
    else:
        for opponent in white(b):
            counter = counter + 1
    return 12 - counter

def height(n: Node) -> int:
    """Determine the height of the tree.
    >>> height(make_root(b))
    0
    """
    h = 0
    for node in n.children:
        h = max(height(node), h)
        h = h + 1
    return h

def next_move(b: Board, depth: int) -> Move:
    """Find the optimal move for the autoplayer."""
    root = make_root(b)
    make_tree(root, depth)
    best = root.children[0]
    for c in root.children:
        if c.value > best.value:
            best = c
    return best.move
