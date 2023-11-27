from board import *
from move import *
from minimax import next_move 

def start_game() -> None:
    """starts the game"""
    print("Hear ye hear ye! 'Tis thine ancient game, foretold by the prophecy of yore!"
          "Thou shalt denounce the wench from which you came, and journey, brave adventurer,"
          "to our lands of conflict and foes!"
          "Thou must choose a side, be brave as you go on, this game of Alquerque may last long!"
          "This quest may become quite fearsome! Upon thy journey the magical machine may ask of you,"
          "enter upon thine board of keys, a single y for yay, or an n for nay!")
    comp_white = input("Does thou wish the magical machine to play white? y or n? ").lower()
    if comp_white == 'y':
        comp_white = True
    else:
        comp_white = False
    comp_black = input("Does thou wish the magical machine to play black? y or n? ").lower()
    if comp_black == 'y':
        comp_black = True
    else:
        comp_black = False
    if (comp_white == False or comp_black == False):
        comp_diff = input("Thine enemy be quick to strike,"
                          "alas you may decide if his bravery is wondrous,"
                          "or his pants be yellow! Thine decision may be made upon entering,"
                          "to your board of keys, a numeral that exists between 0 and 7! ")

def show_board() -> None:
    """Prints a visual representation of the board"""
    print("┌───────────────────-─────┐")
    print("│ ",_convert(1),"─",_convert(2),"─",_convert(3),"─",_convert(4),"─",_convert(5),"│")
    print("│  ┃ \ ┃ / ┃ \ ┃ / ┃  │")
    print("│ ",_convert(6),"─",_convert(7),"─",_convert(8),"─",_convert(9),"─",_convert(10),"│")
    print("│  ┃ / ┃ \ ┃ / ┃ \ ┃  │")
    print("│ ",_convert(11) ,"─",_convert(12) ,"─",_convert(13) ,"─",_convert(14) ,"─",_convert(15) ,"│") 
    print("│  ┃ \ ┃ / ┃ \ ┃ / ┃  │")
    print("│ ",_convert(16) ,"─",_convert(17) ,"─",_convert(18) ,"─",_convert(19) ,"─",_convert(20) ,"│")
    print("│  ┃ / ┃ \ ┃ / ┃ \ ┃  │")
    print("│ ",_convert(21) ,"─",_convert(22) ,"─",_convert(23) ,"─",_convert(24) ,"─",_convert(25) ,"│")
    print("└────────────────────-────┘")
        

def indices_board() -> None:
    """Prints the board with the indeces"""
    print("┌───────────────-─────────┐")
    print("│ ",1," ─",2," ─",3," ─",4," ─",5," │")
    print("│  ┃ \ ┃ / ┃ \ ┃ / ┃   │")
    print("│ ",6," ─",7," ─",8," ─",9," ─",10,"│")
    print("│  ┃ / ┃ \ ┃ / ┃ \ ┃   │")
    print("│ ",11 ,"─",12 ,"─",13 ,"─",14 ,"─",15,"│") 
    print("│  ┃ \ ┃ / ┃ \ ┃ / ┃   │")
    print("│ ",16 ,"─",17 ,"─",18 ,"─",19 ,"─",20,"│")
    print("│  ┃ / ┃ \ ┃ / ┃ \ ┃   │")
    print("│ ",21 ,"─",22 ,"─",23 ,"─",24 ,"─",25,"│")
    print("└──────────────-──────────┘")

def _convert(n: int) -> str:
    """Converts black or white to their respective knight characters"""
    if n in black(b):
        return '\u265E'
    if n in white(b):
        return '\u2658'
    else:
        return n
