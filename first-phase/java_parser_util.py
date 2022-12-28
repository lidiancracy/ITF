import javalang as jl


def tokenzierImp(imp):
    tokens = jl.tokenizer.tokenize(imp)
    lst=[]
    try:
        for token in tokens:
            typeName=token.__class__.__name__
            valueName=token.value
            lst.append(valueName)
        return lst
    except:
        return []
    
def tokenzierImpIdentifier(imp):
    tokens = jl.tokenizer.tokenize(imp)
    lst=[]
    try:
        for token in tokens:
            typeName=token.__class__.__name__
            valueName=token.value
            if typeName=='Identifier':
                # lst.append(typeName)
                lst.append(valueName)
        return lst
    except:
        return []

