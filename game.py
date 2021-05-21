from tkinter import *
from frog import *
from movers import *
from terrain import *

class Game(Frame):
    def __init__(self, win, buttons):
        Frame.__init__(self,win,bd = 0, bg = "black", width=896, height=960)
        self.win = win
        self.buttons=buttons
        self.units = 8
        self.state = "paused"
        self.edgex=896
        self.edgey=960
        self.pack(side=TOP)
        self.board = Canvas(self, bd=0, bg="black",relief=SUNKEN,width=896,height=960)
        self.froog = Frog(root = self, win=self.board, x=480, y=864, chan = self.units)
        autoein0 = Car(root = self,win=self.board, x=1024, y=800, ox=48, oy=28, chan = self.units, spwn="right")
        autoein1 = Car(root = self,win=self.board, x=1342, y=800, ox=48, oy=28, chan = self.units, spwn="right")
        autozwei = Car(root = self,win=self.board, x=-96, y=736, ox=24, oy=24, chan = self.units, spwn="left")
        autodrei = Car(root = self,win=self.board, x=928, y=672, ox=24, oy=24, chan = self.units, spwn="right")
        autovier = Car(root = self, win=self.board, x=-96, y=608, ox=32, oy=22, chan = self.units, spwn="left", col = "#d22", racer = True)
        autofunf = Car(root = self,win=self.board, x=928, y=546, ox=26, oy=24, chan = self.units, spwn="right")

        logein = Log(root = self,win=self.board, x=928, y=418, ox=64, oy=28, chan = self.units, spwn="right")
        logzwei = Log(root = self,win=self.board, x=-96, y=354, ox=64, oy=25, chan = self.units, spwn="left")
        logdrei = Log(root = self,win=self.board, x=878, y=290, ox=64, oy=28, chan = self.units, spwn="right")
        logvier = Log(root = self,win=self.board, x=-56, y=226, ox=64, oy=25, chan = self.units, spwn="left")
        logfunf = Log(root = self,win=self.board, x=901, y=162, ox=64, oy=28, chan = self.units, spwn="right")

        road = Road(self.board)
        water = Water(self.board,root=self)
        grass_start = Grass(self.board,which=1)
        grass_middle = Grass(self.board,which=2)
        swamp1 = Swamp(self.board,root=self,which=1)
        swamp2 = Swamp(self.board,root=self,which=2)
        swamp3 = Swamp(self.board,root=self,which=3)
        swamp4 = Swamp(self.board,root=self,which=4)
        x = 64
        y = 64

        '''
        count = 0
        while count < 14:
            self.board.create_line(0,y+y*count,x*15,y+y*count)
            count+=1

        count = 0
        while count < 13:
            self.board.create_line(x+x*count,y,x+x*count,y*14)
            count+=1
        '''

        self.all_movers = [autoein0,autoein1,autozwei,autodrei,autovier,autofunf,logein,logzwei,logdrei,logvier,logfunf]
        self.kill_terrain = [water,swamp1,swamp2,swamp3,swamp4]
        self.tick_delay = 0
        self.tick_now = 0

        self.a = Label(self, bg ="black", text = "PAUSED", fg = "white")

        #self.win.bind_all("<Escape>", lambda e : self._pause(e))
        #self.win.bind_all("<Return>", lambda e : self._unpause(e))
        #self.win.bind_all("<Button-1>", lambda e : self._pause(e))

    def tick(self, initial = 0):
        collide = False
        obja = None
        if (self.froog.x < 0 or self.froog.x >= self.edgex or self.froog.y < 64 or self.froog.y >= self.edgey - 64):
            if self.froog.killed():
                print("GAME OVER!")
                self.after(1000,self.quit)
                return
        for obj in self.all_movers:
            collide = self.froog.obj_frog(obj)

            if collide:
                self.froog.lock = True
                if obj.can_kill():
                    if self.froog.killed():
                        print("GAME OVER!")
                        self.after(1000,self.quit)
                        return
                else:
                    obja = obj

        for ter in self.kill_terrain:
            if obja is not None:
                pass
                #print("good")
            elif self.froog.obj_frog(ter):
                if self.froog.killed():
                    print("GAME OVER!")
                    self.after(1000,self.quit)
                    return

        if self.state == "running":
            #self.froog.move_frog()
            for obj in self.all_movers:
                #self.froog.move_frog()
                self.froog.draw_frog()
                if initial == 1:
                    obj.draw_obj()
                    self.tick_now = 4
                elif ((self.tick_delay >= self.tick_now) or (obj.racer is True and self.tick_delay == 2)):
                    if obj == obja:
                        #if self.froog.move == "q":
                        if obj.dir == "left":
                            self.froog.x -= self.units
                            self.froog.g -= self.units
                            self.froog.i -= self.units
                            obj.move_obj()
                        else:
                            self.froog.x += self.units
                            self.froog.g += self.units
                            self.froog.i += self.units
                            obj.move_obj()
                        self.froog.draw_frog()
                    else:
                        obj.move_obj()
                    collide = self.froog.obj_frog(obj)

                    if collide:
                        #self.froog.lock = True
                        if obj.can_kill():
                            if self.froog.killed():
                                print("GAME OVER!")
                                self.after(1000, self.quit)
                                return
                        else:
                            #if self.froog.move == "q":
                            if obj.dir == "left":
                                self.froog.move = "a"
                                self.froog.move_frog()
                            else:
                                self.froog.move = "d"
                                self.froog.move_frog()
                            self.froog.draw_frog()


            if self.tick_delay >= self.tick_now:
                self.tick_delay = 0
            else:
                self.tick_delay += 1

            collide = False

            self.froog.lock = False

        else:
            self.froog.lock = True

        self.froog.draw_frog()
        self.after(18, self.tick)



    def _unpause(self):#,event=None):
        #print("return")
        if self.state == "paused":
            #print("hi")
            self.state = "running"
            self.win.update_idletasks()
            self.a.pack_forget()
            self.board.pack()
            self.buttons.start.configure(text = "Pause",command=lambda:self._pause())
            #self.board.bind("<Button-1>", lambda e : self._pause(e))

        else:
            pass

    def _pause(self):#,event=None):
        #print("HELLO")
        if self.state == "running":
            self.state = "paused"
            self.a.pack(side=TOP,expand = True, fill = 'both')
            self.buttons.start.configure(text = "Unpause",command=lambda:self._unpause())
            #self.board.bind("<Button-1>", lambda e : self._unpause(e))

