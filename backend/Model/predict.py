import joblib
import pandas as pd

# import the ml model
with open('Model/model.pk1', 'rb') as f:
    model = joblib.load(f)
    
model_version = '1.0.0'

def predict_output(user_input: dict):
    input_df = pd.DataFrame([user_input])

    probabilities = model.predict_proba(input_df)[0]
    predicted_index = probabilities.argmax()

    prediction = model.classes_[predicted_index]
    confidence = round(probabilities[predicted_index] * 100, 2)

    return prediction, confidence
