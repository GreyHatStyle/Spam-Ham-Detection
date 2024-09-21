from flask import Flask, render_template,request
import joblib
from sklearn.feature_extraction.text import TfidfTransformer

app = Flask(__name__)

# Static is public 
# Templates are private

@app.route("/") # Site end
def hello():

    return render_template("index.html")


@app.route("/predict", methods=['POST', 'GET'])
def predict():
    text = request.form.get('inputText')

    if text != None:

        model = joblib.load('Models\\spam_ham_model.pkl')

        ans = model.predict([text])

        ans = ans[0]

    else:
        ans=""

    return render_template("index.html", answer=ans)


app.run(debug=True)