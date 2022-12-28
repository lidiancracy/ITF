import random

import pandas as pd

with open('../used_data/double-5-predict.txt','r') as f:
    predicts=f.readlines()
with open('../used_data/double-5-result.txt','r') as f:
    results=f.readlines()

indexs=list(range(len(predicts)))

choices=random.sample(indexs,100)

print(choices)

choice_predict=[ predicts[idx].strip() for idx in choices]
choice_results=[ results[idx].strip() for idx in choices]

data={'predict':choice_predict,'result':choice_results}
df=pd.DataFrame(data)
df.to_csv('./random_100_03.csv')






