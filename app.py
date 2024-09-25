from flask import Flask, render_template,request, jsonify
import joblib
import os
from sklearn.base import TransformerMixin, BaseEstimator, ClassifierMixin
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

from sklearn.base import TransformerMixin, BaseEstimator, ClassifierMixin
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import sys
import re
from gunicorn.app.wsgiapp import run





app = Flask(__name__)

@app.route("/") # Site end
def hello():

    return render_template("index.html")


@app.route("/predict", methods=['POST', 'GET'])
def predict():
   
    data = request.get_json()
    text = data.get('inputText')
    
    if text != None:
        print(os.path.join(os.path.dirname(__file__), 'Models', 'Preprocessing.joblib'))
        preprocess = joblib.load(os.path.join(os.path.dirname(__file__), 'Models', 'Preprocessing.joblib'))
        model = joblib.load(os.path.join(os.path.dirname(__file__), 'Models', 'spam-ham-pipe.joblib'))

        ans = model.predict(preprocess.transform([text]))

        ans = ans[0]

    else:
        ans=""

    # return render_template("index.html", answer=ans)
    return jsonify({'answer': ans}) 

if __name__ == "__main__":
    class TextPreprocessor(BaseEstimator, TransformerMixin):
        def __init__(self, max_vocab_size=20000, max_len=None):
            self.max_vocab_size = max_vocab_size
            self.max_len = None
            self.tokenizer = Tokenizer(num_words=self.max_vocab_size)
        
        def fit(self, X, y=None):
            print("Text: ", X)
            self.tokenizer.fit_on_texts(X)
            self.word_index = self.tokenizer.word_index
            self.max_len = len(self.word_index)
            self.vocab_size = len(self.word_index)
            if self.max_len is None:
                self.max_len = max(len(seq) for seq in self.tokenizer.texts_to_sequences(X))
            return self
        
        def transform(self, X, y=None):
            print("Inside tranform function")
            seqs = self.tokenizer.texts_to_sequences(X)
            X_padded = pad_sequences(seqs, maxlen=self.max_len)
            print("X_padded: ", X_padded)
            return X_padded



    class KerasClassifier(BaseEstimator, ClassifierMixin):
        def __init__(self, model):
            self.model = model
        
        def fit(self, X, y):
            print("Inside Keras Clasifier fit")
            # Next time I will do training of model here
            return self 

        def label(self, predictions):
            # ans = ["Spam" if pred_i[0]==1 else "Ham" for pred_i in predictions]
            ans = []
            print("Inside label")
            for pred_i in predictions:
                print(pred_i)
                if pred_i == 1:
                    ans.append("Spam")
                else:
                    ans.append("Ham")
                    
            return ans
        
        def predict(self, X):
            print(X)
            predictions = self.model.predict(X)
            pred = (predictions >= 0.5).astype(int)
            print("Predictions: ", predictions)
            return self.label(pred)
    
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(run())