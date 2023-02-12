from tkinter import *
root=Tk()
import customtkinter

def getSettingPage(root, theme):
    
    settingsFrame = Frame(root, background=theme['background-frame'])
    settingsFrame.place(x=347,y=0, height=800, width=993)

    title = Label(settingsFrame, text="Manage your Preferences",anchor='w',font=('Quicksand Medium',25),foreground='#6E64D7',background='#F5F9FF')
    title.place(height=65, width=405, x=199, y=172)

    lineLeft = Label(settingsFrame, background="#6E64D7")
    lineLeft.place(height=545, width=1, x=164, y=150)

    lineBottom = Label(settingsFrame, background="#6E64D7")
    lineBottom.place(height=1, width=594, x=164, y = 695)

    lineRightTop = Label(settingsFrame, background="#6E64D7")
    lineRightTop.place(height=1, width=75, x=685, y = 150)

    lineRightBottom = Label(settingsFrame, background="#6E64D7")
    lineRightBottom.place(height=75, width=1,x=760, y = 150)

    arrow=Canvas(settingsFrame, width=35, height=16, bg="#F5F9FF", highlightthickness=0)
    arrow.create_line(0, 10, 300, 10, fill="#6E64D7", arrow="first")
    arrow.place(x=810, y=43)

    back=Label(settingsFrame, text="Back", fg="#6E64D7", bg="#F5F9FF", font=("Quicksand",20))
    back.place(x=857, y=28)

    theme = Label(settingsFrame, text="Dark Mode", font=('Quicksand Medium',20),foreground='#6E64D7',background='#F5F9FF')
    theme.place(x=222, y=288)

    switch_var = customtkinter.StringVar(value="on")
    def switch_event():
        print("switch toggled, current value:", switch_var.get())

    switch_1 = customtkinter.CTkSwitch(master=settingsFrame, text="", command=switch_event, fg_color="#FFFFFF", button_color="#6E64D7", button_hover_color="#7F75ED", border_color="#6E64D7", progress_color="#B49BFB", switch_width=50, switch_height=25, corner_radius=40, border_width=2,variable=switch_var, onvalue="Dark", offvalue="Light")
    switch_1.place(x=540,y=298)

    savepath = Label(settingsFrame, text="Model Save Path", font=('Quicksand Medium',20),foreground='#6E64D7',background='#F5F9FF')
    savepath.place(x=222, y=384)

    savepath1=Label(settingsFrame, text="/Home/Datasets/Data1.csv", font=('Quicksand Medium',15),foreground='#514F4F',background='#F5F9FF')
    savepath1.place(x=229, y=446)

    savepathline=Label(settingsFrame, background="#6E64D7")
    savepathline.place(height=1, width=261, x=226, y=479)

    browsebutton1=Label(settingsFrame, text="Browse", font=('Quicksand Medium',15),foreground='#ffffff',background='#6E64D7')
    browsebutton1.place(height=42, width=83, x=535, y=437)

    readpath = Label(settingsFrame, text="Model Read Path", font=('Quicksand Medium',20),foreground='#6E64D7',background='#F5F9FF')
    readpath.place(x=222, y=525)

    readpath1 = Label(settingsFrame, text="/Home/Datasets/Data1.csv", font=('Quicksand Medium',15),foreground='#514F4F',background='#F5F9FF')
    readpath1.place(x=229, y=587)

    readpathline=Label(settingsFrame, background="#6E64D7")
    readpathline.place(height=1, width=261, x=226, y=620)

    browsebutton2=Label(settingsFrame, text="Browse", font=('Quicksand Medium',15),foreground='#ffffff',background='#6E64D7')
    browsebutton2.place(height=42, width=83, x=535, y=578)
    
    return settingsFrame



""""
###############
root.title("Settings")
root.geometry("853x800")
root.config(bg="#FFFFFF")

settingsFrame = Frame(root, background="#F5F9FF")
settingsFrame.place(x=347,y=0, height=800, width=993)

title = Label(settingsFrame, text="Manage your Preferences",anchor='w',font=('Quicksand Medium',25),foreground='#6E64D7',background='#F5F9FF')
title.place(height=65, width=405, x=199, y=172)

lineLeft = Label(settingsFrame, background="#6E64D7")
lineLeft.place(height=545, width=1, x=164, y=150)

lineBottom = Label(settingsFrame, background="#6E64D7")
lineBottom.place(height=1, width=594, x=164, y = 695)

lineRightTop = Label(settingsFrame, background="#6E64D7")
lineRightTop.place(height=1, width=75, x=685, y = 150)

lineRightBottom = Label(settingsFrame, background="#6E64D7")
lineRightBottom.place(height=75, width=1,x=760, y = 150)

arrow=Canvas(settingsFrame, width=35, height=16, bg="#F5F9FF", highlightthickness=0)
arrow.create_line(0, 10, 300, 10, fill="#6E64D7", arrow="first")
arrow.place(x=810, y=43)

back=Label(settingsFrame, text="Back", fg="#6E64D7", bg="#F5F9FF", font=("Quicksand",20))
back.place(x=857, y=28)

theme = Label(settingsFrame, text="Dark Mode", font=('Quicksand Medium',20),foreground='#6E64D7',background='#F5F9FF')
theme.place(x=222, y=288)

switch_var = customtkinter.StringVar(value="on")
def switch_event():
    print("switch toggled, current value:", switch_var.get())

switch_1 = customtkinter.CTkSwitch(master=settingsFrame, text="", command=switch_event, fg_color="#FFFFFF", button_color="#6E64D7", button_hover_color="#7F75ED", border_color="#6E64D7", progress_color="#B49BFB", switch_width=50, switch_height=25, corner_radius=40, border_width=2,variable=switch_var, onvalue="Dark", offvalue="Light")
switch_1.place(x=540,y=298)

savepath = Label(settingsFrame, text="Model Save Path", font=('Quicksand Medium',20),foreground='#6E64D7',background='#F5F9FF')
savepath.place(x=222, y=384)

savepath1=Label(settingsFrame, text="/Home/Datasets/Data1.csv", font=('Quicksand Medium',15),foreground='#514F4F',background='#F5F9FF')
savepath1.place(x=229, y=446)

savepathline=Label(settingsFrame, background="#6E64D7")
savepathline.place(height=1, width=261, x=226, y=479)

browsebutton1=Label(settingsFrame, text="Browse", font=('Quicksand Medium',15),foreground='#ffffff',background='#6E64D7')
browsebutton1.place(height=42, width=83, x=535, y=437)

readpath = Label(settingsFrame, text="Model Read Path", font=('Quicksand Medium',20),foreground='#6E64D7',background='#F5F9FF')
readpath.place(x=222, y=525)

readpath1 = Label(settingsFrame, text="/Home/Datasets/Data1.csv", font=('Quicksand Medium',15),foreground='#514F4F',background='#F5F9FF')
readpath1.place(x=229, y=587)

readpathline=Label(settingsFrame, background="#6E64D7")
readpathline.place(height=1, width=261, x=226, y=620)

browsebutton2=Label(settingsFrame, text="Browse", font=('Quicksand Medium',15),foreground='#ffffff',background='#6E64D7')
browsebutton2.place(height=42, width=83, x=535, y=578)

root.mainloop()
"""