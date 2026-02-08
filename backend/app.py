from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.pydantic_model import UserInput
from Model.predict import model, model_version, predict_output
    
app = FastAPI()

@app.get('/')
def home():
    return {'message':'Insurance premium prediction'}

@app.get('/health')
def health_check():
    return {
        'status':'OK',
        'version':model_version,
        'model_loaded':model is not None
    }
        
@app.post('/predict')
def predict_premium(data: UserInput):

    user_input = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }

    try:
        prediction, confidence = predict_output(user_input)
        
        return JSONResponse(
        status_code=200,
        content={
            "predicted_category": prediction,
            "confidence": confidence
        })
        
    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))