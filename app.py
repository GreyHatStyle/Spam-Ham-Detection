from flask import Flask, render_template,request, jsonify
import joblib
import os
import pickle
from pipe_classes import TextPreprocessor, KerasClassifier


class CustomUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if name == 'TextPreprocessor':
            from pipe_classes import TextPreprocessor
            return TextPreprocessor
        return super().find_class(module, name)
    
class CustomUnpickler2(pickle.Unpickler):
    def find_class(self, module, name):
        if name == 'KerasClassifier':
            from pipe_classes import KerasClassifier
            return KerasClassifier
        return super().find_class(module, name)


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

        with open(os.path.join(os.path.dirname(__file__), 'Models', 'Preprocessing.joblib'), 'rb') as f:
            preprocess = CustomUnpickler(f).load()

        # preprocess = joblib.load(os.path.join(os.path.dirname(__file__), 'Models', 'Preprocessing.joblib'))
        # model = joblib.load(os.path.join(os.path.dirname(__file__), 'Models', 'spam-ham-pipe.joblib'))

        with open(os.path.join(os.path.dirname(__file__), 'Models', 'spam-ham-pipe.joblib'), 'rb') as f:
            model = CustomUnpickler2(f).load()

        ans = model.predict(preprocess.transform([text]))

        ans = ans[0]

    else:
        ans=""

    # return render_template("index.html", answer=ans)
    return jsonify({'answer': ans}) 

if __name__ == "__main__":
    
    
    app.run(debug=True)