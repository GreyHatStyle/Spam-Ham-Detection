# Spam Ham Detection
This project is developed to detect whether the SMS your recieved is **Spam** or **Ham** message.

## Table of Contents
1. [Model Implementation](#model-implementation)
2. [Run Locally](#run-locally)
3. [How to Use?](#how-to-use)
    - [Sample Inputs](#sample-inputs)
    - [Responsiveness](#responsiveness)
5. [Developed By](#developed-by)



## Model Implementation
- The model used in project was trained in SMS Spam collection Dataset with 5572 messages.
- Firstly text data was converted into Vectors using [**TfidfVectorizer**](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html), and the following vector was trained in [**Linear Support Vector Machine Classifier**](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html), which gave good results of **98.34%** on Test Dataset.
- For next check, the Text Dataset was converted into Matrix of tokens, using [**Tokenizer**](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text/Tokenizer) library from [**Tensorflow**](https://www.tensorflow.org/).
- Then the concept of [**Convolutional Neural Network (CNN)**](https://en.wikipedia.org/wiki/Convolutional_neural_network) which generally used in **Image** Dataset, was used to train the **Text** dataset in hope of getting different results.
- Surprisingly using **CNN** concept with 1 Dimensional Convolutional Layers gave accuracy of **97.23%** of Test Dataset.
- Then using concept of **Pipelining**, two instances for Text preprocessing and for Prediction was created, which were later used in backend of website.
- The Front of Website was developed using **HTML**, **CSS** and **Javascript** with the help for **Flask** for connection.

## Run Locally
To setup this project in your local enviornment follow the below steps (*Its recommended to do these following steps in a virtual enviornment*).
\
If you **don't** want to setup virtual envoirnment, then skip 2nd and 4th step.
1. Clone the Repo in your local directory
```
git clone https://github.com/GreyHatStyle/Spam-Ham-Detection.git
```
2. Create Virtual Enviornment
```
python -m venv Spam-Ham-Detection
```
3. Move to Project Directory
```
cd Spam-Ham-Detection
```
4. Activate Virtual Enviornment
```
Scripts\activate
```
5. Install Dependencies
```
  pip install -r requirements.txt
```
6. Start the Project
```
python app.py
```

## How to Use?
The website is simple to use, just enter the SMS text in the input field and press `Validate` button.
\
The text data (input) will be sent to python envoirnment (for predictions) using **Javascript** in form of [**JSON**](https://en.wikipedia.org/wiki/JSON) format
\
\
![image](https://github.com/user-attachments/assets/14452b99-d54e-4e04-8ae5-bdd043bbdd2a)



### Sample inputs
- Congratulations!! you won a free lottery with 2000 dollars!!
- Hi, there I am manas bisht.
- Free!! Free!! you have won Iphone 16 pro max congratulations!!!
- Your attendance is 65% short, kindly maintain else, department will inform your parents.

\
And many more...

### Responsiveness
1. Iphone SE
\
![image](https://github.com/user-attachments/assets/23ad1dab-292c-4754-b21f-47b05eecbb5e)



3. Samsung Galaxy S20 Ultra
\
![image](https://github.com/user-attachments/assets/e113688e-6a8a-421f-a2da-37552049f2ea)


## Developed By
- [@manas_bisht](https://github.com/GreyHatStyle): The Backend Prediction part.
- [@daksh_purohit](https://github.com/EzioAuditore12): The Frontend Web development part.
