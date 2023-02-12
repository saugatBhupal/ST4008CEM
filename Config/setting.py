
def theme(config):
    dark_theme = {"font-color":"#7066D4","background-color":"#1F2127","base":"#FFFFFF","background-frame":"#000000","title":"#7066D4"}
    light_theme = {"font-color":"#6E64D7","background-color":"#FFFFFF","base":"#FFFFFF", "background-frame": "#F5F9FF", "title":"#000000"}
    if(config.readConfig("theme") == "light"):
        return(light_theme)
    else:
        return(dark_theme)

def session(config):
    print(config.readConfig('login'))
    # if(config.readConfig(['login']) == "true"):
    #     return(True)
    # else:
    #     return(False)


    