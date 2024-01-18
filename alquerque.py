from board import *
from move import *
from minimax import next_move


def start_game() -> None:
    """Start the game"""
    print("Hear ye hear ye!"
	  "’Tis thine ancient game… "
          "Thou shalt journey, proud adventurer; "
	  "Be brave as you go on! this game of Alquerque may last long! "
          "'Tis the battefield upon which you will find your glory or perhaps your defeat! "
          "Take notice of thine possible moves "
          "and if thou wish to lay down thine arms, enter q upon thine board of keys. " )
    indices_board()
    show_board()
    comp_white = (input("Does thou wish the magical machine to play white? " 
			"a single y for yay, or an n for nay! ").lower())
    if comp_white == 'n':
        comp_white = False
    elif comp_white == 'y':
        comp_white = True
    elif comp_white == 'q':
        exit()
    else:
        print("Dear friend, 'twas not a choice. Give it another attempt! ")
        start_game()
    comp_black = input("Does thou wish the magical machine to play black? y or n? ").lower()
    if comp_black == 'n':
        comp_black = False
    elif comp_black == 'y':
        comp_black = True
    elif comp_black == 'q':
        exit()
    else:
        print("Dear friend, 'twas not a choice. Give it another attempt! ")
        start_game()
    if (comp_white or comp_black):
        comp_diff = input("Thine enemy be quick to strike, "
                          "but HOW quick? "
                          "Thine decision may be made upon entering, "
                          "to your board of keys, "
                          "a numeral that exists between 1 and 7! ").lower()
        if comp_diff == 'q':
            exit()
        elif not (0 < int(comp_diff) <= 7):
            print("Dear friend, 'twas not a choice. Give it another attempt! ")
            start_game()
        plays_game(comp_white, comp_black, int(comp_diff))
    else:
        plays_game(comp_white, comp_black, 0)

def plays_game(comp_white: bool, comp_black: bool, comp_diff: int) -> None:
    """Play the game"""
    if is_game_over(b):
        if black(b) == []:
            print("Brave battles were fought and brave battles were lost! "
                  "Here I must announce, that our White Knight has won! ")
        elif white(b) == []:
            print("Brave battles were fought and brave battles were lost! "
                  "Here I must announce, that our Black Knight has won! ")
        else:
            print("Battles are strenuous, and strategy flows a plenty. "
                  "Alas at this conjecture, our Knights are wounded and weary. "
                  "Neither may win and yet, neither may lose. The adventure is over, pick up your boots! ")
    else:
        if ((white_plays(b) and comp_white) or (not white_plays(b) and comp_black)):
            new_comp_move = next_move(b, comp_diff)
            move(new_comp_move, b)
            print("The magical machine moves knight", source(new_comp_move),"to field",  target(new_comp_move))
        else:
            player_move()
        show_board()
        plays_game(comp_white, comp_black, comp_diff)


def player_move() -> None:
    """Ask the player for a move, and update the board by making that move"""
    s = input('Which knight shall ride to battle? ').lower()
    if s == 'q':
        exit()
    t = input('Where upon should our knight ride? ').lower()
    if t == 'q':
        exit()
    upcoming_move = make_move(int(s), int(t))
    if is_legal(upcoming_move, b):
        move(upcoming_move, b)
    else: 
        print("Thine knight is lacking the bravery necessary for thy move, try another! ")


def show_board() -> None:
    """Print a visual representation of the board"""
    c = _convert
    print("┌─────────────────────┐")
    print("│ ",c(1),"─",c(2),"─",c(3),"─",c(4),"─",c(5)," │")
    print("│  │ \ │ / │ \ │ / │  │")
    print("│ ",c(6),"─",c(7),"─",c(8),"─",c(9),"─",c(10)," │")
    print("│  │ / │ \ │ / │ \ │  │")
    print("│ ",c(11) ,"─",c(12) ,"─",c(13) ,"─",c(14) ,"─",c(15) ," │") 
    print("│  │ \ │ / │ \ │ / │  │")
    print("│ ",c(16) ,"─",c(17) ,"─",c(18) ,"─",c(19) ,"─",c(20) ," │")
    print("│  │ / │ \ │ / │ \ │  │")
    print("│ ",c(21) ,"─",c(22) ,"─",c(23) ,"─",c(24) ,"─",c(25) ," │")
    print("└─────────────────────┘")
        

def indices_board() -> None:
    """Print the board with the indices"""
    print("┌─────────────────────────┐")
    print("│ ",1," ─",2," ─",3," ─",4," ─",5," │")
    print("│  │  \ │ /  │ \  │ /  │  │")
    print("│ ",6," ─",7," ─",8," ─",9,"─",10," │")
    print("│  │  / │ \  │ /  │ \  │  │")
    print("│ ",11,"─",12,"─",13,"─",14,"─",15,"│") 
    print("│  │  \ │ /  │ \  │ /  │  │")
    print("│ ",16,"─",17,"─",18,"─",19,"─",20,"│")
    print("│  │  / │ \  │ /  │ \  │  │")
    print("│ ",21,"─",22,"─",23,"─",24,"─",25,"│")
    print("└─────────────────────────┘")

def _convert(n: int) -> str:
    """Convert black or white to their respective knight characters"""
    if n in black(b):
        return '\u265E'
    if n in white(b):
        return '\u2658'
    else:
        return ' '

start_game()
