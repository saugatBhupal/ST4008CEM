from tkinter import *
from customtkinter import *
root = Tk()
root.geometry("853x800")



frame = Frame(root, background="#F5F9FF")
frame.place(x=347, y=0, height=800, width=993)


#________lines__________________________________________________

line1 = Canvas(frame, width=1, height=570, background="#6E64D7")
line1.place(x=200,y=121)

line2 = Canvas(frame, width=545, height=1, background="#6E64D7")
line2.place(x=200,y=690)

line3 = Canvas(frame, width=1, height=120, background="#6E64D7")
line3.place(x=745,y=121)

line4 = Canvas(frame, width=90, height=1, bg="#6E64D7")
line4.place(x=655,y=121)



# ______texts_____________

# "Model Preferences"
title_text = Label(frame, text="Model Preferences",font=("Quicksand",30), fg="#6E64D7", bg="#F5F9FF")
title_text.place(x=220, y=120)

# "Select Files: "
select_file_txt = Label(frame, text="Select A File To Load: ", font=("Quicksand Medium",15), fg="#000000", bg="#F5F9FF")
select_file_txt.place(x=220, y=220)

# "select a file to load (browse)"- label
def getFilePath():
    try:
        filePath = filedialog.askopenfilename(initialdir="/", title="Select A File")
        return(filePath)
    except Exception as e:
        print("Error retrieve file path", e)
#save files path


# entry box 1
entry1 = Label(frame, width=32, font=("Quicksand",12), fg="#000000", bg="#F5F9FF", borderwidth=0)
entry1.place(x=224, y=260)
entry1_line = Canvas(frame, height=1, width=350, bg="#6E6ED7")
entry1_line.place(x=224, y=290)

browse_open_file = Label(frame, text="Browse", font=("Quicksand Medium",12), fg="#ffffff", bg="#6E64D7", width=9, height=1)
browse_open_file.place(x=450, y=220)
browse_open_file.bind('<Enter>',lambda event: browse_open_file.config(bg='#4638D6',fg='#ffffff'))
browse_open_file.bind('<Leave>',lambda event: browse_open_file.config(bg='#6E64D7',fg='#ffffff'))
browse_open_file.bind('<Button-1>',lambda event: entry1.config(text=getFilePath()))




# "Text size:"
text_size_txt = Label(frame, text="Text Size: ", font=("Quicksand Medium",14), fg="#000000", bg="#F5F9FF")
text_size_txt.place(x=224, y=330)



# "Random state: "
randomstate_txt = Label(frame, text="Random state: ", font=("Quicksand Medium",14), fg="#000000", bg="#F5F9FF")
randomstate_txt.place(x=224, y=410)


# save model as - text
save_model_as = Label(frame, text="Save Model As: ", font=("Quicksand Medium",14), fg="#000000", bg="#F5F9FF")
save_model_as.place(x=224, y=470)


# For the save directory
entry2 = Label(frame, width=32, font=("Quicksand",12), fg="#000000", bg="#F5F9FF", borderwidth=0)
entry2.place(x=224, y=520)
entry2_line = Canvas(frame, height=1, width=350, bg="#6E6ED7")
entry2_line.place(x=224, y=550)



# Browse 2
browse_save_file = Label(frame, text="Browse", font=("Quicksand Medium",12), fg="#ffffff", bg="#6E64D7", width=9, height=1)
browse_save_file.place(x=450, y=470)
browse_save_file.bind('<Enter>',lambda event: browse_save_file.config(bg='#4638D6',fg='#ffffff'))
browse_save_file.bind('<Leave>',lambda event: browse_save_file.config(bg='#6E64D7',fg='#ffffff'))
browse_save_file.bind('<Button-1>',lambda event: entry2.config(text=getFilePath()))



# Generate
generate_text = Label(frame, text="Generate", font=("Quicksand Medium",18), fg="#ffffff", bg="#6E64D7", width=35, height=2)
generate_text.place(x=224, y=580)
generate_text.bind('<Enter>',lambda event: generate_text.config(bg='#4638D6',fg='#ffffff'))
generate_text.bind('<Leave>',lambda event: generate_text.config(bg='#6E64D7',fg='#ffffff'))




#_________________sliders__________

# slide 1 (text size)
def slider_event(value):
    slider_value.config(text=str(int(value)))

textslider = CTkSlider(master=frame,width=300, from_=0, to=100, command=slider_event, fg_color="#6E64D7",progress_color="#8075F7", button_color="#6E64D7", button_hover_color="#8075F7")
textslider.place(x=500, y=349, anchor=CENTER)

slider_value = Label(frame, text='value', bg="#F5F9FF", fg="#000000", font=("Quicksand Medium",11))
slider_value.place(x=669,y=329)
slider_value_l = Canvas(frame, width=39, height=1, bg="#6E64D7")
slider_value_l.place(x=670, y=357)


# slider 2 (random state)
def slider_event2(value2):
    slider_value2.config(text=str(int(value2)))                                         

random_slider = CTkSlider(master=frame,width=270, from_=0, to=100, command=slider_event2, fg_color="#6E64D7",progress_color="#8075F7", button_color="#6E64D7", button_hover_color="#8075F7")
random_slider.place(x=516, y=425, anchor=CENTER)

slider_value2= Label(frame, text='value', bg="#F5F9FF", fg="#000000", font=("Quicksand Medium",11))
slider_value2.place(x=669,y=400)
slider_value_2 = Canvas(frame, width=39, height=1, bg="#6E64D7")
slider_value_2.place(x=668, y=430)





















root.mainloop()