from dungeon_dragon.control.functions import find_player
from painless.helper.enum import sign_of_game

def x_move_dragon(play_ground: list, life_counter: int, user_avatar: str, level_number: int) -> list: # noqa E501
    """

    control moving of dragon because of smell and power

    Parameters
    ----------
    play_ground: list : the ground of play

    life_counter: int : the situation of player life

    user_avatar: str : the avatar of user

    level_number: int : the level of the game which player choose

    Returns
    -------
    this function return the ground of the game
    """
    x_player, y_player = find_player.find_player(user_avatar, play_ground, level_number) # noqa E501
    x_dragon, y_dragon = find_player.find_player(sign_of_game.DRAGON_SIGN.value, play_ground, level_number) # noqa E501
    if x_player > x_dragon:
        x_new_dragon_step = x_dragon + 1
        if x_new_dragon_step != x_player or y_dragon != y_player:
            play_ground[x_dragon][y_dragon] = '()' # noqa E501
            play_ground[x_new_dragon_step][y_dragon] = sign_of_game.DRAGON_SIGN.value # noqa E501
    elif x_player < x_dragon:
        x_new_dragon_step = x_dragon - 1
        if x_new_dragon_step != x_player or y_dragon != y_player:
            play_ground[x_dragon][y_dragon] = '()' # noqa E501
            play_ground[x_new_dragon_step][y_dragon] = sign_of_game.DRAGON_SIGN.value # noqa E501
    else:
        pass
    return play_ground


def y_move_dragon(play_ground: list, life_counter: int, user_avatar: str, level_number: int) -> list: # noqa E501
    """

    control moving of dragon because of smell and power

    Parameters
    ----------
    play_ground: list : the ground of play

    life_counter: int : the situation of player life

    user_avatar: str : the avatar of user

    level_number: int : the level of the game which player choose

    Returns
    -------
    this function return the ground of the game
    """

    x_player, y_player = find_player.find_player(user_avatar, play_ground, level_number) # noqa E501
    x_dragon, y_dragon = find_player.find_player(sign_of_game.DRAGON_SIGN.value, play_ground, level_number) # noqa E501
    if y_player > y_dragon:
        y_new_dragon_step: int = y_dragon + 1
        if y_new_dragon_step != y_player or x_dragon != x_player:
            play_ground[x_dragon][y_dragon] = '()' # noqa E501
            play_ground[x_dragon][y_new_dragon_step] = sign_of_game.DRAGON_SIGN.value # noqa E501
    elif y_player < y_dragon:
        y_new_dragon_step = y_dragon - 1
        if y_new_dragon_step != y_player or x_dragon != x_player:
            play_ground[x_dragon][y_dragon] = '()' # noqa E501
            play_ground[x_dragon][y_new_dragon_step] = sign_of_game.DRAGON_SIGN.value # noqa E501
    else:
        pass
    return play_ground
