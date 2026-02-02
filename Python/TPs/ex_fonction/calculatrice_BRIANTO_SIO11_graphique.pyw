#Calculatrice<> Brianto Alexandre
#raison : calculatrice graphique > CLI

from math import sqrt # noqa
from tkinter import *
from tkinter.messagebox import showerror
from tkinter.font import Font
from functools import partial

class App(Tk):
    def __init__(self):
        super().__init__() # inheritance
        self.title("Calculatrice")
        self.attributes("-toolwindow", True)
        #self.attributes("-topmost", True)
        self.geometry("320x470") #
        self.resizable(False, False)
        #self.grid_columnconfigure(index=1>>1, weight=1)

        self.calc_var = dict() #Work in Progress, will be used to make variable
        self.calc_answer = [] #Work in Progress, will be used for backspace func
        self._ = 0
        self.pixel = PhotoImage(width=1, height=1) #Pixel placement instead of whatever Tkinter is using
        self.font = partial(Font, size=1<<5)
        self.b_pad = 2 #padding

        self.main_frame = Frame(self)
        self.frame_answer = Frame(self.main_frame)
        self.label_calcul = Label(self.frame_answer, text="", anchor=E, font=Font(size=7<<2), image=self.pixel, compound="center", width=500, height=75)

        self.frame_buttons = Frame(self.main_frame)
        self.button_percent = Button(self.frame_buttons, text="%", font=self.font, image=self.pixel, compound="center", width=68, height=51, command=(lambda : self.modify_calcul(func=self.modulo)))
        self.button_clear = Button(self.frame_buttons, text="CE", font=self.font, image=self.pixel, compound="center", width=68, height=51, command=self.clear)
        self.button_clear2 = Button(self.frame_buttons, text="C", font=self.font, image=self.pixel, compound="center", width=68, height=51, command=self.clear2)
        self.button_back = Button(self.frame_buttons, text="\u00E7", font=self.font(family="Wingdings"), image=self.pixel,compound="center", width=68, height=51, command=self.backspace)
        self.button_rmult = Button(self.frame_buttons, text="1/x", font=self.font, image=self.pixel, compound="center", width=68, height=51, command=(lambda : self.modify_calcul(self.rmult)))
        self.button_pow = Button(self.frame_buttons, text="x\u207F", font=self.font, image=self.pixel, compound="center", width=68, height=51, command=(lambda : self.modify_calcul(self.power)))
        self.button_sqrt = Button(self.frame_buttons, text="\u221Ax", font=self.font, image=self.pixel, compound="center", width=68, height=51, command=(lambda : self.modify_calcul(self.sqroot)))
        self.button_div = Button(self.frame_buttons, text="\u00F7", font=self.font, image=self.pixel, compound="center", width=68, height=51, command=(lambda : self.modify_calcul(self.div)))
        self.button_7 = Button(self.frame_buttons, text="7", font=self.font, image=self.pixel, compound="center", width=68, height=51, command=(lambda : self.modify_calcul(self.seven)))
        self.button_8 = Button(self.frame_buttons, text="8", font=self.font, image=self.pixel, compound="center", width=68, height=51, command=(lambda : self.modify_calcul(self.eight)))
        self.button_9 = Button(self.frame_buttons, text="9", font=self.font, image=self.pixel, compound="center", width=68, height=51, command=(lambda : self.modify_calcul(self.nine)))
        self.button_mult = Button(self.frame_buttons, text="\u00D7", font=self.font, image=self.pixel, compound="center", width=68, height=51, command=(lambda : self.modify_calcul(self.mult)))
        self.button_4 = Button(self.frame_buttons, text="4", font=self.font, image=self.pixel, compound="center", width=68, height=51, command=(lambda : self.modify_calcul(self.four)))
        self.button_5 = Button(self.frame_buttons, text="5", font=self.font, image=self.pixel, compound="center", width=68, height=51, command=(lambda : self.modify_calcul(self.five)))
        self.button_6 = Button(self.frame_buttons, text="6", font=self.font, image=self.pixel, compound="center", width=68, height=51, command=(lambda : self.modify_calcul(self.six)))
        self.button_minu = Button(self.frame_buttons, text="-", font=self.font, image=self.pixel, compound="center", width=68, height=51, command=(lambda : self.modify_calcul(self.minus)))
        self.button_1 = Button(self.frame_buttons, text="1", font=self.font, image=self.pixel, compound="center", width=68, height=51, command=(lambda : self.modify_calcul(self.one)))
        self.button_2 = Button(self.frame_buttons, text="2", font=self.font, image=self.pixel, compound="center", width=68, height=51, command=(lambda : self.modify_calcul(self.two)))
        self.button_3 = Button(self.frame_buttons, text="3", font=self.font, image=self.pixel, compound="center", width=68, height=51, command=(lambda : self.modify_calcul(self.three)))
        self.button_plus = Button(self.frame_buttons, text="+", font=self.font, image=self.pixel, compound="center", width=68, height=51, command=(lambda : self.modify_calcul(self.plus)))
        self.button_signe = Button(self.frame_buttons, text="\u00B1", font=self.font, image=self.pixel, compound="center", width=68, height=51, command=(lambda : self.modify_calcul(self.signe)))
        self.button_0 = Button(self.frame_buttons, text="0", font=self.font, image=self.pixel, compound="center", width=68, height=51, command=(lambda : self.modify_calcul(self.zero)))
        self.button_comm = Button(self.frame_buttons, text=",", font=self.font, image=self.pixel, compound="center", width=68, height=51, command=(lambda : self.modify_calcul(self.comma)))
        self.button_resu = Button(self.frame_buttons, text="=", font=self.font, image=self.pixel, compound="center", width=68, height=51, command=self.give_answer)

        self.main_frame.pack(expand=True, fill="both")
        self.frame_answer.pack(side="top", fill="both", expand=True)
        self.label_calcul.pack(anchor=E, pady=5)
        self.frame_buttons.pack(side="top", fill="both", expand=True)
        self.button_percent.grid(row=0, column=0, padx=self.b_pad, pady=self.b_pad)
        self.button_clear.grid(row=0, column=1, padx=self.b_pad, pady=self.b_pad)
        self.button_clear2.grid(row=0, column=2, padx=self.b_pad, pady=self.b_pad)
        self.button_back.grid(row=0, column=3, padx=self.b_pad, pady=self.b_pad)
        self.button_rmult.grid(row=1, column=0, padx=self.b_pad, pady=self.b_pad)
        self.button_pow.grid(row=1, column=1, padx=self.b_pad, pady=self.b_pad)
        self.button_sqrt.grid(row=1, column=2, padx=self.b_pad, pady=self.b_pad)
        self.button_div.grid(row=1, column=3, padx=self.b_pad, pady=self.b_pad)
        self.button_7.grid(row=2, column=0, padx=self.b_pad, pady=self.b_pad)
        self.button_8.grid(row=2, column=1, padx=self.b_pad, pady=self.b_pad)
        self.button_9.grid(row=2, column=2, padx=self.b_pad, pady=self.b_pad)
        self.button_mult.grid(row=2, column=3, padx=self.b_pad, pady=self.b_pad)
        self.button_4.grid(row=3, column=0, padx=self.b_pad, pady=self.b_pad)
        self.button_5.grid(row=3, column=1, padx=self.b_pad, pady=self.b_pad)
        self.button_6.grid(row=3, column=2, padx=self.b_pad, pady=self.b_pad)
        self.button_minu.grid(row=3, column=3, padx=self.b_pad, pady=self.b_pad)
        self.button_1.grid(row=4, column=0, padx=self.b_pad, pady=self.b_pad)
        self.button_2.grid(row=4, column=1, padx=self.b_pad, pady=self.b_pad)
        self.button_3.grid(row=4, column=2, padx=self.b_pad, pady=self.b_pad)
        self.button_plus.grid(row=4, column=3, padx=self.b_pad, pady=self.b_pad)
        self.button_signe.grid(row=5, column=0, padx=self.b_pad, pady=self.b_pad)
        self.button_0.grid(row=5, column=1, padx=self.b_pad, pady=self.b_pad)
        self.button_comm.grid(row=5, column=2, padx=self.b_pad, pady=self.b_pad)
        self.button_resu.grid(row=5, column=3, padx=self.b_pad, pady=self.b_pad)

        self.error = showerror

    def modify_calcul(self, func):
        try:
            self.calc_answer.append(func())
            self.label_calcul.configure(text=self.label_calcul.cget("text") + func())
        except Warning:
            self.error("WiP", message="WiP")


    @staticmethod
    def modulo():
        return "%"

    def clear(self):
        self.label_calcul.configure(text="")

    def clear2(self):
        self._ = 0
        self.label_calcul.configure(text="")

    def backspace(self):
        self.label_calcul.configure(text=self.label_calcul.cget("text")[:-1])

    @staticmethod
    def rmult():
        return "1/"

    @staticmethod
    def power():
        return "**"

    @staticmethod
    def sqroot():
        raise Warning
        pass

    @staticmethod
    def div():
        return "/"

    @staticmethod
    def seven():
        return "7"

    @staticmethod
    def eight():
        return "8"

    @staticmethod
    def nine():
        return "9"

    @staticmethod
    def mult():
        return "*"

    @staticmethod
    def four():
        return "4"

    @staticmethod
    def five():
        return "5"

    @staticmethod
    def six():
        return "6"

    @staticmethod
    def minus():
        return "-"

    @staticmethod
    def one():
        return "1"

    @staticmethod
    def two():
        return "2"

    @staticmethod
    def three():
        return "3"

    @staticmethod
    def plus():
        return "+"

    @staticmethod
    def signe():
        raise Warning
        pass

    @staticmethod
    def zero():
        return "0"

    @staticmethod
    def comma():
        return "."

    def give_answer(self):
        try:
            result = eval(self.label_calcul.cget("text"))
            self.label_calcul.configure(text=str(result))
            self._ = result
        except Exception as error_name:
            print(error_name)

Main = App()

Main.mainloop()
