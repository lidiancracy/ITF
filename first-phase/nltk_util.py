import nltk


def wordTagging(text):
    text_list = nltk.word_tokenize(text)
    return nltk.pos_tag(text_list)

def getNoun(pos_tag_list):
    lst=[]
    for item in pos_tag_list:
        typz=item[1]
        if typz.startswith('NN'):
            lst.append(item[0])
    return lst

def getAdj(pos_tag_list):
    lst=[]
    for item in pos_tag_list:
        typz=item[1]
        if typz.startswith('JJ'):
            lst.append(typz)
    return lst
    

def countMaxWord(lst):
    dic={}
    for word in lst:
        if word not in dic:
            dic[word]=1
        else:
            dic[word]+=1
    items=dic.items()
    items=sorted(items,key=lambda x:x[1],reverse=True)
    return items

def countFreRecomm(s):
    dic={}
    s=s.split(' ')
    for w in s:
        if w not in dic:
            dic[w]=1
        else:
            dic[w]+=1
    items=dic.items()
    items=sorted(items,key=lambda x:x[1],reverse=True)
    return items[0][0]
    
    





