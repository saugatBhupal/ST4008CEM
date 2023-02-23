from tkinter import *
import tkinter
import customtkinter
from PIL import Image, ImageTk
import os
import sys
 
class login:
    def __init__(self,window, register,controller, login, home, theme, resetPassword):
        self.window = window
        self.register = register
        self.controller = controller
        self.login = login
        self.theme = theme
        self.home = home
        self.resetPassword = resetPassword
    
    def validate(self,username, password, linemail, linepwd):
        if(str(username).strip() != "" and str(password).strip() != "" ):
            if(self.controller.login(username,password) == True):
                python = sys.executable
                os.execl(python, python, * sys.argv)
            else:
                tkinter.messagebox.showerror("Error Message", "Incorrect Credentials. Please Try Again.")
                linemail.config(bg="#FF0000")
                linepwd.config(bg="#FF0000")
        else:
            
            tkinter.messagebox.showerror("Error Message", "Please Make Sure All The Fields Are Filled Before Submitting")
            linemail.config(bg="#FF0000")
            linepwd.config(bg="#FF0000")

    def getRegisterPage(self):
        reg = self.register.register(self.window, self.register, self.controller,self.login,self.home, self.theme, self.resetPassword)
        reg.getRegistrationFrame()
    
    def getHomePage(self):
        homePage = self.home.home(self.window,self.controller,self.theme)
        homePage.getHomePage()
    
    def getResetPassword(self):
        reset = self.resetPassword.resetPassword(self.window, self.theme, True, self.login.login(self.window, self.register, self.controller, self.login,self.home, self.theme, self.resetPassword))
        reset.getResetPage()
    
    
    def getLoginFrame(self):
        theme = self.theme
    
        loginFrame = Frame(self.window, background=theme['background-frame'])
        loginFrame.place(x=347,y=0, height=800, width=993)

        title = Label(loginFrame, text="LOGIN",anchor='w',font=('Quicksand Light Regular',30),foreground=theme['font-color'],background=theme['background-frame'])
        title.place(height=65, width=252,x=199, y = 169)

        titleSub = Label(loginFrame, text="Enter Your Credentials",anchor='w',font=('Quicksand Light',22),foreground=theme['title'],background=theme['background-frame'])
        titleSub.place(height=41, width=431,x=199, y = 225)

        lineLeft = Label(loginFrame, background="#7066D4")
        lineLeft.place(height=534, width=1,x=164, y = 150)

        lineBottom = Label(loginFrame, background="#7066D4")
        lineBottom.place(height=1, width=522,x=164, y = 684)

        lineRightTop = Label(loginFrame, background="#7066D4")
        lineRightTop.place(height=1, width=75,x=613, y = 150)

        lineRightBottom = Label(loginFrame, background="#7066D4")
        lineRightBottom.place(height=75, width=1,x=688, y = 150)

        email=Label(loginFrame, text="Email Address",anchor='w',font=("Quicksand Medium",18),foreground= theme['title'],background=theme['background-frame'])
        email.place(x=204, y=278, height=23,width=145)

        emailVar = StringVar()
        emailinput=Entry(loginFrame, textvariable= emailVar, width=32, font=("Quicksand Light Regular",20),foreground=theme['title'], borderwidth=0,background=theme['background-frame'],highlightthickness=0, highlightbackground=theme['background-frame'])
        emailinput.place(x=227, y=320)

        linemail=Canvas(loginFrame, width=453, height=1, bg="#7066D4", highlightthickness=0)
        linemail.place(x=204, y=359)

        pwd=Label(loginFrame, text="Password",font=("Quicksand Medium",18,),background=theme['background-frame'], foreground=theme['title'])
        pwd.place(x=204, y=390)

        fg_pwd=Label(loginFrame, text="Forgot your Password?", fg="#7066D4", font=("Quicksand SemiBold",12), cursor="hand",background=theme['background-frame'])
        fg_pwd.place(x=530, y=395)
        fg_pwd.bind('<Button-1>', lambda event:self.getResetPassword())

        passwordVar = StringVar()
        pwdinput=Entry(loginFrame,show = '•', textvariable= passwordVar,  width=26, font=("Quicksand Light Regular",25),foreground=theme['title'], borderwidth=0,background=theme['background-frame'],highlightthickness=0, highlightbackground=theme['background-frame'])
        pwdinput.place(x=227, y=440)

        linepwd=Canvas(loginFrame, width=453, height=1, bg="#7066D4", highlightthickness=0)
        linepwd.place(x=204, y=481)

        var = IntVar()
        check=Checkbutton(loginFrame, text="Keep me logged in", fg=theme['font-color'], bg=theme['background-frame'], variable=var, font=("Quicksand Medium",15), highlightbackground="#7066D4", highlightthickness=0)
        check.place(x=204, y=515)

        logbutton=Label(loginFrame, text="LOGIN", fg="#ffffff", bg="#7066D4", width=30, height=2, font=("Quicksand SemiBold",17), cursor="hand")
        logbutton.place(x=204, y=561 , height=50, width=459)

        logbutton.bind('<Enter>',lambda event: logbutton.config(background='#594CE0'))
        logbutton.bind('<Leave>',lambda event: logbutton.config(background='#7066D4'))
        logbutton.bind('<Button-1>',lambda event: self.validate(emailVar.get(), 
                                                       passwordVar.get(), 
                                                       linemail,
                                                       linepwd))

        dacc=Label(loginFrame, text="Don't have an account?", font=("Quicksand Medium",15),foreground=theme['title'],background=theme['background-frame'])
        dacc.place(x=204, y=626)

        reg=Label(loginFrame, text="Register", fg="#6E64D7", font=("Quicksand Bold",15), cursor="hand",background=theme['background-frame'])
        reg.place(x=375, y=626)
        reg.bind('<Button-1>', lambda event: self.getRegisterPage())
    
        return(loginFrame)


