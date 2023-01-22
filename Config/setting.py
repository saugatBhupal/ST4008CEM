import config
def theme(config):
    dark_theme = {"font-color":"#7066D4","background-color":"#1F2127","base":"#FFFFFF"}
    light_theme = {"font-color":"#6E64D7","background-color":"#FFFFFF","base":"#FFFFFF"}
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

session(config)
    