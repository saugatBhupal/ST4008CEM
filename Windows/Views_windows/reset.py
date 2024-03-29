from tkinter import *
root=Tk()

root.title("Reset Page")
root.geometry("853x800")
root.config(bg="#FFFFFF")

resetFrame = Frame(root, background="#F5F9FF")
resetFrame.place(x=347,y=0, height=800, width=993)

title = Label(resetFrame, text="RESET YOUR PASSWORD",anchor='w',font=('Quicksand Medium',25),foreground='#7066D4',background='#F5F9FF')
title.place(height=65, width=399, x=199, y=172)

lineLeft = Label(resetFrame, background="#7066D4")
lineLeft.place(height=545, width=1, x=164, y=150)

lineBottom = Label(resetFrame, background="#7066D4")
lineBottom.place(height=1, width=522, x=164, y = 695)

lineRightTop = Label(resetFrame, background="#7066D4")
lineRightTop.place(height=1, width=75,x=613, y = 150)

lineRightBottom = Label(resetFrame, background="#7066D4")
lineRightBottom.place(height=75, width=1,x=688, y = 150)

email = Label(resetFrame, text="Email Address", anchor='w',font=('Quicksand SemiBold',15),foreground='#000000',background='#F5F9FF')
email.place(height=41, width=431, x=199, y=255)

emailVar = StringVar()
emailinput=Entry(resetFrame, textvariable= emailVar, width=32, font=("Quicksand Light Regular",12),foreground="#514F4F", borderwidth=0,background='#F5F9FF')
emailinput.place(x=227, y=294)

linemail=Canvas(resetFrame, width=470, height=1, bg="#7066D4", highlightthickness=0)
linemail.place(x=204, y=333)

newpwd=Label(resetFrame, text="New Password",font=("Quicksand SemiBold",15),background='#F5F9FF')
newpwd.place(x=204, y=365)

newpasswordVar = StringVar()
newpwdinput=Entry(resetFrame,textvariable= newpasswordVar,  width=32, font=("Quicksand Light Regular",12),foreground="#514F4F",borderwidth=0,background='#F5F9FF')
newpwdinput.place(x=227, y=404)

linenewpwd=Canvas(resetFrame, width=470, height=1, bg="#7066D4", highlightthickness=0)
linenewpwd.place(x=204, y=443)

confirmpwd=Label(resetFrame, text="Confirm New Password", font=("Quicksand SemiBold", 15), background="#F5F9FF")
confirmpwd.place(x=204, y=475)

confirmpwdVar = StringVar()
confirmpwd_input=Entry(resetFrame, textvariable=confirmpwdVar, width=32, font=("Quicksand Light Regular", 12), foreground="#514F4F", borderwidth=0, background='#F5F9FF')
confirmpwd_input.place(x=227, y=514)

line_confirmpwd=Canvas(resetFrame, width=470, height=1, bg="#7066D4", highlightthickness=0)
line_confirmpwd.place(x=204, y=553)

resetbutton=Label(resetFrame, text="RESET", fg="#ffffff", bg="#7066D4", width=30, height=2, font=("Quicksand SemiBold",17), cursor="hand1")
resetbutton.place(x=204, y=610, height=50, width=459)

resetbutton.bind('<Enter>',lambda event: resetbutton.config(background='#594CE0'))
resetbutton.bind('<Leave>',lambda event: resetbutton.config(background='#7066D4'))

root.mainloop()