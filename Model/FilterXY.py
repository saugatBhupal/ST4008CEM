def filterXY(arr, Y):
    X = []
    cols = []
    cols = arr.copy()
    try:
        cols.remove(Y)
        X = cols.copy()
        return(X,Y)
    except:
        print(f"ERROR {Y} is not a column")