from fastapi import FastAPI
# Removed unused imports
import pickle
import uvicorn
from diabetech import Diabetech


app = FastAPI()
pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)

@app.get('/')
def index():
    return {'message': 'Hello, World'}


@app.post('/predict')
def predict_diabetes(data: Diabetech):
    data = data.dict()
    Pregnancies = data['Pregnancies']
    Glucose = data['Glucose']
    BloodPressure = data['BloodPressure']
    SkinThickness = data['SkinThickness']
    Insulin = data['Insulin']
    BMI = data['BMI']
    DiabetesPedigreeFunction = data['DiabetesPedigreeFunction']
    Age = data['Age']

    prediction = classifier.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    if prediction[0] == 1:
        prediction = 'Diabetes'
    else:
        prediction = 'No Diabetes'
    return {
        'prediction': prediction
    } 

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
        
        
# Run the code in the terminal
# uvicorn DiabeTech:app --reload