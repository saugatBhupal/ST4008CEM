from tkinter import *
import tkinter
import customtkinter
from PIL import Image, ImageTk
 


def validate(username, password,window,register,controller, login, linemail, linepwd):
    if(str(username).strip() != "" and str(password).strip() != "" ):
       if(controller.login(username,password) == True):
            getRegisterPage(window, register, controller, login)
       else:
            linemail.config(bg="#FF0000")
            linepwd.config(bg="#FF0000")
    else:
        linemail.config(bg="#FF0000")
        linepwd.config(bg="#FF0000")

def getRegisterPage(window, register, controller, login):
    reg = register.register(window, register, controller,login)
    reg.getRegistrationFrame()
    #register.getRegistrationFrame(window, register, controller,login)  
    
def login(status):
    global log
    if(status):
        log = TRUE
    else:
        log = False   

def getLoginFrame(window,register,controller,login):
    
    loginFrame = Frame(window, background="#F5F9FF")
    loginFrame.place(x=347,y=0, height=800, width=993)

    title = Label(loginFrame, text="LOGIN",anchor='w',font=('Quicksand Light Regular',30),foreground='#7066D4',background='#F5F9FF')
    title.place(height=65, width=252,x=199, y = 169)

    titleSub = Label(loginFrame, text="Lorem ipsum dolor sit amet",anchor='w',font=('Quicksand Light',22),foreground='#000000',background='#F5F9FF')
    titleSub.place(height=41, width=431,x=199, y = 225)

    lineLeft = Label(loginFrame, background="#7066D4")
    lineLeft.place(height=534, width=1,x=164, y = 150)

    lineBottom = Label(loginFrame, background="#7066D4")
    lineBottom.place(height=1, width=522,x=164, y = 684)

    lineRightTop = Label(loginFrame, background="#7066D4")
    lineRightTop.place(height=1, width=75,x=613, y = 150)

    lineRightBottom = Label(loginFrame, background="#7066D4")
    lineRightBottom.place(height=75, width=1,x=688, y = 150)

    email=Label(loginFrame, text="Email Address",anchor='w',font=("Quicksand Medium",18),background='#F5F9FF')
    email.place(x=204, y=278, height=23,width=145)

    emailVar = StringVar()
    emailinput=Entry(loginFrame, textvariable= emailVar, width=32, font=("Quicksand Light Regular",20),foreground="#514F4F", borderwidth=0,background='#F5F9FF')
    emailinput.place(x=227, y=320)

    linemail=Canvas(loginFrame, width=453, height=1, bg="#7066D4", highlightthickness=0)
    linemail.place(x=204, y=359)

    pwd=Label(loginFrame, text="Password",font=("Quicksand Medium",18,),background='#F5F9FF')
    pwd.place(x=204, y=390)

    fg_pwd=Label(loginFrame, text="Forgot your Password?", fg="#7066D4", font=("Quicksand SemiBold",17), cursor="hand",background='#F5F9FF')
    fg_pwd.place(x=479, y=392)

    passwordVar = StringVar()
    pwdinput=Entry(loginFrame,show = '•', textvariable= passwordVar,  width=26, font=("Quicksand Light Regular",25),foreground="#514F4F",borderwidth=0,background='#F5F9FF')
    pwdinput.place(x=227, y=440)

    linepwd=Canvas(loginFrame, width=453, height=1, bg="#7066D4", highlightthickness=0)
    linepwd.place(x=204, y=481)

    var = IntVar()
    check=Checkbutton(loginFrame, text="Keep me logged in", fg="#7066D4", bg="#F5F9FF", variable=var, font=("Quicksand Medium",15), highlightbackground="#7066D4", highlightthickness=0)
    check.place(x=204, y=515)

    logbutton=Label(loginFrame, text="LOGIN", fg="#ffffff", bg="#7066D4", width=30, height=2, font=("Quicksand SemiBold",17), cursor="hand")
    logbutton.place(x=204, y=561 , height=50, width=459)

    logbutton.bind('<Enter>',lambda event: logbutton.config(background='#594CE0'))
    logbutton.bind('<Leave>',lambda event: logbutton.config(background='#7066D4'))
    #logbutton.bind('<Button-1>',lambda event: ( login(controller.login(emailVar.get(), passwordVar.get())) if validate(emailVar.get(), passwordVar.get()) else titleSub.config(text =  "Invalid E-Mail or Password")))
    logbutton.bind('<Button-1>',lambda event: validate(emailVar.get(), 
                                                       passwordVar.get(), 
                                                       window,
                                                       register, 
                                                       controller, 
                                                       login,
                                                       linemail,
                                                       linepwd))

    dacc=Label(loginFrame, text="Don't have an account?", font=("Quicksand Medium",15),background='#F5F9FF')
    dacc.place(x=204, y=626)

    reg=Label(loginFrame, text="Register", fg="#6E64D7", font=("Quicksand Bold",15), cursor="hand",background='#F5F9FF')
    reg.place(x=375, y=626)
    reg.bind('<Button-1>', lambda event: getRegisterPage(window, register, controller, login))
    
    return(loginFrame)

