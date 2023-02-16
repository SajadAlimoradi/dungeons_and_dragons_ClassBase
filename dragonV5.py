import os
import random
import logging
from pyfiglet import Figlet
from termcolor import colored
from dungeon_dragon.control.functions import (
    banner,
    user_player_sign
)

# from Packages.Classes.define_player_position import PlayerPosition
from dungeon_dragon.control.classes.player_move import Character # noqa E501
from dungeon_dragon.control.classes.player_move import Player # noqa E501
from dungeon_dragon.control.classes.dragon_power import Dragon # noqa E501
from dungeon_dragon.control.classes.win_loss import Win_Lose # noqa E501
from dungeon_dragon.control.classes.cheat_adv import Cheat # noqa E501
from dungeon_dragon.control.classes.cheat_adv import Adv # noqa E501
from dungeon_dragon.control.classes.register import Register # noqa E501
from dungeon_dragon.control.classes.login import Login # noqa E501
from dungeon_dragon.view.ground import Ground # noqa E501
from painless.utils.second_thread import background_music
from painless.helper.enum import (
    player,
    sign_of_game
)

from dungeon_dragon.view.login_registeration_view import login_register_view
# number of player's life
life_counter: int = 3


# cleaning
def clear_screen() -> int:
    """this function clean screen from previous code which ran"""
    return os.system('cls')


'''
==============================================================================
GAME IS STARTING HERE!

prerequisite of starting game is going to be prepare.

for example: login/register/level/establishing roles of game, etc
==============================================================================
'''

# Banner is running then user's register or login will be run
banner.banner()
user_name, user_avatar = login_register_view()

# user choose the level of the game
user_level = input('Which level do you want to play? Easy - Medium - Hard\n\n').lower() # noqa E501
# avatar of user will be established
user_avatar: str = user_player_sign.user_player(user_avatar)
# ground of game is going to be prepared here. base on the level which user choose # noqa E501
ground = Ground(user_avatar)
level_number: int = ground.detect_level(user_level)
play_ground: list = ground.make_ground(level_number)

# objects are created
user = Player(user_name, user_avatar, level_number)
dragon = Dragon(user_avatar, level_number)
dungeon = Character()
cheat_code = Cheat(user_avatar, level_number)
adv_code = Adv(user_avatar, level_number)

# after making ground, now roles are going to be established in the ground of the game # noqa E501
player_X_Y = random.sample(range(level_number), 6)
user.position(play_ground, player_X_Y[0], player_X_Y[1], user_avatar)
dragon.position(play_ground, player_X_Y[2], player_X_Y[3], sign_of_game.DRAGON_SIGN.value) # noqa E501
dungeon.position(play_ground, player_X_Y[4], player_X_Y[5], sign_of_game.DUNGEON_SIGN.value) # noqa E501

# game is loading here (game need loading because it is so KHAFAN! :) )
Ground.loading_game()
# all the roles are ready! ground of game is going to be printed here.
ground.print_ground(play_ground, life_counter)


'''
==============================================================================
prerequisite(login/register/level of game/establishing roles)
of starting game, is ready.

Now game is going to start.
==============================================================================
'''
# background music is start from here.
background_music.start()

while True:
    attack_probability: float = random.random()
    cross_player: str = input("\nWhere Should I Go ?\n")
    clear_screen()
    # handling adv
    if cross_player == "adv":
        life_counter: int = adv_code.advertising(play_ground, cross_player, life_counter, ground= Ground(user_avatar)) # noqa E501
    # handling player move
    user.move_left(play_ground, cross_player, life_counter, ground) # noqa E501
    user.move_right(play_ground, cross_player, life_counter, ground= Ground(user_avatar)) # noqa E501
    user.move_up(play_ground, cross_player, life_counter, ground= Ground(user_avatar)) # noqa E501
    user.move_down(play_ground, cross_player, life_counter, ground= Ground(user_avatar)) # noqa E501
    user.move_check(play_ground, cross_player, life_counter, ground= Ground(user_avatar)) # noqa E501
    user.move_help(play_ground, cross_player, life_counter, ground= Ground(user_avatar)) # noqa E501
    # handling Dragon move
    dragon.smelling_power(play_ground, attack_probability, life_counter)
    life_counter: int = dragon.hearing_power(play_ground, attack_probability, life_counter) # noqa E501
    # handling situation of winning and losing
    Win_Lose.win(play_ground, life_counter, user_avatar, level_number)
    # handling cheatCode
    cheat_code.cheat_code_comeonman(play_ground, cross_player, life_counter, ground= Ground(user_avatar)) # noqa E501
    cheat_code.cheat_code_bombu(play_ground, cross_player, life_counter, ground= Ground(user_avatar)) # noqa E501
    cheat_code.cheat_code_bombd(play_ground, cross_player, life_counter, ground= Ground(user_avatar)) # noqa E501
    cheat_code.cheat_code_fire(play_ground, cross_player, life_counter, ground= Ground(user_avatar)) # noqa E501
    