from tkinter import *
class Calculator:
    #Constructor to build all the buttons
    def __init__(self):
        #to check whether the calculator is displaying a result or not
        self.answerstate=False
        self.Ans=0
        
        # to initialize the tkinter gui
        self.root=Tk()
        self.root.title("Calculator")
        
        # The number display whehn inputting values
        self.TextEntry=Entry(self.root,text=" ")
        self.TextEntry.grid(row=0,columnspan=8,padx=10,pady=4)
        
        # adding all the buttons and arranging them in a grid
        self.LPar=Button(self.root,text="(",width=7,height=1,command=lambda:self.changeEntry("("))
        self.LPar.grid(row=1,column=0)
        self.RPar=Button(self.root,text=")",width=7,height=1,command=lambda:self.changeEntry(")"))
        self.RPar.grid(row=1,column=1)
        self.Anse=Button(self.root,text="Ans",width=7,height=1,command=lambda:self.changeEntry("self.Ans"))
        self.Anse.grid(row=1,column=2)
        self.AClear=Button(self.root,text="AC",width=7,height=1,command=lambda:self.changeEntry("AC"))
        self.AClear.grid(row=1,column=3)
        self.Seven = Button(self.root, text="7", width=7, height=1,command=lambda:self.changeEntry("7"))
        self.Seven.grid(row=2, column=0)
        self.Eight=Button(self.root,text="8",width=7,height=1,command=lambda:self.changeEntry("8"))
        self.Eight.grid(row=2,column=1)
        self.Nine=Button(self.root,text="9",width=7,height=1,command=lambda:self.changeEntry("9"))
        self.Nine.grid(row=2,column=2)
        self.Div=Button(self.root,text="/",width=7,height=1,command=lambda:self.changeEntry("/"))
        self.Div.grid(row=2,column=3)
        self.Four=Button(self.root,text="4",width=7,height=1,command=lambda:self.changeEntry("4"))
        self.Four.grid(row=3,column=0)
        self.Five=Button(self.root,text="5",width=7,height=1,command=lambda:self.changeEntry("5"))
        self.Five.grid(row=3,column=1)
        self.Six=Button(self.root,text="6",width=7,height=1,command=lambda:self.changeEntry("6"))
        self.Six.grid(row=3,column=2)
        self.Mul=Button(self.root,text="*",width=7,height=1,command=lambda:self.changeEntry("*"))
        self.Mul.grid(row=3,column=3)
        self.One=Button(self.root,text="1",width=7,height=1,command=lambda:self.changeEntry("1"))
        self.One.grid(row=4,column=0)
        self.Two=Button(self.root,text="2",width=7,height=1,command=lambda:self.changeEntry("2"))
        self.Two.grid(row=4,column=1)
        self.Three=Button(self.root,text="3",width=7,height=1,command=lambda:self.changeEntry("3"))
        self.Three.grid(row=4,column=2)
        self.Minus=Button(self.root,text="-",width=7,height=1,command=lambda:self.changeEntry("-"))
        self.Minus.grid(row=4,column=3)
        self.Zero=Button(self.root,text="0",width=7,height=1,command=lambda:self.changeEntry("0"))
        self.Zero.grid(row=5,column=0)
        self.Dot=Button(self.root,text=".",width=7,height=1,command=lambda:self.changeEntry("."))
        self.Dot.grid(row=5,column=1)
        self.Equal=Button(self.root,text="=",width=7,height=1,command=lambda:self.changeEntry("="))
        self.Equal.grid(row=5,column=2)
        self.Plus=Button(self.root,text="+",width=7,height=1,command=lambda:self.changeEntry("+"))
        self.Plus.grid(row=5,column=3)

    def changeEntry(self,val:str):
        # first must check the state of the calculator
        # if the answerstate is true it means the the calculator is currently
        # displaying the result
        if self.answerstate:
            exp=""
            self.answerstate=False
        # get the current displayed value 
        else:
            exp = self.TextEntry.get()
        
        # clear the display
        self.TextEntry.delete(0, END)
        
        # clear the display
        if val=="AC":
            return
        # evaluate display using python's buildin eval expression function
        elif val=="=":
            # catch any exception
            # one exception to occur would be if two operators are right next to each other
            try:
                answer=eval(exp)
                self.TextEntry.insert(0,answer)
                self.Ans=answer
            except:
                self.TextEntry.insert(0,exp)
            self.answerstate=True
        # otherwise add need input answer to display
        else:
            self.TextEntry.insert(0,exp+val)


    def start(self):
        self.root.mainloop()

