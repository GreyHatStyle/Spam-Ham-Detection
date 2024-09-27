# Spam Ham Detection
This project is developed to detect whether the SMS your recieved is **Spam** or **Ham** message.

- The model used in project was trained in SMS Spam collection Dataset with 5572 messages.
- Firstly text data was converted into Vectors using [**TfidfVectorizer**](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html), and the following vector was trained in [**Linear Support Vector Machine Classifier**](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html), which gave good results of **98.34%** on Test Dataset.
- For next check, the Text Dataset was converted into Matrix of tokens, using [**Tokenizer**](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text/Tokenizer) library from [**Tensorflow**](https://www.tensorflow.org/).
- Then the concept of [**Convolutional Neural Network (CNN)**](https://en.wikipedia.org/wiki/Convolutional_neural_network) which generally used in **Image** Dataset, was used to train the **Text** dataset in hope of getting different results.
- Surprisingly using **CNN** concept with 1 Dimensional Convolutional Layers gave accuracy of **97.23%** of Test Dataset.
- Then using concept of **Pipelining**, two instances for Text preprocessing and for Prediction was created, which were later used in backend of website.

## Features
