# my_app/ml_model.py
# import tensorflow as tf
import os
from django.conf import settings

MODEL_PATH = os.path.join(settings.BASE_DIR, 'patients', 'models', 'lstm_heart_model.h5')


model = None

def load_model():
    global model
    if model is None:
        model = tf.keras.models.load_model(MODEL_PATH)
    return model

def predict(input_data):
    mdl = load_model()
    
    prediction = mdl.predict(input_data)
    return prediction
