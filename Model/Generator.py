from sklearn import ensemble
import sklearn as sk
import pandas as pd
import pickle
import matplotlib.pyplot as plt

class model:
    def __init__(self,params):
        self.fileName = params.getFilePath()
        self.testSize = params.getTestSize()
        self.random = params.getRandom()
        self.savePath = params.getSavePath()
    
    def generate(self,x,y):
        file = self.fileName
        testSize = self.testSize
        random = self.random
        print(self.fileName)
        try:
            df = pd.read_csv(file)
            X = df[x]
            X = pd.get_dummies(X)
            Y = df[y]
            X_TRAIN,X_TEST ,Y_TRAIN,Y_TEST = sk.model_selection.train_test_split(X,Y,test_size = testSize,random_state = random)
            model = ensemble.ExtraTreesClassifier()
            model.fit(X_TRAIN,Y_TRAIN)
            model.decision_path(X_TRAIN)
            Y_PRED = model.predict(X_TEST)
            accuracy_score = round((sk.metrics.accuracy_score(Y_TEST,Y_PRED)*100),2)
            print (f"Accuracy : {accuracy_score}%")
            return(model)
        except Exception as e:
            print("Error :" , e)
            
    def getHead(self):
        file = self.fileName
        try:
            df = pd.read_csv(file)
            head = df.columns
            col = [cols for cols in head]
            return(col)
        except Exception as e:
            print("Error while retrieving", e)
            
    def save(self,model):
        file = self.savePath + ".h5"
        pickle.dump(model, open(file, 'wb'))
        
       
        