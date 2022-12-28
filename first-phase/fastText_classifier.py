import fasttext


def load_classifier(path='../fastTextModel/liu_0.82.bin'):
    classifier = fasttext.load_model(path)
    return classifier

def fastText_classification(classifier,context):
    predictLabel=classifier.predict(context)[0][0]
    predictLabel.replace('__label__','')
    return predictLabel
