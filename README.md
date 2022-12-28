# Method-Name-Generation
You can get the data set used in the paper at the following links.
- new kui dataset
https://www.aliyundrive.com/s/KdzieHyG9xt
- new-100 dataset
https://www.aliyundrive.com/s/Q5RHCdZBWL8
- new-400 dataset
https://www.aliyundrive.com/s/5jM7pKdRamP
- dataset used by RQ5
https://www.aliyundrive.com/s/F1Eve9P8Me3

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
