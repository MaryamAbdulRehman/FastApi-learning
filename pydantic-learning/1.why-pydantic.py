from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

# Patient model
class Patient(BaseModel):
    name: Annotated[
        str,
        Field(
            max_length=50,
            title="Name of the Patient",
            description="Write the name of the Patient which is less than 50 characters",
            examples=["Aliya", "Amira"]
        )
    ]

    age: int = Field(gt=0, lt=120)
    email: EmailStr
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: bool
    linkedin_url: AnyUrl
    allergies: Annotated[
        Optional[List[str]],
        Field(max_length=5, title="Dust Allergy")
    ] = None

    contact_details: Dict[str, str]


# Raw input data
patient_info = {
    "name": "Maryam",
    "age": 88,
    "weight": 70.5,
    "married": "True",
    "email": "maryam11@gmail.com",
    "linkedin_url": "http://linkedin.com",
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