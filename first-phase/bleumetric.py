# from nlgeval import compute_metrics
# metrics_dict = compute_metrics(hypothesis='./ldpred.txt',references=['./ldlabel.txt'])
# print(metrics_dict)
pred=[]
with open("./pred.txt","r") as f:
    lines=f.readlines()
    for line in lines:
        pred.append(line)
label=[]
with open("./label.txt","r") as f:
    lines=f.readlines()
    for line in lines:
        label.append(line)
count=0
for i in range(len(label)):
    if(label[i]==pred[i]):
        count=count+1
print(count)
print(len(label))
print(count/len(label))
