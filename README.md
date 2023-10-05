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



### Run the ITF Framework

#### 1. Using the First-Step Framework to Recommend Method Names

The `first-phase.sh` script is designed to initialize the recommendation process, ensuring that the required resources and configurations are properly set for the subsequent stages of recommendation.

~~~
first-phase.sh
~~~

#### 2. Using the Second-Step Framework to Recommend Method Names

Welcome to the second phase of the ITF framework, focusing on refining the recommendations based on the results of the first phase and diving deeper into the method naming recommendations.

##### Prerequisites

- **Python Version**: Ensure you have `python3` installed.
- **TensorFlow**: Version 1.12 ([Installation Link](install))
  - To verify your TensorFlow version: `python3 -c 'import tensorflow as tf; print(tf.__version__)'`
- **Java Dataset**: This process requires `JDK` for Java code parsing and dataset creation.
- **Rouge Score Calculation**: Install the necessary module via `pip install rouge`.

##### Step 0: Set Up the Environment

Begin by cloning the repository which contains all the necessary scripts and configuration files:

```bash
git clone (https://github.com/lidiancracy/ITF.git)
cd second-phase
```

##### Step 1: Data Preparation

For this step, you can use the existing dataset or create a new one:

1. **Create and Preprocess a New Dataset**: 
    - The `preprocess.sh` script is responsible for processing Java source files, extracting methods and converting them into a structured format suitable for model training and evaluation.
    - Edit the `preprocess.sh` file as per the provided instructions.
    - Execute the script:

    ```bash
    bash preprocess.sh
    ```

##### Step 2: Model Training

For this step, the focus is on model training:

1. **Train a Model from Scratch**: 
    - The `train.sh` script manages the model training process, utilizing the dataset prepared in the previous step.
    - Edit the `train.sh` file to point it to the right preprocessed data.
    - Adjust the configuration parameters in `config.py` if necessary.
    - Begin the training:

    ```bash
    bash train.sh
    ```

##### Step 3: Model Evaluation

Once the model is trained, evaluate its performance:

- Using the `code2seq.py` script, load the trained model and evaluate it on the test dataset. This step provides insights into the model's accuracy and other performance metrics.

```bash
python3 code2seq.py --load [hidden_model_path]/model.release --test [hidden_data_path]
```

##### Step 4: Model Examination

For a hands-on look into the model's predictions:

- The `code2seq.py` with `--predict` flag allows manual input, letting you understand and observe the model's predictions and, if configured, attention scores.

```bash
python3 code2seq.py --load [hidden_model_path]/model.release --predict
```







