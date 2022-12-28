import re

import javalang as jl


def hump2underline(hunp_str):
    p=re.compile(r'([a-z]|\d)([A-Z])')
    sub=re.sub(p,r'\1 \2',hunp_str).lower()
    return sub


def transfromMethod2Context(method):
    line = method.split('@')
    if(len(line)!=5):
        return '','',''
    name=line[-1].strip()
    body=line[-2].strip()
    returnType=line[1].strip()
    paras=line[2].strip()
    className=line[0].strip()
    enc=tokenzierEnc(className)
    inf=tokenzierInf(returnType,paras)
    imp=tokenzierImp(body)
    context=joinContext(enc,inf,imp)
    return context,body,name


    
           


def loadData(path):
    '''读取java生成的数据集的路径
    :param path:
    :return:
    '''
    names=[]
    bodys=[]
    returnType=[]
    paras=[]
    className=[]
    with open(path,'r',encoding='utf-8') as f:
        lines=f.readlines()
        for line in lines:
            line = line.split('@')
            if(len(line)!=5):
                continue
            try:
                names.append(line[-1].strip())
                bodys.append(line[-2].strip())
                returnType.append(line[1].strip())
                paras.append(line[2].strip())
                className.append(line[0].strip())
            except:
                continue
    return names,bodys,returnType,paras,className

def generateContext(bodys,returnTypes,paras,classNames):
    '''
    生成方法的上下文
    :param bodys: 方法列表
    :param returnTypes: 返回值列表
    :param paras: 参数列表
    :param classNames: 类名列表
    :return:
    '''
    contexts=[]
    for i in range(len(bodys)):
        body=bodys[i]
        returnType=returnTypes[i]
        para=paras[i]
        className=classNames[i]
        enc=tokenzierEnc(className)
        inf=tokenzierInf(returnType,para)
        imp=tokenzierImp(body)
        context=joinContext(enc,inf,imp)
        contexts.append(context)
    return contexts


'''
enc:class name
inf:return type and parameters
imp:method body
'''
def joinContext(enc,inf,imp):
    return enc+' '+inf+' '+imp


def tokenzierEnc(enc):
    return hump2underline(enc)

def tokenzierInf(returnType,paraList):
    returnType=hump2underline(returnType)
    paraList=hump2underline(paraList)
    return returnType+' '+paraList

def tokenzierImp(imp):
    tokens = jl.tokenizer.tokenize(imp)
    lst=[]
    try:
        for token in tokens:
            typeName=token.__class__.__name__
            valueName=token.value
            if typeName=='Identifier':
                # lst.append(typeName)
                lst.append(valueName)
        return ' '.join(map(hump2underline,lst))
    except:
        return ' '
