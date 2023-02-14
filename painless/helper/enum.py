import os
from enum import Enum
from pathlib import Path


class player (Enum):
    """avatar which user can choose them are saved here."""
    one = '\U0001F47D'
    two = '\U0001F916'
    three = '\U0001F921'

# define player emoji


class sign_of_game(Enum):
    """ sign of different roles is defined here"""
    LOSING_SIGN: str = '\U0001F4A8'
    DUNGEON_SIGN: str = '\U0001F49A'
    DRAGON_SIGN: str = '\U0001F432'
    LIFE_SIGN: str = '\U0001F9E1'
    FIRE_SIGN: str = '\U0001F525'
    BOMB_SIGN: str = '\U0001F4A3'
    BOMB: str = '\U0001F4A3'


previous_directory = Path(__file__).resolve().parent.parent.parent


class sound_and_imgs_of_game(Enum):
    """path of voice are played, saved here."""
    comeonman: str = os.path.join(previous_directory, 'dungeon_dragon\\sounds', 'comeonman.mp3') # noqa E501
    cheat_code_1: str = os.path.join(previous_directory, 'dungeon_dragon\\sounds', 'cheat_code_1.mp3') # noqa E501
    sound_adv_1: str = os.path.join(previous_directory, 'dungeon_dragon\\sounds', 'adv1.mp3') # noqa E501
    img_adv_1: str = os.path.join(previous_directory, 'dungeon_dragon\\imgs', 'adv1.jpg') # noqa E501
    losing_life: str = os.path.join(previous_directory, 'dungeon_dragon\\sounds', 'losinglife.mp3') # noqa E501
    losing: str = os.path.join(previous_directory, 'dungeon_dragon\\sounds', 'losing.mp3') # noqa E501
    winning: str = os.path.join(previous_directory, 'dungeon_dragon\\sounds', 'winning.mp3') # noqa E501