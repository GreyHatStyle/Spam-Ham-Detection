from flask import Flask, render_template,request, jsonify
import joblib
import os
from model import KerasClassifier, TextPreprocessor
import logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route("/") # Site end
def hello():

    return render_template("index.html")


@app.route("/predict", methods=['POST', 'GET'])
def predict():
   
    data = request.get_json()
    text = data.get('inputText')

    try:
        if text != None:
            print(os.path.join(os.path.dirname(__file__), 'Models', 'Preprocessing.joblib'))
            preprocess = joblib.load(os.path.join(os.path.dirname(__file__), 'Models', 'Preprocessing.joblib'))
            model = joblib.load(os.path.join(os.path.dirname(__file__), 'Models', 'spam-ham-pipe.joblib'))

            ans = model.predict(preprocess.transform([text]))

            ans = ans[0]

        else:
            ans=""
    except:
        ans = f"dir: {os.getcwd}, sys: {sys.path}"
        logging.info(f"Current directory: {os.getcwd()}")
        import sys
        logging.info(f"sys.path: {sys.path}")

    # return render_template("index.html", answer=ans)
    return jsonify({'answer': ans}) 

if __name__ == "__main__":
    
    app.run(debug=True)