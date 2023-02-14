import logging
import configparser
from dungeon_dragon.control.functions import (
    find_player,
    type_check
)

from dungeon_dragon.view.ground import Ground
from painless.helper.enum import sign_of_game

# logging file is config and handle here
config = configparser.ConfigParser()
config.read('config\\logging.toml')
logger = logging.getLogger(__name__)
file_h = logging.FileHandler(config['player']['file_handler'])
file_f = logging.Formatter(config['player']['file_formatter'])
file_h.setFormatter(file_f)
file_h.setLevel(logging.INFO)
logger.addHandler(file_h)
logger.setLevel(logging.INFO)
'''
name of the function which start with [move], controls the user
'''


class Character():
    """
    this class is parent of dragon and player class
    and define the position of player_sign
    for example detect the position of player to be in x = 1 and y = 2 etc.
    """

    def position(self, play_ground: list, random_X: int, random_Y: int, sign: str) -> list: # noqa E501
        """this function define position of different roles
        in the ground of the game

        Parameters
        ----------
        play_ground : list : the ground of play

        random_X: int : position of player in x_axis

        random_Y: int : position of player in y_axis

        sign: str : avatar of character


        Returns
        -------
        play_ground: int : return the ground of the game

        """
        play_ground[random_X][random_Y] = sign
        return play_ground


