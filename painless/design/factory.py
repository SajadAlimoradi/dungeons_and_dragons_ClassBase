import random
from enum import Enum

# from dragonV5 import level_number, user_avatar
from dungeon_dragon.view.ground import Ground


class sign_of_game(Enum):
    """ """
    LOSING_SIGN: str = '\U0001F4A8'
    DUNGEON_SIGN: str = '\U0001F49A'
    DRAGON_SIGN: str = '\U0001F432'
    LIFE_SIGN: str = '\U0001F9E1'
    BOMB: str = '\U0001F4A3'


player_X_Y = random.sample(range(8), 6)
play_ground = Ground('x').make_ground(8)


class Dragon:
    def __init__(self, x_position, y_position):
        self.X = x_position
        self.Y = y_position

    def put_role(self):
        a = play_ground[self.X][self.Y] = sign_of_game.DRAGON_SIGN.value
        return a


def get_role(role):
    roles = dict(dragon=Dragon(player_X_Y[0], player_X_Y[1]))
    return roles[role]


dd = get_role('dragon')
dd.put_role()
print(play_ground)
