from tkinter import *
from frog import *
from game import *

class Move_Std:
    def __init__(self,root,win,x,y,ox,oy,chan,spwn,col = "white"):
        self.x = x - ox
        self.y = y - oy
        self.i = x + ox
        self.j = y + oy
        self.a = self.x
        self.b = self.y
        self.c = self.i
        self.d = self.j

        self.can = win
        self.root = root
        self.spwn = spwn
        self.col = col
        self.chan = chan
        def path(s):
            if s == "right":
                return "left"
            else:
                return "right"
        self.dir = path(self.spwn)
        self.rec = self.can.create_rectangle(self.a,self.b,self.c,self.d,fill=self.col)
        #self.rec = self.can.create_line(self.a,self.b,self.c,self.d)

    def draw_obj(self):
        i = self.can.create_rectangle(self.a,self.b,self.c,self.d,fill=self.col)
        self.can.delete(self.rec)
        self.rec = i

    def move_obj(self):
        if ((self.dir == "right" and self.a + self.chan > 922) or (self.dir == "left" and self.a - self.chan < -64)):
            self.a = self.x
            self.c = self.i

        elif self.dir == "left":
            self.a = self.a - self.chan
            self.c = self.c - self.chan
        else:
            self.a = self.a + self.chan
            self.c = self.c + self.chan

        self.draw_obj()

    def can_kill(self):
        pass

class Car(Move_Std):
    def __init__(self,root,win,x,y,ox,oy,chan,spwn,col="magenta",racer=False):
        Move_Std.__init__(self,root,win,x,y,ox,oy,chan,spwn,col)
        self.racer = racer

    def can_kill(self):
        #print("HI")
        if self.root.froog.lives >=1:
            return True
        else:
            return False

class Log(Move_Std):
    def __init__(self,root,win,x,y,ox,oy,chan,spwn,col="#5EAB00"):
        Move_Std.__init__(self,root,win,x,y,ox,oy,chan,spwn,col)
        self.racer = False


