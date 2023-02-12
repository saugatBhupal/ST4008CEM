from tkinter import *
from tkinter import filedialog
from customtkinter import *


class modelPreferences:
    def __init__(self, window, model,generator,filterXY,Heads,readPath):
        self.root = window
        self.model = model
        self.generator = generator
        self.readPath = readPath
        self.filterXY = filterXY
        self.Heads = Heads
        
    def modeller(self, readPath,savePath, testSize, random, PColumn):
        model = self.model
        filterXY = self.filterXY
        params = model.params(readPath,savePath,testSize,random)
        Generator = self.generator.model(params)
        try:
            X,Y = filterXY.filterXY(Generator.getHead(), PColumn)
        except Exception as e:
            print(e)
        else:
            model = Generator.generate(X,Y)
            Generator.save(model)

        
    def getHead(self, filepath):
        return(self.Heads.getHead(filepath))
    
    def getFrame(self):
        frame = Frame(self.root, background="#F5F9FF")
        frame.place(x=347, y=0, height=800, width=993)


        #________lines__________________________________________________

        line1 = Label(frame,  background="#6E64D7")
        line1.place(x=166,y=103, width=1, height=666,)

        line2 = Label(frame, background="#6E64D7")
        line2.place(x=166,y=769, width=522, height=1)

        line3 = Label(frame, background="#6E64D7")
        line3.place(x=690,y=103, width=1, height=73)

        line4 = Label(frame, bg="#6E64D7")
        line4.place(x=615,y=103, width=75, height=1)



        # ______texts_____________

        # "Model Preferences"
        title_text = Label(frame, text="Model Preferences",font=("Quicksand Regular",40), fg="#6E64D7", bg="#F5F9FF")
        title_text.place(x=201, y=119)

        # "Select Files: "
        select_file_txt = Label(frame, text="Select A File To Load: ", font=("Quicksand Medium",18), fg="#000000", bg="#F5F9FF")
        select_file_txt.place(x=205, y=216)

        # "select a file to load (browse)"- label
        def getFilePath():
            try:
                filePath = filedialog.askopenfilename(initialdir="/", title="Select A File")
                return(filePath)
            except Exception as e:
                print("Error retrieve file path", e)
        def savePath():
            try:
                filePath = filedialog.asksaveasfilename(initialdir="/", title="Save Model As:")
                return(filePath)
            except Exception as e:
                print("Error retrieve file path", e)
        #save files path
            
            
        # entry box 1
        entry1 = Label(frame,anchor='w', text = self.readPath,width=50, font=("Quicksand Medium",14), fg="#514f4f", bg="#F5F9FF", borderwidth=0)
        entry1.place(x=213, y=266)

        entry1_line = Label(frame,  bg="#6E6ED7")
        entry1_line.place(x=201, y=300,height=1, width=360)

        browse_open_file = Label(frame, text="Browse", font=("Quicksand SemiBold",12), fg="#ffffff", bg="#6E64D7")
        browse_open_file.place(x=405, y=211,width=100,height=30)
        browse_open_file.bind('<Enter>',lambda event: browse_open_file.config(bg='#4638D6',fg='#ffffff'))
        browse_open_file.bind('<Leave>',lambda event: browse_open_file.config(bg='#6E64D7',fg='#ffffff'))
        browse_open_file.bind('<Button-1>',lambda event: entry1.config(text=getFilePath()))




        # "Test size:"
        test_size_txt = Label(frame, text="Test Size: ", font=("Quicksand Medium",18), fg="#000000", bg="#F5F9FF")
        test_size_txt.place(x=205, y=336)

        # "Prediction Column Text:"
        predictionColumn = Label(frame, text="Prediction Column: ", font=("Quicksand Medium",18), fg="#000000", bg="#F5F9FF")
        predictionColumn.place(x=205, y=459)
        
        columnsLine = Label(frame, bg="#6E6ED7")
        columnsLine.place(x=386, y=481, height=1, width=141)
        
        ColumnVar = StringVar()
        Column = Entry(frame, bg="#F5F9FF",textvariable= ColumnVar, highlightcolor="#F5F9FF", highlightthickness=0, highlightbackground="#F5F9FF", borderwidth=0)
        Column.place(x=386, y=455, width=137, height=25)

        # "Random state: "
        randomstate_txt = Label(frame, text="Random state: ", font=("Quicksand Medium",18), fg="#000000", bg="#F5F9FF")
        randomstate_txt.place(x=205, y=397)

        # save model as - text
        save_model_as = Label(frame, text="Save Model As: ", font=("Quicksand Medium",18), fg="#000000", bg="#F5F9FF")
        save_model_as.place(x=205, y=582)

        # List Columns
        columns = Label(frame,wraplength=440, justify="left", anchor='w', font=("Quicksand",12), fg="#514F4F", bg="#F5F9FF", borderwidth=0)
        columns.place(x=213, y=503,width=440, height=40)
        
        columnsLine = Label(frame, bg="#6E6ED7")
        columnsLine.place(x=201, y=551, height=1, width=450)
        
        # For the save directory
        entry2 = Label(frame,anchor='w', width=50, font=("Quicksand",14), fg="#514F4F", bg="#F5F9FF", borderwidth=0)
        entry2.place(x=213, y=632)

        entry2_line = Label(frame, bg="#6E6ED7")
        entry2_line.place(x=201, y=665, height=1, width=350)

        # Browse 2
        browse_save_file = Label(frame, text="Browse", font=("Quicksand Medium",12), fg="#ffffff", bg="#6E64D7")
        browse_save_file.place(x=405, y=577, width=100, height=30)
        browse_save_file.bind('<Enter>',lambda event: browse_save_file.config(bg='#4638D6',fg='#ffffff'))
        browse_save_file.bind('<Leave>',lambda event: browse_save_file.config(bg='#6E64D7',fg='#ffffff'))
        browse_save_file.bind('<Button-1>',lambda event: entry2.config(text=savePath()))
        
        # Get Columns
        getColumns = Label(frame, text="Columns", font=("Quicksand Medium",12), fg="#ffffff", bg="#6E64D7")
        getColumns.place(x=561, y=461, width=100, height=30)
        getColumns.bind('<Enter>',lambda event: getColumns.config(bg='#4638D6',fg='#ffffff'))
        getColumns.bind('<Leave>',lambda event: getColumns.config(bg='#6E64D7',fg='#ffffff'))
        getColumns.bind('<Button-1>',lambda event: columns.config(text=columns.config(text=self.getHead(entry1.cget("text"))))) 

        #_________________sliders__________
               
        slider_value = Label(frame, text='20', bg="#F5F9FF", fg="#000000", font=("Quicksand Medium",11))
        slider_value.place(x=594,y=333)
        
         # slide 1 (text size)
        def slider_event(value):
            slider_value.config(text=str(int(value)))
        
        testslider = CTkSlider(master=frame,width=231, from_=0, to=100, command=slider_event, fg_color="#6E64D7",progress_color="#8075F7", button_color="#6E64D7", button_hover_color="#8075F7")
        testslider.place(x=450, y=349, anchor=CENTER)
        
        slider_value_l = Label(frame,  bg="#6E64D7")
        slider_value_l.place(x=587, y=354,width=39, height=1)

        slider_value2= Label(frame, text='4', bg="#F5F9FF", fg="#000000", font=("Quicksand Medium",11))
        slider_value2.place(x=594,y=397)
        slider_value_2 = Canvas(frame, width=39, height=1, bg="#6E64D7")
        slider_value_2.place(x=587, y=418)
 
        # slider 2 (random state)
        def slider_event2(value2):
            slider_value2.config(text=str(int(value2)))                                         

        random_slider = CTkSlider(master=frame,width=231, from_=0, to=10, command=slider_event2, fg_color="#6E64D7",progress_color="#8075F7", button_color="#6E64D7", button_hover_color="#8075F7")
        random_slider.place(x=450, y=410, anchor=CENTER)
        
        # Generate
        generate_text = Label(frame, text="Generate", font=("Quicksand Medium",18), fg="#ffffff", bg="#6E64D7", width=35, height=2)
        generate_text.place(x=224, y=688)
        generate_text.bind('<Enter>',lambda event: generate_text.config(bg='#4638D6',fg='#ffffff'))
        generate_text.bind('<Leave>',lambda event: generate_text.config(bg='#6E64D7',fg='#ffffff'))
        generate_text.bind('<Button-1>', lambda event: self.modeller(entry1.cget("text"), entry2.cget("text"), slider_value.cget("text"), slider_value2.cget("text"), ColumnVar.get()))

        
        return(frame)






