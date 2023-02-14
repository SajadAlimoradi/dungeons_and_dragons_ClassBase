# from enum import Enum
from painless.helper.enum import player


def user_player(user_avatar: str):
    """

    Parameters
    ----------
    user_avatar : avatar of player which save in enum class


    Returns
    -------
    this function return the avatar which player choose as value

    """
    while True:
        if user_avatar == 'one':
            return player.one.value
            break
        elif user_avatar == 'two':
            return player.two.value
            break
        elif user_avatar == 'three':
            return player.three.value
            break
        else:
            print("Please enter correct value")
