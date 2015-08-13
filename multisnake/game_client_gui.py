''' Contains client display code '''

import pyglet

class GameWindow(pyglet.window.Window,object):
    """docstring for GameWindow"""
    def __init__(self, *args, **kwargs):
        super(GameWindow, self).__init__(*args, **kwargs)

    def update(self):
        pass


