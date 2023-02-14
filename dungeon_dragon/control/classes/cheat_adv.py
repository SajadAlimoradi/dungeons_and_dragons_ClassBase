import time
import os
import logging
import configparser
from playsound import playsound
from termcolor import colored
from pyfiglet import Figlet
from PIL import Image
from dungeon_dragon.control.functions import find_player
from dungeon_dragon.view.ground import Ground
from painless.utils.second_thread import stop_thread, background_music
from painless.helper.enum import (
    sign_of_game,
    sound_and_imgs_of_game
)


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


# cleaning
def clear_screen() -> int:
    """this function clean screen from previous code which ran"""
    return os.system('cls')


class Cheat():

    """
    this class contain many cheat codes which can help player to win
    for example by typing 'comeonman' all side of player convert to fire and
    player win the game
    by typing bombd/bombu player can throw bombe to down or top of it's
    position and by typing fire, bombs explode and if the bomb is close
    to dragon, the dragon will be killed and player win the game
    """

    def __init__(self, user_avatar: str, level_number: int):
        self.user_avatar = user_avatar
        self.level_number = level_number
        # self.ground = Ground(self.user_avatar)

    def __repr__(self):
        return f'This is a cheat code define for {self.user_avatar} user'

    def cheat_code_comeonman(self, play_ground: list, cross_player: str, life_counter: int, ground: Ground) -> None: # noqa E501

        """some cheat code defined in the game, this function handle comeonman

        Parameters
        ----------
        play_ground : list : the ground of play

        cross_player : str : the button which user press (left, right,...)

        life_counter : int : the situation of player life

        Returns
        -------
            None

        """
        if cross_player == "comeonman":
            logger.info(f'player press [{cross_player}] cheatcode and win ')
            logger.info('player win')
            clear_screen()
            x_player, y_player = find_player.find_player(self.user_avatar, play_ground, self.level_number) # noqa E501
            play_ground[x_player + 1][y_player] = sign_of_game.FIRE_SIGN.value
            play_ground[x_player - 1][y_player] = sign_of_game.FIRE_SIGN.value
            play_ground[x_player][y_player + 1] = sign_of_game.FIRE_SIGN.value
            play_ground[x_player][y_player - 1] = sign_of_game.FIRE_SIGN.value
            ground.print_ground(play_ground, life_counter)
            playsound(sound_and_imgs_of_game.comeonman.value) # noqa E501
            playsound(sound_and_imgs_of_game.cheat_code_1.value) # noqa E501
            win_message = Figlet(font='standard')
            print(colored(win_message.renderText('YOU WIN'), 'blue'))
            stop_thread.is_set()
            quit()

    def cheat_code_bombd(self, play_ground: list, cross_player: str, life_counter: int,  ground: Ground) -> None: # noqa E501

        """some cheat code defined in the game, this function handle comeonman

        Parameters
        ----------
        play_ground : list : the ground of play

        cross_player : str : the button which user press (left, right,...)

        life_counter : int : the situation of player life

        Returns
        -------
            None

        """
        if cross_player == "bombd":
            logger.info(f'player press [{cross_player}] cheatcode') # noqa E501
            x_player, y_player = find_player.find_player(self.user_avatar, play_ground, self.level_number) # noqa E501
            if x_player < self.level_number - 2:
                clear_screen()
                play_ground[x_player + 1][y_player] = sign_of_game.BOMB_SIGN.value # noqa E501
                ground.print_ground(play_ground, life_counter)
                x_bomb, y_bomb = find_player.find_player(self.user_avatar, play_ground, self.level_number) # noqa E501
                time.sleep(0.5)
                clear_screen()
                play_ground[x_player + 1][y_player] = '()'
                play_ground[x_player + 2][y_player] = sign_of_game.BOMB_SIGN.value # noqa E501
                ground.print_ground(play_ground, life_counter)
            else:
                clear_screen()
                print("you can't bombing")
                ground.print_ground(play_ground, life_counter)

    def cheat_code_bombu(self, play_ground: list, cross_player: str, life_counter: int,  ground: Ground) -> None: # noqa E501

        """some cheat code defined in the game, this function handle comeonman

        Parameters
        ----------
        play_ground : list : the ground of play

        cross_player : str : the button which user press (left, right,...)

        life_counter : int : the situation of player life

        Returns
        -------
            None

        """
        # ground = Ground(self.user_avatar)
        if cross_player == "bombu":
            logger.info(f'player press [{cross_player}] cheatcode') # noqa E501
            x_player, y_player = find_player.find_player(self.user_avatar, play_ground, self.level_number) # noqa E501
            if x_player > 1:
                clear_screen()
                play_ground[x_player - 1][y_player] = sign_of_game.BOMB_SIGN.value # noqa E501
                ground.print_ground(play_ground, life_counter)
                x_bomb, y_bomb = find_player.find_player(self.user_avatar, play_ground, self.level_number) # noqa E501
                time.sleep(0.5)
                clear_screen()
                play_ground[x_player - 1][y_player] = '()'
                play_ground[x_player - 2][y_player] = sign_of_game.BOMB_SIGN.value # noqa E501
                ground.print_ground(play_ground, life_counter)
            else:
                clear_screen()
                print("you can't bombing")
                ground.print_ground(play_ground, life_counter)

    def cheat_code_fire(self, play_ground: list, cross_player: str, life_counter: int,  ground: Ground) -> None: # noqa E501

        """some cheat code defined in the game, this function handle comeonman

        Parameters
        ----------
        play_ground : list : the ground of play

        cross_player : str : the button which user press (left, right,...)

        life_counter : int : the situation of player life

        Returns
        -------
            None

        """
        if cross_player == "fire":
            logger.info(f'player press [{cross_player}] cheatcode') # noqa E501
            x_bomb, y_bomb = find_player.find_player(sign_of_game.BOMB_SIGN.value, play_ground, self.level_number) # noqa E501
            if (x_bomb is not None) and (y_bomb is not None):
                play_ground[x_bomb][y_bomb] = sign_of_game.FIRE_SIGN.value
                clear_screen()
                ground.print_ground(play_ground, life_counter)
                x_fire, y_fire = find_player.find_player(sign_of_game.FIRE_SIGN.value, play_ground, self.level_number) # noqa E501
                x_dragon, y_dragon = find_player.find_player(sign_of_game.DRAGON_SIGN.value, play_ground, self.level_number) # noqa E501
                time.sleep(1)
                play_ground[x_fire][y_fire] = '()'
                if (x_dragon - x_fire == 0 and abs(y_dragon - y_fire) == 1) or (abs(x_dragon - x_fire) == 1 and y_dragon - y_fire == 0): # noqa E501
                    logger.info('player win')
                    play_ground[x_dragon][y_dragon] = sign_of_game.LOSING_SIGN.value # noqa E501
                    clear_screen()
                    ground.print_ground(play_ground, life_counter)
                    stop_thread.is_set()
                    background_music.join()
                    playsound(sound_and_imgs_of_game.cheat_code_1.value) # noqa E501
                    win_message = Figlet(font='standard')
                    print(colored(win_message.renderText('GREAT Dragon killed! YOU WIN'), 'blue')) # noqa E501
                    quit()
            else:
                ground.print_ground(play_ground, life_counter)
                pass


