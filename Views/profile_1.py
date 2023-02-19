from tkinter import *
from tkinter import ttk
root=Tk()

root.title("Profile Page")
root.geometry("853x800")
root.config(bg="#FFFFFF")

profileFrame = Frame(root, background="#F5F9FF")
profileFrame.place(x=347,y=0, height=800, width=993)

lineRightTop = Label(profileFrame, background="#7066D4")
lineRightTop.place(height=1, width=77, x=860, y=42)

lineRightBottom = Label(profileFrame, background="#7066D4")
lineRightBottom.place(height=75, width=1,x=937, y=42)

logout = Label(profileFrame, background="#7066D4", fg="#ffffff", text="Log Out", font=("Quicksand SemiBold", 12))
logout.place(height=30, width=79, x=848, y=53)

photo = Label(profileFrame, width=24, height=11, bg="#F5F9FF", highlightbackground="#7066D4", highlightthickness=2)
photo.place(x=75, y=78)

profilename = Label(profileFrame, background="#F5F9FF", fg="#7066D4", text= "user101", font=("Quicksand Medium", 20))
profilename.place(x=108, y=255)

fullname = Label(profileFrame, background="#F5F9FF", fg="#000000", text= "Full Name", font=("Quicksand Medium", 17))
fullname.place(x=310, y=78)

fullname_input = Label(profileFrame, width=48, height=2, bg="#F5F9FF", highlightbackground="#7066D4", highlightthickness=2)
fullname_input.place(x=310, y=119)

email = Label(profileFrame, background="#F5F9FF", fg="#000000", text= "Email Address", font=("Quicksand Medium", 17))
email.place(x=310, y=167)

email_input = Label(profileFrame, width=48, height=2, bg="#F5F9FF", highlightbackground="#7066D4", highlightthickness=2)
email_input.place(height=40, x=310, y=208)

modelgenerated = Label(profileFrame, background="#F5F9FF", fg="#000000", text= "Models Generated", font=("Quicksand Medium", 17))
modelgenerated.place(x=72, y=360)

textboxFrame = Frame(root, background="#ffffff")
textboxFrame.place(x=420, y=420, height=362, width=757)

def getProfile():
    return textboxFrame

# textbox = Text(textboxFrame, highlightthickness=0)
# textbox.place(x=0, y=0, width=757)
# textbox.config(state=DISABLED)

scroll = Scrollbar(textboxFrame, orient="vertical", command=getProfile)
scroll.place(x=740, y=0)

model1 = Label(textboxFrame, background="#7066D4", fg="#ffffff", text="Model 1", font=("Quicksand SemiBold", 13))
model1.place(x=30, y=30, width=293, height=42)

model2 = Label(textboxFrame, background="#7066D4", fg="#ffffff", text="Model 2", font=("Quicksand SemiBold", 13))
model2.place(x=434, y=30, width=293, height=42)

model3 = Label(textboxFrame, background="#7066D4", fg="#ffffff", text="Model 3", font=("Quicksand SemiBold", 13))
model3.place(x=30, y=100, width=293, height=42)

model4 = Label(textboxFrame, background="#7066D4", fg="#ffffff", text="Model 4", font=("Quicksand SemiBold", 13))
model4.place(x=434, y=100, width=293, height=42)

model5 = Label(textboxFrame, background="#7066D4", fg="#ffffff", text="Model 5", font=("Quicksand SemiBold", 13))
model5.place(x=30, y=170, width=293, height=42)

model6 = Label(textboxFrame, background="#7066D4", fg="#ffffff", text="Model 6", font=("Quicksand SemiBold", 13))
model6.place(x=434, y=170, width=293, height=42)

model7 = Label(textboxFrame, background="#7066D4", fg="#ffffff", text="Model 7", font=("Quicksand SemiBold", 13))
model7.place(x=30, y=240, width=293, height=42)

model8 = Label(textboxFrame, background="#7066D4", fg="#ffffff", text="Model 8", font=("Quicksand SemiBold", 13))
model8.place(x=434, y=240, width=293, height=42)

model9 = Label(textboxFrame, background="#7066D4", fg="#ffffff", text="Model 9", font=("Quicksand SemiBold", 13))
model9.place(x=30, y=310, width=293, height=42)

model10 = Label(textboxFrame, background="#7066D4", fg="#ffffff", text="Model 10", font=("Quicksand SemiBold", 13))
model10.place(x=434, y=310, width=293, height=42)

# textboxFrame["yscrollcommand"] = scroll.set

root.mainloop()