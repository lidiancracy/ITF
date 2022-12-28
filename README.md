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




- 训练关键字提取器
训练数据是keyword_extraction_data下面的数据集
生成的模型，放在KeywordsExtractor下面
python train_and_eval.py --train_source_file keywords_extraction_data/train/inputs.jsonl.gz --train_target_file keywords_extraction_data/train/summaries.jsonl.gz --valid_source_file keywords_extraction_data/test/inputs.jsonl.gz --valid_target_file keywords_extraction_data/test/summaries.jsonl.gz --node_vocab_file vocabulary/node_5.vocab --edge_vocab_file vocabulary/edge.vocab --target_vocab_file vocabulary/output_5.vocab --train_steps 30000 --lr_decay_rate 0.95 --lr_decay_steps 3000 --classify --model_name KeywordsExtractor --checkpoint_dir KeywordsExtractor --node_features_dropout 0.0 --validation_interval 3000 --embeddings_dropout 0.2 --learning_rate 0.0005 --batch_size 16 --checkpoint_interval 3000 --seed 2020
- 运行关键字提取程序以预测每个代码段的关键字
python train_and_eval.py --node_vocab_file vocabulary/node_5.vocab --edge_vocab_file vocabulary/edge.vocab --target_vocab_file vocabulary/output_5.vocab --classify --model_name KeywordsExtractor --checkpoint_dir KeywordsExtractor --node_features_dropout 0.0 --embeddings_dropout 0.2 --batch_size 16 --seed 2020 --infer_source_file keywords_extraction_data/test/inputs.jsonl.gz --infer_predictions_file keywords_extraction_data/test/infer_keywords.json --infer_target_file keywords_extraction_data/test/summaries.jsonl.gz
