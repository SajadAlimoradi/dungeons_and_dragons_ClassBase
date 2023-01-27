level_game: dict = {
    'easy': 5,
    'medium': 8,
    'hard': 10
}


# search for player
def find_gaming_sign(func):
    """

    Parameters
    ----------
    func : this is first class object function that use this decoration


    Returns
    -------

    """
    def inner_find_gaming_sign(gaming_sign: str, play_ground: list, level_number: int): # noqa E501
        """

        Parameters
        ----------
        gaming_sign : name of character which we search


        Returns
        -------
        the inner function will return; we make decorate function here

        """
        role, play_ground, level_number = func(gaming_sign, play_ground, level_number) # noqa E501
        for row in range(level_number):
            for col in range(level_number):
                if play_ground[row][col] == role:
                    return row, col
                    break
        return None, None
    return inner_find_gaming_sign


@find_gaming_sign
def find_player(gaming_sign: str, play_ground: list, level_number: int):
    """

    Parameters
    ----------
    gaming_sign : name of character which we search


    Returns
    -------
    the sign of player send to decorator for finding it

    """
    return gaming_sign, play_ground, level_number
