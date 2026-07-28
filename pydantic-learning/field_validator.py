from pydantic import BaseModel, EmailStr, AnyUrl, Field,field_validator
from typing import List, Dict, Optional, Annotated

# Patient model
class Patient(BaseModel):
    name: str
    age: int 
    email: EmailStr
    weight: float
    married: bool
    linkedin_url: AnyUrl
    allergies: List[str]
    contact_details: Dict[str, str]
    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains=['hdfc.com','icici.com']
        # abc@gmail.com
        domain_name=value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value
    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()
    @field_validator('age')
    @classmethod
    def validate_age(cls,value):
        if 0<value<100:
            return value
        raise('Age should be in between o and 100')

# Raw input data
patient_info = {
    "name": "Maryam",
    "age": 88,
    "weight": 70.5,
    "married": "True",
    "email": "maryam11@hdfc.com",
    "linkedin_url": "http://linkedin.com",
    'allergies':['pollen','dust'],
    "contact_details": {
        "email": "maryam@gmail.com",
        "phone": "03132345654"
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