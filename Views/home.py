from tkinter import *
from customtkinter import *
from PIL import ImageTk,Image

class home:
    def __init__(self,window,controller,theme,modelPage):
        self.window = window
        self.controller = controller
        self.theme = theme 
        self.modelPage = modelPage
    
    def getModelPage(self):
        self.modelPage.getFrame();
    
    def getHomePage(self):
        theme = self.theme
        window = self.window
        
        homeFrame = Frame(window, background=theme['background-frame'])
        homeFrame.place(x=347,y=0, height=800, width=993)
        
        sq1=Label(homeFrame, background=theme['font-color'], cursor="hand")
        
        sq1.place(x=50, y=170, width=180, height=160)
        sq1.bind('<Button-1>', lambda event:self.getModelPage())
        sq1.bind('<Enter>',lambda event: sq1.config(background='#594CE0'))
        sq1.bind('<Leave>',lambda event: sq1.config(background=theme['font-color']))

        sq2=Label(homeFrame,background=theme['font-color'], text="", cursor="hand")
        sq2.place(x=338, y=170, width=180, height=160)
        sq2.bind('<Button-1>', lambda event:self.getModelPage())
        sq2.bind('<Enter>',lambda event: sq2.config(background='#594CE0'))
        sq2.bind('<Leave>',lambda event: sq2.config(background=theme['font-color']))

        sq3=Label(homeFrame, background=theme['font-color'], text="", cursor="hand")
        sq3.place(x=620, y=170, width=180, height=160)
        sq3.bind('<Button-1>', lambda event:self.getModelPage())
        sq3.bind('<Enter>',lambda event: sq3.config(background='#594CE0'))
        sq3.bind('<Leave>',lambda event: sq3.config(background=theme['font-color']))

        ranforest=Label(homeFrame, text="Random Forest\nClassifier", fg="#ffffff", background=theme['font-color'], font=("Quicksand SemiBold", 13))
        ranforest.place(x=83, y=228)

        dectree=Label(homeFrame, text="Decision Tree\nClassifier", fg="#ffffff", background=theme['font-color'], font=("Quicksand SemiBold", 13))
        dectree.place(x=377, y=225)

        extratree=Label(homeFrame, text="Extra Tree Classifier", fg="#ffffff", background=theme['font-color'], font=("Quicksand SemiBold", 13))
        extratree.place(x=640, y=235)

        sq4=Label(homeFrame,background=theme['font-color'],text="", cursor="hand")
        sq4.bind('<Button-1>', lambda event:self.getModelPage())
        sq4.place(x=54, y=410, width=180, height=160)
        sq4.bind('<Enter>',lambda event: sq4.config(background='#594CE0'))
        sq4.bind('<Leave>',lambda event: sq4.config(background=theme['font-color']))

        sq5=Label(homeFrame,background=theme['font-color'], cursor="hand")
        sq5.bind('<Button-1>', lambda event:self.getModelPage())
        sq5.place(x=339, y=408, width=180, height=160)
        sq5.bind('<Enter>',lambda event: sq5.config(background='#594CE0'))
        sq5.bind('<Leave>',lambda event: sq5.config(background=theme['font-color']))

        sq6=Label(homeFrame,background=theme['font-color'], cursor="hand")
        sq6.bind('<Button-1>', lambda event:self.getModelPage())
        sq6.place(x=620, y=408, width=180, height=160)
        sq6.bind('<Enter>',lambda event: sq6.config(background='#594CE0'))
        sq6.bind('<Leave>',lambda event: sq6.config(background=theme['font-color']))

        lineareg=Label(homeFrame, text="Linear Regressor", fg="#ffffff", background=theme['font-color'], font=("Quicksand SemiBold", 13))
        lineareg.place(x=82, y=476)

        randomreg=Label(homeFrame, text="Random Forest\nRegressor", fg="#ffffff", background=theme['font-color'], font=("Quicksand SemiBold", 13))
        randomreg.place(x=375, y=465)

        extrareg=Label(homeFrame, text="Extra Tree Regressor", fg="#ffffff", background=theme['font-color'], font=("Quicksand SemiBold", 13))
        extrareg.place(x=640, y=475)
        
        return(homeFrame)
