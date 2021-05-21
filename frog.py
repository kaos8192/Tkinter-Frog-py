from tkinter import *

class Frog:
    def __init__(self, root, win, x, y, chan):
        self.can = win
        self.start = (x,y)
        self.x = x
        self.y = y
        self.g = x + 18
        self.h = y + 18
        self.i = x - 18
        self.j = y - 18
        self.lives = 3
        self.chan = chan
        self.root = root
        self.col = "#ff751a"
        self.rec = self.can.create_rectangle(self.g,self.h,self.i,self.j,fill=self.col)
        self.lock = False
        self.can.bind_all("<Key>", lambda e : self.movehelp(e))
        self.move = 'q'
        self.life_left = self.can.create_text(48,32,text = "Lives"+f":  {self.lives}", fill = "white", font = (16))


    def draw_frog(self):
        i = self.can.create_rectangle(self.g,self.h,self.i,self.j,fill=self.col)
        self.can.delete(self.rec)
        self.rec = i


    def movehelp(self, event):
        if self.move == 'q':
            self.move=event.keysym
            self.move_frog()

    def move_frog(self):
        if self.lock is True:
            self.root.after(10,self.move_frog)

        elif ((self.move == 'Up' or self.move == 'w') and self.y - self.chan > 0):
           self.y -= self.chan
           self.h -= self.chan
           self.j -= self.chan
        elif ((self.move == 'Down' or self.move == 's') and self.y + self.chan < 896):
           self.y += self.chan
           self.h += self.chan
           self.j += self.chan
        elif ((self.move == 'Left' or self.move == 'a') and self.x - self.chan > 0):
           self.x -= self.chan
           self.g -= self.chan
           self.i -= self.chan
        elif ((self.move == 'Right' or self.move == 'd') and self.x + self.chan < 896):
           self.x += self.chan
           self.g += self.chan
           self.i += self.chan
        else:
            pass

        obja = None
        for obj in self.root.all_movers:
            if self.obj_frog(obj):
                if obj.can_kill():
                    self.killed()
                else:
                    obja = obj
        for ter in self.root.kill_terrain:
            if obja is not None:
                pass
                #print("good")
            elif self.obj_frog(ter):
                self.killed()


        self.move = 'q'

        self.lock = True

    def obj_frog(self, obj):
        #print("KILL")
        xa, ya, xb, yb = self.can.coords(self.rec)
        res = self.can.find_overlapping(xa,ya,xb,yb)
        if obj.rec in res:
            return True
        else:
            return False

    def killed(self):
        self.lock = True
        self.lives -= 1
        print(str(self.lives))
        if self.lives >=1:
            self.x = self.start[0]
            self.y = self.start[1]
            self.g = self.start[0] + 18
            self.h = self.start[1] + 18
            self.i = self.start[0] - 18
            self.j = self.start[1] - 18
            self.can.delete(self.life_left)
            self.life_left = self.can.create_text(48,32,text = "Lives"+f":  {self.lives}", fill = "white", font = (16))
            return False
        else:
            return True
