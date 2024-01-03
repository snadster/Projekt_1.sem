from board import *
from move import *
from dataclasses import dataclass
from typing import Any

@dataclass
class Node:
    children: list[Any]
    parent: Any
    data: Board
    value: int # hvor meget har man lyst til at være i den givne bræt-tilstand
    move: Move
    
def make_tree(r: Node, depth: int) -> None:
    """Make a tree with depth chosen by player."""
    list_of_nodes = [r]
    while height(r) <= depth + 1:
        current = r
        for m in legal_moves(current.data):
            list_of_nodes.append(add_child(current, m))
        list_of_nodes = (list_of_nodes[1:])
        current = list_of_nodes[0]
        

def make_root(b: Board) -> Node:
    """Start a tree."""
    n = Node([], None, copy(b), 0, None)
    return n

def _max(n: int) -> bool:
    """Determine whether a node is a max node"""
    return layer(n) % 2 == 0

def layer(n: Node) -> int:
    """Return the current layer"""
    current_layer = 0
    current_node = n
    while n.parent != None:
        current_node = n.parent
        current_layer = current_layer + 1
    return current_layer 

def add_child(p: Node, m: Move) -> None:
    """Add a child to the given parent. The order is irrelevant."""
    p.children.append(_child(p, m))
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

def _child(pap: Node, m: Move) -> Node:
    new_board = _temp_board(m, pap.data)
    child = Node([], pap, new_board, heu(new_board), m)
    return child

def _temp_board(m: Move, b: Board) -> Board:
    c = copy(b)
    move(m, c)
    return copy(c)

def heu(b: Board) -> int:
    """Determine the value of a node. This is the heuristic function."""
    counter = 0
    if white_plays:
        for opponent in black(b):
            counter = counter + 1
    else:
        for opponent in white(b):
            counter = counter + 1
    return 12 - counter

def height(n: Node) -> int:
    """Determine the height of the tree."""
    h = 0
    for node in n.children:
        h = max(height(node), h)
        h = h + 1
    return h

def next_move(b: Board, depth: int) -> Move:
    """Execute the optimal move for the player."""
    root = make_root(b)
    make_tree(root, depth)
    best = root.children[0]
    for c in root.children:
        if c.value > best.value:
            best = c
    return best.move
