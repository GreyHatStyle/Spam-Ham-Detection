from flask import Flask, render_template,request
import joblib


# Pipe Line classes
from sklearn.base import TransformerMixin, BaseEstimator, ClassifierMixin
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

class TextPreprocessor(TransformerMixin):
    def __init__(self, max_vocab_size=20000, max_len=None):
        self.max_vocab_size = max_vocab_size
        self.max_len = max_len
        self.tokenizer = Tokenizer(num_words=self.max_vocab_size)
    
    def fit(self, X, y=None):
        self.tokenizer.fit_on_texts(X)
        self.word_index = self.tokenizer.word_index
        self.vocab_size = len(self.word_index)
        if self.max_len is None:
            self.max_len = max(len(seq) for seq in self.tokenizer.texts_to_sequences(X))
        return self
    
    def transform(self, X, y=None):
        seqs = self.tokenizer.texts_to_sequences(X)
        X_padded = pad_sequences(seqs, maxlen=self.max_len)
        return X_padded

    def fit_transform(self, X, y=None):
        return self.fit(X).transform(X)


class KerasClassifier(BaseEstimator, ClassifierMixin):
    def __init__(self, model):
        self.model = model
    
    def fit(self, X, y):
        # Next time I will do training of model here
        return self
    
    def predict(self, X):
        predictions = self.model.predict(X)
        pred = (predictions>=0.5).astype(int)
        return "Spam" if pred==1 else "Ham" 
    


app = Flask(__name__)



@app.route("/") # Site end
def hello():

    return render_template("index.html")


@app.route("/predict", methods=['POST', 'GET'])
def predict():
    text = request.form.get('inputText')

    if text != None:

        # model = joblib.load('Models\\spam-ham-pipe.pkl')
        model = joblib.load('Models\\spam_ham_model.pkl')

        ans = model.predict([text])
        ans = ans[0]

    else:
        ans=""

    return render_template("index.html", answer=ans)


app.run(debug=True)