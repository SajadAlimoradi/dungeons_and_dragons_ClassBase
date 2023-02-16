from dungeon_dragon.control.classes.register import Register # noqa E501
from dungeon_dragon.control.classes.login import Login # noqa E501
from pyfiglet import Figlet
from termcolor import colored
import logging
import os
from painless.helper.enum import player


# cleaning
def clear_screen() -> int:
    """this function clean screen from previous code which ran"""
    return os.system('cls')


def login_register_view() -> str:
    while True:
        clear_screen()
        start_message = Figlet(font='standard', width=110)
        print(colored(start_message.renderText('Welcome to D & D v.5 '), 'green')) # noqa E501
        enter_situation: str = input("\nPlease choose : Login / Register\n").casefold() # noqa E501
        clear_screen()
        if enter_situation == 'register':
            print(colored(start_message.renderText('Register'), 'red'))
            while True:
                while True:
                    print(f'one : {player.one.value}  two : {player.two.value}  three: {player.three.value}') # noqa E501
                    user_avatar: str = input("Please choose your avatar : one / two / three\n") # noqa E501
                    if user_avatar not in ['one', 'two', 'three']:
                        clear_screen()
                        print("Please enter correct number")
                    else:
                        break
                user_name: str = input("UserName : ")
                user_password: str = input("Password : ")
                user = Register(user_name, user_password, user_avatar)
                while True:
                    confirm_user_password = input("Confirm Password : ")
                    register_auth = user.Register(confirm_user_password) # noqa E501
                    if register_auth is True:
                        break
                logging.basicConfig(filename='painless/helper/login_register_total.log', format='%(asctime)s - %(filename)s - %(message)s', level=logging.INFO) # noqa E501
                logging.info(f'{user_name} Registered')
                break
        elif enter_situation == 'login':
            print(colored(start_message.renderText('Login'), 'red'))
            while True:
                user_name: str = input("UserName : ")
                user_password: str = input("Password : ")
                user = Login(user_name, user_password)
                user_name, user_avatar = user.login()
                if user_name is not None:
                    logging.basicConfig(filename='painless/helper/login_register_total.log', format='%(asctime)s - %(filename)s - %(message)s', level=logging.INFO) # noqa E501
                    logging.info(f'{user_name} Logged in')
                    break
                # else:
                #     pass
            break
        else:
            print("Please choose between these options")
    return user_name, user_avatar
