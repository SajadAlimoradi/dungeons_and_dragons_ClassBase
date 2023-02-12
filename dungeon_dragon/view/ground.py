import time
import os
from pyfiglet import Figlet
from termcolor import colored
from painless.design.singleton import Singleton

LIFE_SIGN: str = '\U0001F9E1'

level_game: dict = {
    'easy': 8,
    'medium': 10,
    'hard': 12
}


# cleaning
def clear_screen() -> int:
    """this function clean screen from previous code which ran"""
    return os.system('cls')


class Ground(metaclass=Singleton):
    """
    this class handle the ground by the level which player choose it,
    for example; make the ground, load it
    in addition there are other feature for make the player interesting
    for example loading the game

    """

    def __init__(self, user_avatar):
        self.user_avatar = user_avatar

    def __repr__(self):
        return 'This is a class for handling ground of game'

    # define level of game
    def detect_level(self, user_level) -> int:
        """
        this function translate the input of user from string to int

        Parameters
        ----------
        level_game : enter the dictionary of defined level

        user_level : the level which user enter will be enter here as string


        Returns
        -------
        play_ground: int : return the ground of the game

        """
        for level, level_number in level_game.items():
            if level == user_level:
                return level_number
                break
            else:
                return level_game['medium']

    # print play ground
    def print_ground(self, play_ground: list, life_counter: int) -> None: # noqa E501
        """this function print play ground

        Parameters
        ----------
        play_ground: list : the ground of play

        life_counter : int : this parameter enter the situation of player life

        Returns
        -------
        None


        """
        print(f"{self.user_avatar} -> {LIFE_SIGN} * {life_counter}")
        print("-------------\n")
        for line in play_ground:
            print(*line)

    # define ground of the game
    def make_ground(self, level_number: int) -> list:
        """

        Parameters
        ----------
        level_number : int : stage of level which user choose is detected here.

        Returns
        -------
        play_ground: int : return the ground of the game

        """
        play_ground: list = list()
        for column in range(level_number):
            empty_row: list = []
            for row in range(level_number):
                empty_row.append("()")
            play_ground.append(empty_row)
        return play_ground

    @staticmethod
    def loading_game() -> None:
        """
        showing loading for player; it means game is so heavy and cool :)
        this function return nothing

        Parameters
        ----------
        None

        Returns
        -------
        None

        """
        second_counter: int = 0
        while second_counter < 3:
            second_counter += 1
            print("LOADING.  ")
            time.sleep(0.25)
            clear_screen()
            print("LOADING.. ")
            time.sleep(0.25)
            clear_screen()
            print("LOADING...")
            time.sleep(0.25)
            clear_screen()
        start_message = Figlet(font='standard')
        print(colored(start_message.renderText('Are  you  ready  ?!'), 'red'))
        time.sleep(1)
        clear_screen()
        print(colored(start_message.renderText('GO'), 'red'))
        time.sleep(0.5)
        clear_screen()
