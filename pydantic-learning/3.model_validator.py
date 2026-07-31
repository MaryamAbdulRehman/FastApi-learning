from pydantic import BaseModel, EmailStr, AnyUrl, Field,field_validator,model_validator
from typing import List, Dict, Optional, Annotated
# patient Model
class Patient(BaseModel):
    name: str
    age: int 
    email: EmailStr
    weight: float
    married: bool
    linkedin_url: AnyUrl
    allergies: List[str]
    contact_details: Dict[str, str]
    # decorator
    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age>60 and 'emergency' not in model.contact_details:
            raise ValueError('Patient older than 60 must have an emergency contact')
        return model
# Raw input data
patient_info = {
    "name": "Maryam",
    "age": '88',  #yahan age string ma dii ha agar ya opar acess karain to type coercion k baad kii value da ga like mode ='after' sa
    "weight": 70.5,
    "married": "True",
    "email": "maryam11@hdfc.com",
    "linkedin_url": "http://linkedin.com",
    'allergies':['pollen','dust'],
    "contact_details": {
        "email": "maryam@gmail.com",
        "phone": "03132345654",
        'emergency':'1122'
    }
}

# Create Pydantic object
patient1 = Patient(**patient_info)


# Insert patient data
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print("Inserted")


# Update patient data
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Updated")


update_patient_data(patient1)
insert_patient_data(patient1)