class Player(Character):
    """ """

    def __init__(self, user_name: str, user_avatar: str, level_number: int):
        self.user_name = user_name
        self.user_avatar = user_avatar
        self.level_number = level_number

    def move_left(self, play_ground: list, cross_player: str, life_counter: int, ground: Ground) -> list: # noqa E501
        """
        this function define ability of player and how player move left

        Parameters
        ----------
        play_ground : list : the ground of play

        cross_player : str : the button which user press (left, right,...)

        life_counter : int : the situation of player life

        Returns
        -------
        play_ground: list : return the ground of the game

        """
        if cross_player == 'left':
            row, col = find_player.find_player(self.user_avatar, play_ground, self.level_number) # noqa E501
            x_dragon, y_dragon = find_player.find_player(sign_of_game.DRAGON_SIGN.value, play_ground, self.level_number) # noqa E501
            x_position: int = row
            y_position: int = col - 1
            logger.info(f'{self.user_name} press {cross_player} and now its location is {x_position},{y_position}') # noqa E501
            if y_position < 0 or (x_position == x_dragon and y_position == y_dragon): # noqa E501
                ground.print_ground(play_ground, life_counter)
            else:
                play_ground[row][col] = '()' # noqa E501
                play_ground[x_position][y_position] = self.user_avatar # noqa E501
                ground.print_ground(play_ground, life_counter)


    def move_right(self, play_ground: list, cross_player: str, life_counter: int,  ground: Ground) -> list: # noqa E501
        """
        this function define ability of player and how player move right

        Parameters
        ----------
        play_ground : list : the ground of play

        cross_player : str : the button which user press (left, right,...)

        life_counter : int : the situation of player life

        Returns
        -------
        play_ground: list : return the ground of the game

        """
        if cross_player == 'right':
            row, col = find_player.find_player(self.user_avatar, play_ground, self.level_number) # noqa E501
            x_dragon, y_dragon = find_player.find_player(sign_of_game.DRAGON_SIGN.value, play_ground, self.level_number) # noqa E501
            x_position: int = row
            y_position: int = col + 1
            logger.info(f'{self.user_name} press {cross_player} and now its location is {x_position},{y_position}') # noqa E501
            if y_position > self.level_number-1 or (x_position == x_dragon and y_position == y_dragon ): # noqa E501
                ground.print_ground(play_ground, life_counter)
            else:
                play_ground[row][col] = '()' # noqa E501
                play_ground[x_position][y_position] = self.user_avatar # noqa E501
                ground.print_ground(play_ground, life_counter)


    def move_down(self, play_ground: list, cross_player: str, life_counter: int,  ground: Ground) -> list: # noqa E501
        """
        this function define ability of player and how player down

        Parameters
        ----------
        play_ground : list : the ground of play

        cross_player : str : the button which user press (left, right,...)

        life_counter : int : the situation of player life

        Returns
        -------
        play_ground: list : return the ground of the game

        """
        if cross_player == 'down':
            row, col = find_player.find_player(self.user_avatar, play_ground, self.level_number) # noqa E501
            x_dragon, y_dragon = find_player.find_player(sign_of_game.DRAGON_SIGN.value, play_ground, self.level_number) # noqa E501
            x_position: int = row + 1
            y_position: int = col
            logger.info(f'{self.user_name} press {cross_player} and now its location is {x_position},{y_position}') # noqa E501
            if x_position > self.level_number-1 or (x_position == x_dragon and y_position == y_dragon ): # noqa E501
                ground.print_ground(play_ground, life_counter)
            else:
                play_ground[row][col] = '()' # noqa E501
                play_ground[x_position][y_position] = self.user_avatar # noqa E501
                ground.print_ground(play_ground, life_counter)


    def move_up(self, play_ground: list, cross_player: str, life_counter: int,  ground: Ground) -> list: # noqa E501
        """
        this function define ability of player and how player move up

        Parameters
        ----------
        play_ground : list : the ground of play

        cross_player : str : the button which user press (left, right,...)

        life_counter : int : the situation of player life

        Returns
        -------
        play_ground: list : return the ground of the game

        """
        if cross_player == 'up':
            row, col = find_player.find_player(self.user_avatar, play_ground, self.level_number) # noqa E501
            x_dragon, y_dragon = find_player.find_player(sign_of_game.DRAGON_SIGN.value, play_ground, self.level_number) # noqa E501
            x_position: int = row - 1
            y_position: int = col
            logger.info(f'{self.user_name} press {cross_player} and now its location is {x_position},{y_position}') # noqa E501
            if x_position < 0 or ( y_position == y_dragon and x_position == x_dragon): # noqa E501
                ground.print_ground(play_ground, life_counter)
            else:
                play_ground[row][col] = '()' # noqa E501
                play_ground[x_position][y_position] = self.user_avatar # noqa E501
                ground.print_ground(play_ground, life_counter)


    def move_check(self, play_ground: list, cross_player: str, life_counter: int,  ground: Ground) -> None: # noqa E501
        """
        this function define check input of user and authenticate it

        Parameters
        ----------
        play_ground : list : the ground of play

        cross_player : str : the button which user press (left, right,...)

        life_counter : int : the situation of player life

        Returns
        -------
        None

        """
        if cross_player not in ['left', 'right', 'up', 'down', 'help', 'adv', 'bombu', 'fire', 'bombd','']: # noqa E501
            print('please enter correct sign')
            type_check.type_check(cross_player)
            # ground = Ground(self.user_avatar)
            ground.print_ground(play_ground, life_counter)


    def move_help(self, play_ground: list, cross_player: str, life_counter: int, ground: Ground) -> None: # noqa E501
        """
        this, help player to find dungeon

        Parameters
        ----------
        play_ground : list : the ground of play

        cross_player : str : the button which user press (left, right,...)

        life_counter : int : the situation of player life

        Returns
        -------
        play_ground: list : return the ground of the game

        """

        if cross_player == 'help':
            print("========================================================================================") # noqa E501
            print(''' for playing use this method
                    North : up
                    South : down
                    East : left
                    West : right
                    bombd : throw bomb to down
                    bombu : throw bomb to up
                    fire : explode bomb one by one

                    ''')
            x_dungeon, y_dungeon = find_player.find_player(sign_of_game.DUNGEON_SIGN.value, play_ground, self.level_number) # noqa E501
            x_player, y_player = find_player.find_player(self.user_avatar, play_ground, self.level_number) # noqa E501
            print(f'You can find dungeon {  abs(x_dungeon - x_player)} home upper or downer from player') # noqa E501
            print(f'You can find dungeon { abs(y_dungeon - y_player)} home lefter or righter from player') # noqa E501
            print("========================================================================================") # noqa E501
            ground.print_ground(play_ground, life_counter)