class Adv():
    """
    this class contain many cheat codes which can help player to increase life.
    by typing 'adv' kolah ghermezi adv play and finally the life situation
    increase for example if life_ounter = 2 by typing adv life_counter = 3
    """

    def __init__(self, user_avatar: str, level_number: int):
        self.user_avatar = user_avatar
        self.level_number = level_number

    def __repr__(self):
        return f'This is a Adv code define for {self.user_avatar} user'

    def advertising(self, play_ground: list, cross_player: str, life_counter: int,  ground: Ground) -> int: # noqa E501
        """this function run the advertisement and change situation
        of player's life

        Parameters
        ----------
        play_ground: list : the ground of play

        cross_player: str : the button which user press (left, right,...)

        life_counter: int : the situation of player life

        Returns
        -------
        new_life_counter : int : changed situation of player life(one life increase) # noqa E501
        """
        life_counter = life_counter
        if cross_player == "adv":
            logger.info(f'player press watching ads') # noqa E501
            adv = Image.open(sound_and_imgs_of_game.img_adv_1.value) # noqa E501
            adv.show()
            playsound(sound_and_imgs_of_game.sound_adv_1.value)
            new_life_counter = life_counter + 1
            ground.print_ground(play_ground, new_life_counter)
            logger.info(f'Now life sitution is {new_life_counter}')
            return new_life_counter
        else:
            return life_counter
