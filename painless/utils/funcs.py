import threading
import os
from threading import Thread
from playsound import playsound
from pathlib import Path

stop_thread = threading.Event()


previous_directory = Path(__file__).resolve().parent.parent.parent
file_path = os.path.join(previous_directory, 'dungeon_dragon\\sounds', 'game.mp3')


def play():
    """this function run background music"""
    playsound(file_path)


# thread of playing is made here
background_music = Thread(target=play)
