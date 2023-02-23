import pandas as pd

def getHead(file):
        try:
            df = pd.read_csv(file)
            head = df.columns
            col = [cols for cols in head]
            return(col)
        except Exception as e:
            print("Error while retrieving", e)