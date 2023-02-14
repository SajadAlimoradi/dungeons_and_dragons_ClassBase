from dungeon_dragon.control.functions import (
    find_player,
    dragon_move,
)
import logging
import configparser
from dungeon_dragon.control.classes.win_loss import Win_Lose
from painless.helper.enum import sign_of_game

# logging file is config and handle here
config = configparser.ConfigParser()
config.read('config\\logging.toml')
logger = logging.getLogger(__name__)
file_h = logging.FileHandler(config['cheat_adv']['file_handler'])
file_f = logging.Formatter(config['cheat_adv']['file_formatter'])
file_h.setFormatter(file_f)
file_h.setLevel(logging.INFO)
logger.addHandler(file_h)
logger.setLevel(logging.INFO)


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


class Dragon(Character):
    """
    this class define ability of dragon and how dragon move or attack to player
    """
    def __init__(self, user_avatar, level_number):
        self.user_avatar = user_avatar
        self.level_number = level_number

    def __repr__(self):
        return 'This is a class for Dragon Character'


    def smelling_power(self, play_ground: list, attack_probability: float, life_counter: int) -> list: # noqa E501
        """
        detect the power of dragon smell and define how to act

        Parameters
        ----------
        play_ground : list : the ground of play

        attack_probability : float : probability of attack for dragon

        life_counter : int : the situation of player life

        Returns
        -------
        play_ground: int : return the ground of the game

        """
        row, col = find_player.find_player(self.user_avatar, play_ground, self.level_number) # noqa E501
        x_dragon, y_dragon = find_player.find_player(sign_of_game.DRAGON_SIGN.value, play_ground, self.level_number) # noqa E501
        if attack_probability < 0.3:
            if (abs(row - x_dragon) == 0) and (abs(col - y_dragon) > 2 and (abs(col - y_dragon) <= 5)): # noqa E501
                logger.info('Dragon Attack by Smelling Power')
                print("YOU ARE IN DANGER!")
                play_ground = dragon_move.y_move_dragon(play_ground, life_counter, self.user_avatar, self.level_number) # noqa E501

            elif (abs(col - y_dragon) == 0) and (abs(row - x_dragon) > 2) and (abs(row - x_dragon) <= 5): # noqa E501
                logger.info('Dragon Attack by Smelling Power')
                print("YOU ARE IN DANGER!")
                play_ground = dragon_move.x_move_dragon(play_ground, life_counter, self.user_avatar, self.level_number) # noqa E501
        return play_ground

    def hearing_power(self, play_ground: list, attack_probability: float, life_counter: int) -> int: # noqa E501
        """
        detect the power of dragon hearing and define how to act

        Parameters
        ----------
        play_ground: list : the ground of play

        attack_probability: float : probability of attack for dragon

        life_counter: int : the situation of player life


        Returns
        -------
        life_counter : int : the situation of player life

        """
        row, col = find_player.find_player(self.user_avatar, play_ground, self.level_number) # noqa E501
        x_dragon, y_dragon = find_player.find_player(sign_of_game.DRAGON_SIGN.value, play_ground, self.level_number) # noqa E501
        if attack_probability < 0.9:
            if (abs(row - x_dragon) == 0) and (abs(col - y_dragon) <= 2):
                logger.info('Dragon Attack by Hearing Power')
                print("hear", attack_probability)
                play_ground: list = dragon_move.y_move_dragon(play_ground, life_counter, self.user_avatar, self.level_number) # noqa E501
                life_situation: int = Win_Lose.lose(play_ground, life_counter, self.user_avatar, self.level_number) # noqa E501
                return life_situation
            elif (abs(col - y_dragon) == 0) and (abs(row - x_dragon) <= 2):
                logger.info('Dragon Attack by Hearing Power')
                print("hear", attack_probability)
                play_ground: list = dragon_move.x_move_dragon(play_ground, life_counter, self.user_avatar, self.level_number) # noqa E501
                life_situation: int = Win_Lose.lose(play_ground, life_counter, self.user_avatar, self.level_number) # noqa E501
                return life_situation
            else:
                return life_counter
        else:
            return life_counter
