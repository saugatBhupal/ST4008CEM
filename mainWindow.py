from tkinter import *
from Views import login,register
from PIL import Image, ImageTk


def highlightAccount(account):
    account.config(background='#7066D4',foreground='#ffffff')

def window(controller):
    
    window = Tk()
    window.title('Login')

    photo = PhotoImage(file ='artBoards/icon.png') 
    window.wm_iconphoto(False, photo)
    window.geometry("1280x800")
    
    bgImage = PhotoImage(file='artBoards/background.png')
    dashArea = Label(window,image=bgImage)
    dashArea.place(x=50, y=0, width=1280, height=800 )

    sidebar = Label(window,background='#ffffff')
    sidebar.place(x=0,y=0,height=800,width=347)

    learnToUse = Label(window,text="Generate A Model",font=('Quicksand',18),background='#ffffff',foreground='#7066D4',cursor="hand")
    learnToUse.bind('<Enter>',lambda event: learnToUse.config(background='#7066D4',foreground='#FFFFFF'))
    learnToUse.bind('<Leave>',lambda event: learnToUse.config(background='#ffffff',foreground='#7066D4'))
    learnToUse.place(x=0, y=288,height=50,width=347)

    generateAModel = Label(window,text="Browse Models",font=('Quicksand',18),background='#ffffff',foreground='#7066D4',cursor="hand")
    generateAModel.place(x=0, y=376, height=50, width=347)
    generateAModel.bind('<Enter>',lambda event: generateAModel.config(background='#7066D4',foreground='#FFFFFF'))
    generateAModel.bind('<Leave>',lambda event: generateAModel.config(background='#ffffff',foreground='#7066D4'))

    browseModels = Label(window,text="Manage Preferences",font=('Quicksand',18),background='#ffffff',foreground='#7066D4',cursor="hand")
    browseModels.place(x=0, y=600, height=50, width=347)
    browseModels.bind('<Enter>',lambda event: browseModels.config(background='#7066D4',foreground='#FFFFFF'))
    browseModels.bind('<Leave>',lambda event: browseModels.config(background='#ffffff',foreground='#7066D4'))

    account = Label(window,text="Account",font=('Quicksand',18),background='#ffffff',foreground='#7066D4',cursor="hand")
    account.place(x=0, y=678, height=50, width=347)
    account.bind('<Enter>',lambda event: account.config(background='#7066D4',foreground='#FFFFFF'))
    account.bind('<Leave>',lambda event: account.config(background='#ffffff',foreground='#7066D4'))

    modelTitle = Label(window,text='Models',font=('Quicksand',18),foreground='#7066D4')
    modelTitle.place(x=140, y=198, w=67, h=18)

    line1 = Label(window, background='#7066D4')
    line1.place(x=0, y=205, width=120, height=1)

    line1 = Label(window, background='#7066D4')
    line1.place(x=227, y=205, width=120, height=1)

    settingsTitle = Label(window,text='Settings',font=('Quicksand',18),foreground='#7066D4')
    settingsTitle.place(x=138, y=508, w=67, h=18)

    line2 = Label(window, background='#7066D4')
    line2.place(x=0, y=517, width=120, height=1)

    line1 = Label(window, background='#7066D4')
    line1.place(x=227, y=517, width=120, height=1)

    logoImg = PhotoImage(file='artboards/logo-resized.png')
    logo = Label(window,image=logoImg)
    logo.place(x=80, y=40)

    login.getLoginFrame(window,register,controller,login)
    highlightAccount(account)
    window.mainloop()
    
  


    


