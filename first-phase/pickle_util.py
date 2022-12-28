import pickle

def saveToFile(p,path):
    with open(path,'wb') as f:
        pickle.dump(p,f)

def loadPickle(path):
    with open(path,'rb') as f:
        p=pickle.load(f)
    return p
