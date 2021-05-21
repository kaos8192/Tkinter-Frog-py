#Frogger by Geir Anderson
from tkinter import *
from frog import *
from game import *
from movers import *
#TODO make classes

def main():
    init_win = Tk()
    init_win.title("Frooger")
    init_win.configure(background="black")
    init_win.geometry("1280x1024")

    button_frame = Frame(init_win, bd = 8, bg = "#666699",width=986,height=158)
    button_frame.pack(side=BOTTOM)

    game_frame = Game(init_win,button_frame)
    def start_it(it):
        game_frame.board.pack()
        game_frame._unpause()
        game_frame.tick(initial = 1)
        it.configure(text="Pause",command=lambda:game_frame._pause())


    button_frame.start = Button(button_frame, text = "Start", command=lambda:start_it(button_frame.start))
    button_frame.start.pack(side=LEFT)

    button_frame.quit = Button(button_frame, text = "Quit", command=init_win.destroy)
    button_frame.quit.pack(side=RIGHT)

    if game_frame.state == "paused":
        game_frame._pause()

    else:
        init_win.after(372,game_frame.tick())

    init_win.mainloop()

main()
