import joblib
import pickle
import tensorflow as tf
import tensorflow_text as text  # Registers the ops.
from tensorflow import keras
import nltk

nltk.download("punkt")
nltk.download("stopwords")
nltk.download('wordnet')

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
import re

stop_words = stopwords.words('english')


def get_prepared_data(text, rm_stop_words=True, stemming=True, lemmatisation=True):
    # Create an empty DataFrame which will hold our data set.
    words = text
    words = re.sub('(?:\s)http[^, ]*|\d', '', words)
    words = words.split(" ")

    # Clean the data remove: (numbers, special characters) and make words in lower case.
    cleaned_words = [''.join(ch for ch in word if ch.isalnum()).lower() for word in words if re.match("\w", word)]

    # Remove stopwords if needed
    if rm_stop_words:
        cleaned_words = [word for word in cleaned_words if word not in stop_words]

    # Do stemming if needed
    if stemming:
        ps = PorterStemmer()
        cleaned_words = [ps.stem(word) for word in cleaned_words]

    # Do lemmatisation if needed
    if lemmatisation:
        lem = WordNetLemmatizer()
        cleaned_words = [lem.lemmatize(word) for word in cleaned_words]
    return cleaned_words


with open("models/tfidf.pickle", 'rb') as pickle_file:
    tr = pickle.load(pickle_file)
def get_text_ready(text):
    cleaned_text = get_prepared_data(text)
    cleaned_text = " ".join(cleaned_text)
    transformed_text = tr.transform([cleaned_text])
    return transformed_text


lr = joblib.load("models/LR_model.sav")
def LR(text):
    new_text = get_text_ready(text)
    return lr.predict(new_text)[0]


dt = joblib.load("models/DecisionTreeClassifier_Model.sav")
def DT(text):
    new_text = get_text_ready(text)
    return dt.predict(new_text)[0]


# tf.saved_model.LoadOptions(experimental_io_device="/job:localhost")
# model = keras.models.load_model("models")
# def bert(text):
#     return model.pridect(text)
