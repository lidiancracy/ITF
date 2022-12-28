import os
import warnings

from context_util import hump2underline
from java_parser_util import tokenzierImp, tokenzierImpIdentifier
from pre_predictor import (pre_delegations_predictor, pre_getter_predictor,
                           pre_predictor, pre_setter_predictor)
from seq2seq_predictor import seq2seqPredictor

os.environ["CUDA_VISIBLE_DEVICES"] = "1"
warnings.filterwarnings('ignore')
from context_util import transfromMethod2Context
from fastText_classifier import fastText_classification, load_classifier
from load_data_util import loadData
from predictor import predictor


def processMethodName(name):
    name=name.split(' ')
    templ=[]
    [templ.append(i) for i in name if not i in templ]
    name=templ
    name=[hump2underline(x) for x in name]
    return ' '.join(name).replace('_','').lower()

if __name__ == '__main__':
    print('starting...')
    methodList=loadData('../data/example-data/liu-kui-data.txt')
    classifier=load_classifier()
    summarizer=seq2seqPredictor()
    predict_list=[]
    real_list=[]
    for method in methodList:
        context,body,name=transfromMethod2Context(method)
        if context=='' or body=='' or name=='':
            continue  
        mylst=tokenzierImp(body) 
        predictName,pre_flag=pre_predictor(mylst)
        if pre_flag:
            predictName=processMethodName(predictName)
            name=processMethodName(name)
            print('{} | {}'.format(predictName,name))
            predict_list.append(predictName)
            real_list.append(name)
        else:
            method_type=fastText_classification(classifier,context)
            method_type=method_type.replace('__label__','')
            predictName=predictor(method_type,context,body,summarizer)
            name=hump2underline(name)
            predictName=processMethodName(predictName)
            name=processMethodName(name)
            print('{} | {}'.format(predictName,name))
            predict_list.append(predictName)
            real_list.append(name)
        with open('./pred.txt','a') as f:
            for predict in predict_list:
                f.write('{}\n'.format(predict.strip()))
        with open('./label.txt','a') as f:
            for real in real_list:
                f.write('{}\n'.format(real.strip()))

        
        





