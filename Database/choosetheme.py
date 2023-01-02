from ColorTheme import *


def chooseTheme():
    input_theme = input("Choose Theme: ")
    if input_theme == "Dark" or input_theme == "dark":
        return darkTheme() 
    elif input_theme == "Light" or input_theme == "light":
        return lightTheme()