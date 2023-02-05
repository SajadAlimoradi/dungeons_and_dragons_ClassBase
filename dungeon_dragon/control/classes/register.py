# import csv
import os
import time
from database import db
from dungeon_dragon.model import User


# cleaning
def clear_screen() -> int:
    """this function clean screen from previous code which ran"""
    return os.system('cls')


class Register():
    """
    handling Register of user and authenticate the value of object
    """

    def __init__(self, user_name: str, user_password: str, user_avatar: str):
        self.user_name = user_name
        self.user_password = user_password
        self.user_avatar = user_avatar

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

    @property
    def user_password(self):
        """
        this function is getter of the user_password's setter
        """
        return self.__user_password

    @user_password.setter
    def user_password(self, value):
        """
        this function check type of user_password(it must be at least 8 character) # noqa E501

        Parameters
        ----------
        value : user_password which player enter


        Returns
        -------
        as private attr return the user_password

        """
        if len(value) < 8:
            raise TypeError('Password must contain at least 8 character')
        else:
            self.__user_password = value

    def Register(self, confirm_user_password: str) -> str:
        """handling registration of user and save it in csv file

        Parameters
        ----------
        confirm_user_password: str : value of second time user enter password for authentication # noqa E501

        Returns
        -------
        user_name, user_password, user_avatar
        """

        clear_screen()
        while True:
            clear_screen()
            if self.__user_password == confirm_user_password:
                print("You Registered Succsesfully")
                time.sleep(1)
                clear_screen()
                db.engine.connect()
                user = User.create(
                    username=self.__user_name,
                    password=self.__user_password,
                    avatar=self.user_avatar
                )
                return True
                # return self.__user_name, self.__user_password, self.user_avatar # noqa E501
                break
            else:
                print("Please enter correct")
                time.sleep(1)
                clear_screen()
                return None, None, None
                break
