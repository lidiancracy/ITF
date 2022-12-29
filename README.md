# Method-Name-Generation
You can get the data set used in the paper at the following links.
- new kui dataset
https://pan.baidu.com/s/1wQH66aUMhCsaRb7w3UYkGA?pwd=dx1t
- new-100 dataset
https://pan.baidu.com/s/1RAMoEJUrtxZcpz3fJYmSsw?pwd=0nqx
- new-400 dataset
https://pan.baidu.com/s/12tHY3a1tlw8AoSIQl5_Rmw?pwd=ee8i
- dataset used by RQ5
https://pan.baidu.com/s/1WFEsFF9Fd5WJGinJ_5pcog?pwd=d9tg


### run the ITF

~~~
You can view the fasttext classifier and heuristic rules under the first-phase folder.
~~~

you need to train the bi_lstm first.
~~~
sh run_itf.sh
~~~

Then, use generated model to predict method names.
~~~
sh infer_itf.sh
~~~

~~~
- we have trained some models,you can download from this link. 
- https://pan.baidu.com/s/1o53cQ8wwCziQNmekhu-bBQ?pwd=u2ak
~~~
