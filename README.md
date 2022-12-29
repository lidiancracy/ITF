# Method-Name-Generation
You can get the data set used in the paper at the following links.
- new kui dataset
https://www.aliyundrive.com/s/KdzieHyG9xt
- new-100 dataset
https://pan.baidu.com/s/1RAMoEJUrtxZcpz3fJYmSsw?pwd=0nqx
- new-400 dataset
https://www.aliyundrive.com/s/5jM7pKdRamP
- dataset used by RQ5
https://pan.baidu.com/s/1WFEsFF9Fd5WJGinJ_5pcog?pwd=d9tg

- You can view the fasttext classifier and heuristic rules under the first-phase folder.

### run the ITF
you need to train the bi_lstm first.
~~~
sh run_itf.sh
~~~

- we have trained some models,you can download from this link. https://www.aliyundrive.com/s/F8uY217NQpe

Then, use generated model to predict method names.
~~~
sh infer_itf.sh
~~~
