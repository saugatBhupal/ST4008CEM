from tkinter import *
from customtkinter import *
window = Tk()
window.geometry("1280x800")
window.configure(bg="#f2eefc")

register_frame = Frame(window, background="#F5F9FF")
register_frame.place(x=347, y=0, height=800, width=993)



# ________LINES_________________________________________________________

#line1(vertical left)
line1 = Canvas(register_frame, width=1, height=674, bg="#6E64D7")
line1.place(x=164, y=150, height=545, width=1)

#line2(horizontal bottom)
line2 = Canvas(register_frame, width=1000, height=1, bg="#6E64D7")
line2.place(x=164, y=695)

#line3(horizonatal mid)
line3 = Canvas(window, width=1, height=282, bg="#9E96E9")
line3.place(x=910, y=205)   

#line4(horizontal line top right)
line4 = Canvas(window, width=75, height=1, bg="#9E96E9")
line4.place(x=1398, y=85)

#line5(vertical line top right)
line5 = Canvas(window, width=1, height=73, bg="#9E96E9")
line5.place(x=1469, y=86)


#________________TEXTS____________________________________________________________________________________________


#back
back = Label(window, text="Back", fg="#6E64D7", bg="#f2eefc", font=("Quicksand",16))
back.place(x=1425, y=28 )
arrow=Canvas(window, width=35, height=16, bg="#f2eefc", highlightthickness=0)
arrow.create_line(0, 10, 300, 10, fill="#6E64D7", arrow="first")
arrow.place(x=1390, y=35)

#register text
registration = Label(window, text="Registration", fg="#6E64D7", bg="#f2eefc", font=("Quicksand",30))
registration.place(x=450, y=90)

#username
uname = Label(window, text="Username", font=("Quicksand", 16), fg="#000000", bg="#FFFFFF")
uname.place(x=450, y=207)
#username-input
uname_input = Entry(window, fg="#000000", bg="#f2eefc", width=30,borderwidth=0, font=("Quicksand",12))
uname.configure(bg="#f2eefc")
uname_input.place(x=473,y=259, height=27)
canvas_name= Canvas(window, width=390, height=1, bg="#6E6ED7")
canvas_name.place(x=450, y=298)


#Email
email = Label(window, text="Email Address", font=("Quicksand",16), fg="#000000", bg="#f2eefc")
email.place(x=450, y=339)
#Email-input
email_input = Entry(window, fg="#000000", bg="#f2eefc",width=30, font=("Quicksand",12), borderwidth=0)
email_input.place(x=473, y=389, height=27)
canvas_email= Canvas(window, width=390, height=1, bg="#6E6ED7")
canvas_email.place(x=450, y=428)


#Password
password = Label(window, text="Password", font=("Quicksand",16), fg="#000000", bg="#f2eefc")
password.place(x=985, y=205)
#password-input
password_input = Entry(window, fg="#000000", bg="#f2eefc", borderwidth=0,width=60,font=("Quicksand",12))
password_input.place(x=985, y=255, height=27)
canvas_pwd= Canvas(window, width=390, height=1, bg="#6E6ED7")
canvas_pwd.place(x=985, y=295)


#confirm-pwd
confirm_password = Label(window, text="Confirm Password", font=("Quicksand",16), fg="#000000", bg="#f2eefc")
confirm_password.place(x=985, y=333)
#confirm-pwd-input
confirm_password_input = Entry(window, fg="#000000", bg="#f2eefc",width=60, borderwidth=0, font=("Quicksand",12))
confirm_password_input.place(x=985, y=383, height=27)
canvas_confpwd= Canvas(window, width=390, height=1, bg="#6E6ED7")
canvas_confpwd.place(x=985, y=423)


#checkbox-keep_me_logged_in
keep_me_logged_in = CTkCheckBox(window,text="Keep me logged in", font=("Quicksand",15),checkbox_width=20, checkbox_height=20, border_color="#6E64D7", border_width=1, fg_color="#6E64D7" )
keep_me_logged_in.place(x=800,y=539)


#create_acc-button
create_acc = CTkButton(window, text="Create Account", font=("Quicksand",20), fg_color="#6E64D7", bg_color="#FFFFFF")
create_acc.place(x=800, y=572, width=451, height=59)
create_acc.bind('<Enter>',lambda event: create_acc.config(bg_color='#ffffff',fg_color='#6E64D7'))
create_acc.bind('<Leave>',lambda event: create_acc.config(bg_color='#6E64D7',fg_color='#6E64D7'))

#already_have_acc-text
alr_have_acc = Label(window, text="Already have an account?", font=("Quicksand",12), fg="#000000", bg="#f2eefc")
alr_have_acc.place(x=800, y=645)

#sign_in
sign_in = Label(window, text="Sign in", font=("Quicksand",12), fg="#6E64D7", bg="#f2eefc")
sign_in.place(x=999, y=645)


window.mainloop()