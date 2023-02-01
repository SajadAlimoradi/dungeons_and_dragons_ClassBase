def type_check(cross_player: str):
    """
    this function check user 's input
    Parameters
    ----------
    cross_player: str :  the button which user press (left, right,...)


    Returns
    -------
    this function return nothing
    """
    if cross_player == '':
        print("\nHow can i guess what do you want!! DADASH or ABJI \n")
    elif cross_player[0] == 'l':
        print("\nDo you mean 'left'?\n")
    elif cross_player[0] == 'r':
        print("\nDo you mean 'right'?\n")
    elif cross_player[0] == 'u':
        print("\nDo you mean 'up'?\n")
    elif cross_player[0] == 'd':
        print("\nDo you mean 'down'?\n")
    elif cross_player[0] == 'b':
        print("\nDo you mean 'bomb'?\n")
    elif cross_player[0] == 'f':
        print("\nDo you mean 'fire'?\n")
    else:
        print("\nHow can i guess what do you want!! DADASH or ABJI \n")
