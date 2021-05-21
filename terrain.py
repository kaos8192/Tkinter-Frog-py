from tkinter import *
from frog import *
from movers import *

class Road:
    def __init__(self,can):
        self.can = can
        self.rec = self.can.create_rectangle(-10, 512, 1000, 832, fill = "#222")
    def can_kill(self):
        return False

class Water:
    def __init__(self,can,root):
        self.can = can
        self.root = root
        self.rec = self.can.create_rectangle(-10, 64, 1000, 448, fill = "#00F")
    '''
    def can_kill(self):
        #print("HI")
        if self.root.froog.lives >=1:
            return True
        else:
            return False
    '''

class Grass:
    def __init__(self,can,which):
        self.can = can
        self.which = which
        if self.which == 1:
            self.rec = self.can.create_rectangle(-10, 832, 1000, 896, fill = "#0B1")
        elif self.which == 2:
            self.rec = self.can.create_rectangle(-10, 448, 1000, 512, fill = "#0B1")
    def can_kill(self):
        return False

class Swamp:
    def __init__(self,can,root,which):
        self.can = can
        self.root = root
        self.which = which
        if self.which == 1:
            self.rec = self.can.create_rectangle(128, 64, 192, 128, fill = "#080")
        elif self.which == 2:
            self.rec = self.can.create_rectangle(320, 64, 384, 128, fill = "#080")
        elif self.which == 3:
            self.rec = self.can.create_rectangle(510, 64, 574, 128, fill = "#080")
        elif self.which == 4:
            self.rec = self.can.create_rectangle(702, 64, 766, 128, fill = "#080")
    '''
    def can_kill(self):
        #print("HI")
        if self.root.froog.lives >=1:
            return True
        else:
            return False
    '''

