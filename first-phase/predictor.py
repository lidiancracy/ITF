from java_parser_util import tokenzierImp, tokenzierImpIdentifier
from nltk_util import (countFreRecomm, countMaxWord, getAdj, getNoun,
                       wordTagging)
from seq2seq_predictor import seq2seqPredictor


def predictor(typz,context,body,summerizer):
    if typz=='get':
        bodyContext=' '.join(tokenzierImpIdentifier(body))
        predictName=getPredict(bodyContext)
        return typz+' '+ predictName
    elif typz=='set':
        bodyContext=' '.join(tokenzierImpIdentifier(body))
        predictName=setPredict(bodyContext)
        return 'set'+' '+predictName
    elif typz=='test':
        bodyContext=' '.join(tokenzierImpIdentifier(body))
        predictName=testPredict(bodyContext)
        return 'test'+' '+predictName
    elif typz=='is':
        bodyContext=' '.join(tokenzierImpIdentifier(body))
        predictName=isPredict(bodyContext)
        return  'is'+' '+predictName
    elif  typz=='main':
        return typz
    elif typz=='equals':
        return typz
    elif typz=='hash':
        return typz
    else:
        return summerizer.summarize(context)

def getPredict(context):
    nnLst=wordTagging(context)
    nnLst=getNoun(nnLst)
    
    countNN=countMaxWord(nnLst)
    if len(countNN)==0:
        return countFreRecomm(context)
    else:
        return countNN[0][0]

def setPredict(context):
    nnLst=wordTagging(context)
    nnLst=getNoun(nnLst)
    countNN=countMaxWord(nnLst)
    if len(countNN)==0:
        return countFreRecomm(context)
    else:
        return countNN[0][0]
    
def isPredict(context):
    JJLst=wordTagging(context)
    JJLst=getAdj(JJLst)
    countNN=countMaxWord(JJLst)
    if len(countNN)==0:
        return countFreRecomm(context)
    else:
        return countNN[0][0]

def testPredict(context):
    nnLst=wordTagging(context)
    nnLst=getNoun(nnLst)
    countNN=countMaxWord(nnLst)
    if len(countNN)==0:
        return countFreRecomm(context)
    else:
        return countNN[0][0]
    

def invocationPredicon():
    pass

def n_gramPredictor():
    pass
