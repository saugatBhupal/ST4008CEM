class params:
    def __init__(self, filepath,savePath, testSize , random):
        self.testSize = int(testSize)
        self.random = int(random)
        self.filepath = filepath
        self.savePath = savePath
    def getTestSize(self):
        return(self.testSize)
    def getRandom(self):
        random = self.random
        return(random)
    def getFilePath(self):
        return(self.filepath)
    def getSavePath(self):
        return(self.savePath)
        