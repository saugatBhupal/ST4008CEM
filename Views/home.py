from tkinter import *
from customtkinter import *
from PIL import ImageTk,Image

class home:
    def __init__(self,window,controller,theme):
        self.window = window
        self.controller = controller
        self.theme = theme 
        
    def getHomePage(self):
        window = self.window
        
        homeFrame = Frame(window, background="#F5F9FF")
        homeFrame.place(x=347,y=0, height=800, width=993)

        sq1=CTkLabel(window,bg_color="#ffffff",text="", width=180, height=160)
        sq1.place(x=400, y=150)

        sq2=CTkLabel(window,bg_color="#ffffff",text="", width=180, height=160)
        sq2.place(x=750, y=150)

        sq3=CTkLabel(window,bg_color="#ffffff",text="", width=176, height=160)
        sq3.place(x=1100, y=150)

        ranforest=Label(window, text="Random Forest\nClassifier", fg="#7066D4", bg="#F2F2F2", font=("Quicksand SemiBold", 13))
        ranforest.place(x=428, y=330)

        dectree=Label(window, text="Decision Tree\nClassifier", fg="#7066D4", bg="#F2F2F2", font=("Quicksand SemiBold", 13))
        dectree.place(x=783, y=330)

        extratree=Label(window, text="Extra Tree Classifier", fg="#7066D4", bg="#F2F2F2", font=("Quicksand SemiBold", 13))
        extratree.place(x=1123, y=330)

        sq4=CTkLabel(window,bg_color="#ffffff",text="", width=176, height=160)
        sq4.place(x=400, y=450)

        sq5=CTkLabel(window,bg_color="#ffffff",text="", width=180, height=160)
        sq5.place(x=750, y=450)

        sq6=CTkLabel(window,bg_color="#ffffff",text="",width=180, height=160)
        sq6.place(x=1100, y=450)

        lineareg=Label(window, text="Linear Regressor", fg="#7066D4", bg="#F2F2F2", font=("Quicksand SemiBold", 13))
        lineareg.place(x=415, y=630)

        randomreg=Label(window, text="Random Forest\nRegressor", fg="#7066D4", bg="#F2F2F2", font=("Quicksand SemiBold", 13))
        randomreg.place(x=774, y=630)

        extrareg=Label(window, text="Extra Tree Regressor", fg="#7066D4", bg="#F2F2F2", font=("Quicksand SemiBold", 13))
        extrareg.place(x=1100, y=630)
