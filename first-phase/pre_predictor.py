from context_util import hump2underline


def pre_predictor(lst):
    methodName,flag=pre_getter_predictor(lst)
    if flag:
        return methodName,True
    methodName,flag=pre_setter_predictor(lst)
    if flag:
        return methodName,True
    methodName,flag=pre_delegations_predictor(lst)
    if flag:
        return methodName,True
    return 'None',False
    
def pre_getter_predictor(lst):
    template1=['{','return','someword',';','}']
    template2=['{','return','this','.','someword',';','}']
    if 'return' in lst:
        if len(lst)==len(template1):
            for idx in range(len(lst)):
                if template1[idx]!=lst[idx] and idx!=2:
                    return 'None',False
            name='get'+lst[2].capitalize()
            if name.isalpha():
                return name,True
            else:
                return 'None',False
        if len(lst)==len(template2):
            for idx in range(len(lst)):
                if template2[idx]!=lst[idx] and idx!=4:
                    return 'None',False 
            name='get '+lst[4].capitalize()
            if name.isalpha():
                return name,True
            else:
                return 'None',False
    else:
        return 'None',False
    return 'None',False


def pre_setter_predictor(lst):
    template1=['{','someword','=', 'someword', ';','}']
    template2=['{','this','.','someword','=','someword',';','}']
    if '=' in lst:
        if len(lst)==len(template1):
            for idx in range(len(lst)):
                if template1[idx]!=lst[idx]:
                    if idx==1 or idx==3:
                        continue
                    else:
                        return 'None',False
            name='set'+lst[1].capitalize();
            if name.isalpha():
                return name,True;
            else:
                return 'None',False
        if len(lst)==len(template2):
            for idx in range(len(lst)):
                if template2[idx]!=lst[idx]:
                    if idx==3 or idx==5:
                        continue
                    else:
                        return 'None',False
            name='set'+lst[3].capitalize()
            if name.isalpha():
                return name,True
            else:
                return 'None',False
        return 'None',False
    else:
        return 'None',False

def pre_delegations_predictor(lst):
    if lst.count(';')!=1:
        return 'None',False
    template1=['{','methodcall','(', 'someparameter', ')',';','}']
    template2=['{','return','methodcall','(','someparameter',')',';','}']
    if len(lst)<len(template1):
        return 'None',False
    if 'return' in lst:
        for idx in range(4):
            if template2[idx]!=lst[idx]:
                if idx==2:
                    continue
                else:
                    return 'None',False 
        for idx in range(-1,-4,-1):
            if template2[idx]!=lst[idx]:
                return 'None',False
        name=lst[2]
        if name.isalpha():
            return lst[2],True
        else:
            return 'None',False
    else:
        for idx in range(3):
            if template1[idx]!=lst[idx]:
                if idx==1:
                    continue
                else:
                    return 'None',False
        for idx in range(-1,-4,-1):
            if template2[idx]!=lst[idx]:
                return 'None',False
        name=lst[1]
        if name.isalpha():
            return lst[1],True
        else:
            return 'None',False

 
        


        
    
    
    


    


