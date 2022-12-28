with open('./predict.txt','r') as f:
    predictList=f.readlines()

with open('./label.txt','r') as f:
    labelList=f.readlines()

length=len(predictList)
cnt=0
for idx in range(length):
    label=labelList[idx].strip()
    predict=predictList[idx].strip()
    # if label.startswith('set') or label.startswith('get') or label.startswith('is'):
    #     print('{} | {}'.format(label,predict))
    if label==predict:
        cnt+=1
print('sucess rate:{}'.format(cnt*1.0/length))

