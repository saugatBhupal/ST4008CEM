from tkinter import *

def getLoginFrame(window, register, controller, login):
    login.getLoginFrame(window, register,controller, login)

def validate(username, fullname, email, password, confirmpassword, controller):
    if(username,fullname,email,password,confirmpassword != ""):
        if(password == confirmpassword):
            controller.register(username,
                                fullname,
                                email,
                                password)

def getRegistrationFrame(window, register, controller, login):
    registerFrame = Frame(window, background="#F5F9FF")
    registerFrame.place(x=347,y=0, height=800, width=993)

    title = Label(registerFrame, text="Register",anchor='w',font=('Quicksand Light Regular',30),foreground='#7066D4',background='#F5F9FF')
    title.place(height=65, width=252,x=82, y = 99)

    username=Label(registerFrame, text="Username",anchor='w',font=("Quicksand Medium",18),background='#F5F9FF')
    username.place(x=82, y=189, height=23,width=145)

    usernameVar = StringVar()
    usernameInput=Entry(registerFrame , textvariable= usernameVar,  font=("Quicksand Light Regular",20),foreground="#514F4F", borderwidth=0,background='#F5F9FF')
    usernameInput.place(x=104, y=241, width=270)

    lineUsername = Canvas(registerFrame, width=314, height=1,bg="#7066D4", highlightthickness=0)
    lineUsername.place(x=82, y=280)

    fullname=Label(registerFrame, text="Full Name",anchor='w',font=("Quicksand Medium",18),background='#F5F9FF')
    fullname.place(x=82, y=296, height=23,width=145)

    fullnameVar = StringVar()
    fullname=Entry(registerFrame , textvariable= fullnameVar,  font=("Quicksand Light Regular",20),foreground="#514F4F", borderwidth=0,background='#F5F9FF')
    fullname.place(x=104, y=342, width=270)

    lineFullname = Canvas(registerFrame, width=314, height=1,bg="#7066D4", highlightthickness=0)
    lineFullname.place(x=82, y=381)

    email=Label(registerFrame, text="Email Address",anchor='w',font=("Quicksand Medium",18),background='#F5F9FF')
    email.place(x=82, y=396, height=23,width=145)

    emailVar = StringVar()
    emailinput=Entry(registerFrame , textvariable= emailVar, font=("Quicksand Light Regular",20),foreground="#514F4F", borderwidth=0,background='#F5F9FF')
    emailinput.place(x=104, y=446,width=270)

    lineEmail = Canvas(registerFrame, width=314, height=1,bg="#7066D4", highlightthickness=0)
    lineEmail.place(x=82, y=485)

    password=Label(registerFrame, text="Create Password",anchor='w',font=("Quicksand Medium",18),background='#F5F9FF')
    password.place(x=444, y=191, height=23,width=145)

    passwordVar = StringVar()
    passwordInput=Entry(registerFrame , show='•', textvariable= passwordVar, font=("Quicksand Light Regular",20),foreground="#514F4F", borderwidth=0,background='#F5F9FF')
    passwordInput.place(x=464, y=240,width=270)

    linePassword = Canvas(registerFrame, width=314, height=1,bg="#7066D4", highlightthickness=0)
    linePassword.place(x=445, y=279)

    confirmPassword=Label(registerFrame, text="Confirm Password",anchor='w',font=("Quicksand Medium",18),background='#F5F9FF')
    confirmPassword.place(x=444, y=296, height=23,width=145)

    confirmPasswordVar = StringVar()
    confirmPasswordInput=Entry(registerFrame ,show= '•',  textvariable= confirmPasswordVar, font=("Quicksand Light Regular",20),foreground="#514F4F", borderwidth=0,background='#F5F9FF')
    confirmPasswordInput.place(x=469, y=341,width=270)

    lineConfirmPassword = Canvas(registerFrame, width=314, height=1,bg="#7066D4", highlightthickness=0)
    lineConfirmPassword.place(x=445, y=381)

    lineLeft = Label(registerFrame, background="#7066D4")
    lineLeft.place(height=610, width=1, x=59, y=90)

    lineBottom = Label(registerFrame, background="#7066D4")
    lineBottom.place(height=1, width=719, x=59, y=700)

    lineRightTop = Label(registerFrame, background="#7066D4")
    lineRightTop.place(height=1, width=75, x=704, y=85)

    lineRightBottom = Label(registerFrame, background="#7066D4")
    lineRightBottom.place(height=75, width=1, x=778, y=85)

    lineSeparator = Label(registerFrame, background="#7066D4")
    lineSeparator.place(height=312, width=1, x=419, y=175)

    var = IntVar()
    check = Checkbutton(registerFrame, text="I agree with the terms and conditions", fg="#7066D4", bg="#F5F9FF", variable=var, font=(
    "Quicksand Medium", 15), highlightbackground="#7066D4", highlightthickness=1)
    check.place(x=197, y=547   )

    registerButton = Label(registerFrame, text="Create Account", fg="#ffffff", bg="#7066D4",width=30, height=2, font=("Quicksand SemiBold", 17), cursor="hand")
    registerButton.place(x=204, y=580, height=50, width=459)
    registerButton.bind('<Enter>', lambda event: registerButton.config(background='#594CE0'))
    registerButton.bind('<Leave>', lambda event: registerButton.config(background='#7066D4'))
    registerButton.bind('<Button-1>', lambda event:validate(
                                                            usernameVar.get(),
                                                            fullnameVar.get(),
                                                            emailVar.get(),
                                                            passwordVar.get(),
                                                            confirmPasswordVar.get(),
                                                            controller))
    
    alreadyHaveAnAccount=Label(registerFrame, text="Already have an account?", font=("Quicksand Medium",15),background='#F5F9FF')
    alreadyHaveAnAccount.place(x=202, y=645)

    loginPage = Label(registerFrame, text="Login", fg="#6E64D7", font=(
    "Quicksand Bold", 15), cursor="hand", background='#F5F9FF')
    loginPage.place(x=400, y=645)
    loginPage.bind('<Button-1>', lambda event: getLoginFrame(window, register,controller, login))

    return (registerFrame)
