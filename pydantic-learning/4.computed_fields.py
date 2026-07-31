from pydantic import BaseModel, EmailStr, AnyUrl, Field,field_validator,computed_field
from typing import List, Dict, Optional, Annotated
class Patient(BaseModel):
    name:str
    age:int
    email:EmailStr
    height:float
    weight:float
    married:bool
    linkedin_url:AnyUrl
    allergies:Optional[List[str]]=None
    contact_details:Dict[str,str]
    @computed_field
    @property
    def bmi(self) ->float:
        calculate_bmi=round(self.weight/(self.height**2),2)
        return calculate_bmi

# Raw input data
patient_info = {
    "name": "Maryam",
    "age": '88',  #yahan age string ma dii ha agar ya opar acess karain to type coercion k baad kii value da ga like mode ='after' sa
    "weight": 70.5, #kg
    'height':1.75, #meter
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

# Update patient data
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('Bmi',patient.bmi)
    print("Updated")

update_patient_data(patient1)

