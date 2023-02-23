from tkinter import *
from tkinter import filedialog
from customtkinter import *

class settingsPage:
    def __init__(self, root, theme, config, setting):
        self.root = root
        self.theme = theme
        self.config = config
        self.settting = setting
    
    def getSettingsPage(self):
        
        root = self.root
        theme = self.theme
        config = self.config
        
        backgroud = theme['background-frame']
        
        settingsFrame = Frame(root, background=theme['background-frame'])
        settingsFrame.place(x=347,y=0, height=800, width=993)

        title = Label(settingsFrame, text="Manage your Preferences",anchor='w',font=('Quicksand Medium',25),foreground='#6E64D7',background=theme['background-frame'])
        title.place(height=65, width=405, x=199, y=172)

        lineLeft = Label(settingsFrame, background="#6E64D7")
        lineLeft.place(height=545, width=1, x=164, y=150)

        lineBottom = Label(settingsFrame, background="#6E64D7")
        lineBottom.place(height=1, width=594, x=164, y = 695)

        lineRightTop = Label(settingsFrame, background="#6E64D7")
        lineRightTop.place(height=1, width=75, x=685, y = 150)

        lineRightBottom = Label(settingsFrame, background="#6E64D7")
        lineRightBottom.place(height=75, width=1,x=760, y = 150)

        theme = Label(settingsFrame, text="Dark Mode", font=('Quicksand Medium',20),foreground='#6E64D7',background=theme['background-frame'])
        theme.place(x=222, y=288)

        switch_var = StringVar(value="on")
        def switch_event():
            mode = switch_var.get()
            config.writeConfig("theme", mode)
            if(mode == 'light'):
                python = sys.executable
                os.execl(python, python, * sys.argv)
            
        readpath1 = Label(settingsFrame, text=config.readConfig('model-read-path'), font=('Quicksand Medium',15),foreground='#514F4F',background=backgroud)
        readpath1.place(x=229, y=587)
        
        savepath1=Label(settingsFrame, text=config.readConfig('model-save-path'), font=('Quicksand Medium',15),foreground='#514F4F',background=backgroud)
        savepath1.place(x=229, y=446)
            
        def getFilePath():
            try:
                filePath = filedialog.askdirectory(initialdir="/", title="Select A File")
                savepath1.config(text=filePath)
                config.writeConfig("model-read-path", filePath)
            except Exception as e:
                print("Error retrieve file path", e)
        def savePath():
            try:
                filePath = filedialog.askdirectory(initialdir="/", title="Save Model As:")
                readpath1.config(text=filePath)
                config.writeConfig("model-save-path", filePath)
            except Exception as e:
                print("Error retrieve file path", e)
            

        switch_1 = CTkSwitch(settingsFrame, text="", command=switch_event, fg_color="#FFFFFF", button_color="#6E64D7", button_hover_color="#7F75ED", border_color="#6E64D7", progress_color="#B49BFB", width= 50, height=25, corner_radius=40, border_width=2,variable=switch_var, onvalue="dark", offvalue="light")
        switch_1.place(x=540,y=298)

        savepath = Label(settingsFrame, text="Model Save Path", font=('Quicksand Medium',20),foreground='#6E64D7',background=backgroud)
        savepath.place(x=222, y=384)

        savepathline=Label(settingsFrame, background="#6E64D7")
        savepathline.place(height=1, width=261, x=226, y=479)

        browsebutton1=Label(settingsFrame, text="Browse", font=('Quicksand Medium',15),foreground='#ffffff',background='#6E64D7',cursor="hand")
        browsebutton1.place(height=42, width=83, x=535, y=437)
        browsebutton1.bind('<Button-1>', lambda event:getFilePath())

        readpath = Label(settingsFrame, text="Model Read Path", font=('Quicksand Medium',20),foreground='#6E64D7',background=backgroud)
        readpath.place(x=222, y=525)

        

        readpathline=Label(settingsFrame, background="#6E64D7")
        readpathline.place(height=1, width=261, x=226, y=620)

        browsebutton2=Label(settingsFrame, text="Browse", font=('Quicksand Medium',15),foreground='#ffffff',background='#6E64D7', cursor="hand")
        browsebutton2.place(height=42, width=83, x=535, y=578)
        browsebutton2.bind('<Button-1>', lambda event:savePath())

        return(settingsFrame)