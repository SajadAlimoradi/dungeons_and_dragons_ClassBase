# import csv
import os
import time
# from database import db
from dungeon_dragon.model import User


# cleaning
def clear_screen() -> int:
    """this function clean screen from previous code which ran"""
    return os.system('cls')


class Login():
    """
    handling login of user and authenticate the value of object
    """
    def __init__(self, user_name, user_password):
        self.user_name = user_name
        self. user_password = user_password

    @property
    def user_name(self):
        """
        this function is getter of the user_name's setter
        """
        return self.__user_name

    @user_name.setter
    def user_name(self, value):
        """
        this function check type of user_name(it must be int or int)

        Parameters
        ----------
        value : user_name which player enter


        Returns
        -------
        as private attr return the user_name

        """
        if isinstance(value, (str, int)) is not True:
            raise ValueError('username must be str')
        else:
            self.__user_name = value

    def login(self) -> str:
        """
        handling login of user and check the input with database
        """
        clear_screen()
        while True:
            user_name = self.__user_name
            user_password = self.user_password
            clear_screen()
            user = User.adapt(user_name)
            for line in user:
                if user_name == line[0] and user_password == line[1]:
                    user_avatar = line[2]
                    print("You Logged in Succsesfully")
                    time.sleep(1)
                    clear_screen()
                    return user_name, user_avatar
                    break
            else:
                print("Please enter correct data")
                return None, None
