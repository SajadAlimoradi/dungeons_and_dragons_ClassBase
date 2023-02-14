import os
import logging
import configparser
from termcolor import colored
from playsound import playsound
from pyfiglet import Figlet
from dungeon_dragon.control.functions import (
    find_player
)
from dungeon_dragon.view.ground import Ground
from painless.utils.second_thread import stop_thread

from painless.helper.enum import (
    sound_and_imgs_of_game,
    sign_of_game
)


# logging file is config and handle here
config = configparser.ConfigParser()
config.read('config\\logging.toml')
logger = logging.getLogger(__name__)
file_h = logging.FileHandler(config['win_lose']['file_handler'])
file_f = logging.Formatter(config['win_lose']['file_formatter'])
file_h.setFormatter(file_f)
file_h.setLevel(logging.INFO)
logger.addHandler(file_h)
logger.setLevel(logging.INFO)


def clear_screen() -> int:
    """this function clean screen from previous code which ran"""
    return os.system('cls')

# define losing


class Win_Lose():
    """
    this class handle situation of winning and losing
    """

    # define losing
    @staticmethod
    def lose(play_ground: list, life_counter: int, user_avatar: str, level_number: int) -> int: # noqa E501
        """this function define the position which player lose
        if position of player reach to dragon;
        player going to die or lost one of it's life

        Parameters
        ----------
        life_counter : int: this parameter enter the situation of player life

        play_ground: list : return the ground of the game

        life_counter: int : this parameter enter the situation of player life

        user_avatar: str : avatar of player

        level_number: int : stage of level which user choose is detected here.


        Returns
        -------
        new_life_counter : int: this parameter is the situation of player life

        """
        clear_screen()
        if life_counter > 0:
            logger.info('player lost one life')
            new_life_counter = life_counter - 1
            logger.info(f'Now life sitution is {new_life_counter}')
            ground = Ground(user_avatar)
            ground.print_ground(play_ground, new_life_counter)
            playsound(sound_and_imgs_of_game.losing_life.value) # noqa E501
            lose_message = Figlet(font='standard')
            print(colored(lose_message.renderText('BE CAREFULL !'), 'blue'))
            print("By watching advertisment you can return your lost life ==== adv") # noqa E501
            return new_life_counter
        else:
            logger.info('player lose')
            x_player, y_player = find_player.find_player(user_avatar, play_ground, level_number) # noqa E501
            play_ground[x_player][y_player] = LOSING_SIGN # noqa E501
            ground = Ground(user_avatar)
            ground.print_ground(play_ground, life_counter)
            playsound(sound_and_imgs_of_game.losing.value) # noqa E501
            lose_message = Figlet(font='standard')
            print(colored(lose_message.renderText('YOU LOSE :('), 'blue'))
            stop_thread.is_set()
            quit()

    # define winning
    @staticmethod
    def win(play_ground: list, life_counter: int, user_avatar: str, level_number: int) -> None: # noqa E501
        """this function define the position which player win
        if player reach to the dungeon; player going to win

        Parameters
        ----------
        life_counter : int: this parameter enter the situation of player life

        play_ground: list : return the ground of the game

        life_counter: int : this parameter enter the situation of player life

        user_avatar: str : avatar of player

        level_number: int : stage of level which user choose is detected here.


        Returns
        -------
        None

        """
        x_dungeon, y_dungeon = find_player.find_player(sign_of_game.DUNGEON_SIGN.value, play_ground, level_number) # noqa E501
        x_player, y_player = find_player.find_player(user_avatar, play_ground, level_number) # noqa E501
        if (abs(x_player - x_dungeon) == 1 and abs(y_player - y_dungeon) == 0) or (abs(x_player - x_dungeon) == 0 and abs(y_player - y_dungeon) == 1): # noqa E501
            logger.info('player win')
            clear_screen()
            ground = Ground(user_avatar)
            ground.print_ground(play_ground, life_counter)
            playsound(sound_and_imgs_of_game.winning.value) # noqa E501
            win_message = Figlet(font='standard')
            print(colored(win_message.renderText('YOU WIN :)'), 'blue'))
            stop_thread.is_set()
            quit()
