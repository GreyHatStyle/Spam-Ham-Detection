from flask import Flask, render_template,request, jsonify
import joblib
import os


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
    from custom_class import KerasClassifier, TextPreprocessor
    app.run(debug=True)