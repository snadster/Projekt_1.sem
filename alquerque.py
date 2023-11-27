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
