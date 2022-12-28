from __future__ import print_function

import numpy as np
import pandas as pd
from keras_text_summarization.library.rnn import RecursiveRNN2
from keras_text_summarization.library.seq2seq import Seq2SeqSummarizer


def seq2seqPredictor():
    np.random.seed(42)
    model_dir_path = '../seq2seq_model'
    config = np.load(RecursiveRNN2.get_config_file_path(model_dir_path=model_dir_path),allow_pickle=True).item()
    summarizer =  RecursiveRNN2(config)
    summarizer.load_weights(weight_file_path=RecursiveRNN2.get_weight_file_path(model_dir_path=model_dir_path))
    # return summarizer.summarize(context)
    return summarizer

