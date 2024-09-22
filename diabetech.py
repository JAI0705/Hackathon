from pydantic import BaseModel

class Diabetech(BaseModel):
    Pregnancies	: int
    Glucose	: int
    BloodPressure	: int
    SkinThickness	: int
    Insulin	: int
    BMI	: float
    DiabetesPedigreeFunction	: float
    Age	: int
    
    