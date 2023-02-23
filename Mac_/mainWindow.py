from tkinter import *
from tkinter import messagebox
from Config import setting, config
from Views import login,register,home,modelPreferences,settingsPage,resetPassword
from Model import paramModel, Generator, FilterXY, Heads
from PIL import Image, ImageTk
import sys
import os


def highlight(field):
    field.config(background='#7066D4',foreground='#ffffff')

def getLoginStatus():
    return setting.session(config)

def getHomePage(homePage, field):
    homePage.getHomePage()
    highlight(field)
    
def getSettingPage(settingPage, field):
    settingPage.getSettingsPage()
    highlight(field)

def logout():
    
    userDetails = {'status':False,'username':""}
    config.saveUser(userDetails)
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
def window(controller):
    theme = setting.theme(config)

    window = Tk()
    window.title('Login')

    settingPage = settingsPage.settingsPage(window, theme, config, setting)
    modelPage = modelPreferences.modelPreferences(window,paramModel,Generator,FilterXY,Heads,setting.readPath(config))
    homePage = home.home(window,controller,theme, modelPage)
    
    photo = PhotoImage(file ='artBoards/icon.png') 
    window.wm_iconphoto(False, photo)
    window.geometry("1280x800")
    
    bgImage = PhotoImage(file='artBoards/background.png')
    dashArea = Label(window,image=bgImage)
    dashArea.place(x=50, y=0, width=1280, height=800 )

    sidebar = Label(window,background=theme['background-color'])
    sidebar.place(x=0,y=0,height=800,width=347)

    generateAModel = Label(window,text="Generate A Model",font=('Quicksand',18),foreground=theme['font-color'],background=theme['background-color'],cursor="hand")
    generateAModel.bind('<Enter>',lambda event: generateAModel.config(background=theme['font-color'],foreground=theme['base']))
    generateAModel.bind('<Leave>',lambda event: generateAModel.config(background=theme['background-color'],foreground=theme['font-color']))
    generateAModel.place(x=0, y=288,height=50,width=347)

    browseModels = Label(window,text="Browse Models",font=('Quicksand',18),foreground=theme['font-color'],background=theme['background-color'],cursor="hand")
    browseModels.place(x=0, y=376, height=50, width=347)
    browseModels.bind('<Enter>',lambda event: browseModels.config(background=theme['font-color'],foreground=theme['base']))
    browseModels.bind('<Leave>',lambda event: browseModels.config(background=theme['background-color'],foreground=theme['font-color']))

    preferences = Label(window,text="Manage Preferences",font=('Quicksand',18),foreground=theme['font-color'],background=theme['background-color'],cursor="hand")
    preferences.place(x=0, y=600, height=50, width=347)
    preferences.bind('<Enter>',lambda event: preferences.config(background=theme['font-color'],foreground=theme['base']))
    preferences.bind('<Leave>',lambda event: preferences.config(background=theme['background-color'],foreground=theme['font-color']))

    account = Label(window,text="Account",font=('Quicksand',18),foreground=theme['font-color'],background=theme['background-color'],cursor="hand")
    account.place(x=0, y=678, height=50, width=347)
    account.bind('<Enter>',lambda event: account.config(background=theme['font-color'],foreground=theme['base']))
    account.bind('<Leave>',lambda event: account.config(background=theme['background-color'],foreground=theme['font-color']))

    modelTitle = Label(window,text='Models',font=('Quicksand',18),foreground=theme['font-color'],background=theme['background-color'])
    modelTitle.place(x=140, y=198, w=67, h=18)

    line1 = Label(window, background='#7066D4')
    line1.place(x=0, y=205, width=120, height=1)

    line1 = Label(window, background='#7066D4')
    line1.place(x=227, y=205, width=120, height=1)

    settingsTitle = Label(window,text='Settings',font=('Quicksand',18),foreground=theme['font-color'],background=theme['background-color'])
    settingsTitle.place(x=138, y=508, w=67, h=18)

    line2 = Label(window, background='#7066D4')
    line2.place(x=0, y=517, width=120, height=1)
    
    line1 = Label(window, background='#7066D4')
    line1.place(x=227, y=517, width=120, height=1)

    logoImg = PhotoImage(file='artboards/logo-resized.png')
    logo = Label(window,image=logoImg,background=theme['background-color'])
    logo.place(x=80, y=40)
    
    if(getLoginStatus()):
        generateAModel.bind('<Button-1>', lambda event: getHomePage(homePage, generateAModel))
        preferences.bind('<Button-1>', lambda event: getSettingPage(settingPage, preferences))
        account.config(text="Logout")
        account.bind('<Button-1>', lambda event: logout())
    
    if(not getLoginStatus()):
        generateAModel.bind('<Button-1>', lambda event: messagebox.showerror("Error Message", "Please Login Or Create An Account First"))
        preferences.bind('<Button-1>', lambda event: messagebox.showerror("Error Message", "Please Login Or Create An Account First"))
        
    if(getLoginStatus()):
        getHomePage(homePage, generateAModel)
    
    else:    
        log = login.login(window, register, controller, login, home, theme, resetPassword)
        log.getLoginFrame()
        highlight(account)
    window.mainloop()
    
  


    


