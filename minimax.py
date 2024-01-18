from board import *
from move import *
from dataclasses import dataclass
import Any

@dataclass
class Node:
    children: list[Any]
    parent: Any
    data: Board
    value: int # hvor meget har man lyst til at være i den givne bræt-tilstand
    move: Move
    
def make_tree(r: Node, depth: int) -> None:
    """Make a tree with depth chosen by player."""
    current = r
    for m in legal_moves(current.data):
        add_child(current, m)
        
    # kalder make_root()
    # for hvert lovligt move for nuværende bræt, skal der tilføjes et barn til listen i roden. 
    # Der skal tilføjes det antal lag som svarer til sværhedsgraden. 

def make_root() -> Node:
    """Start a tree."""
    n = Node([], None, copy(b), 0, None)
    return n

def _max(n: int) -> bool:
    """Determine whether a node is a max node"""
    return layer % 2 == 0

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
    append.p.children(_child(p, m))
    if _max(p):
        p.value = max(p.children.value)
    else:
        p.value = min(p.children.value)

def _child(pap: Node, m: Move) -> Node:
    new_board = _temp_board(m, pap.data)
    child = Node([], pap, new_board, heu(new_board), m)
    return child

def _temp_board(m: move, b: Board) -> Board:
    return copy(move(m, copy(b)))

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

def best_move(tree: Any) -> Move:
    """Determine the optimal move for the given player by finding the highest or lowest value."""
    best = max(root.children.value)
    return best.move

def height(n: Node) -> int:
    """Determine the height of the tree."""
    h = 0
    for node in n.children:
        h = max(height(Node), h)
    return h + 1

def next_move(b: Board, depth: int) -> None:
    """Execute the optimal move for the player."""
    move(best_move(make_tree(root, depth)))


root = make_root()
