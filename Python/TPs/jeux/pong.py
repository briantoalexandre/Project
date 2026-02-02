from tkinter import *
from functools import partial

class window(Tk):
    def __init__(self, size, racket, ball):
        super().__init__()
        self.windowsize = size
        self.geometry(self.windowsize)
        self.title("PING 8.8.8.8")
        self.update()
        self.racket1 = Button(self, text="")
        self.racket1x = racket[0]
        self.racket1y = racket[1]
        self.racket1width = racket[2]
        self.racket1height = racket[3]
        self.racket2 = Button(self, text="")
        self.racket2x = int(self.winfo_width())-(racket[2]+17.5*2+racket[0])
        self.racket2y = racket[1]
        self.racket2width = racket[2]
        self.racket2height = racket[3]
        self.ball = Button(self, text="")
        self.ballx = ball[0]
        self.bally = ball[1]
        self.ballwidth = ball[2]
        self.ballheight = ball[3]
        self.ai = 1
        
    
        
    def up(self, event):
        if self.racket1y >= 0:
            self.racket1y -= 5
            self.racket1.place_configure(y=self.racket1y)
            self.update()
    
    def down(self, event):
        if self.racket1y <= self.winfo_height()-self.racket1.winfo_height():
            self.racket1y += 5
            self.racket1.place_configure(y=self.racket1y)
            self.update()
    def up2(self, event):
        if self.racket2y >= 0:
            self.racket2y -= 5
            self.racket2.place_configure(y=self.racket2y)
            self.update()
    
    def down2(self, event):
        if self.racket2y <= self.winfo_height()-self.racket2.winfo_height():
            self.racket2y += 5
            self.racket2.place_configure(y=self.racket2y)
            self.update()
    
    def dlup(self, event): #diagonal left up
        pass
    
    def drup(self, event): #diagonal right up
        pass
    
    def right(self, event):
        pass
    
    def drdown(self, event): #diagonal right down
        pass
    
    def dldown(self, event): #diagonal left down
        pass
    
    def left(self, event):
        pass
    
    def placement(self):
        self.racket1.configure(width=self.racket1width, height=self.racket1height) #racket1 options
        self.racket1.place(x=self.racket1x, y=self.racket1y)
        self.bind(sequence="<Up>", func=self.up)
        self.bind(sequence="<Down>", func=self.down)
        self.update()
        self.racket2.configure(width=self.racket2width, height=self.racket2height) #racket2 options
        self.racket2.place(x=self.racket2x, y=self.racket2y)
        if self.ai == 0:
            self.bind(sequence="<P>", func=self.up2)
            self.bind(sequence="<M>", func=self.down2)
        self.update()
        self.ball.configure(width=self.ballwidth, height=self.ballheight) #ball options
        self.ball.place(x=self.winfo_width()//2-self.ball.winfo_width(),y=self.winfo_height()//2-self.ball.winfo_height())

racket1 = [15,0,1,7] #[x,y,width,height]
racket2 =[15,0,1,7] #width,height]
ball =[30,30,2,2] #[x,y,width,height]
Main = window(size="600x400", racket=racket1, ball=ball)

Main.placement()

Main.mainloop()
    
