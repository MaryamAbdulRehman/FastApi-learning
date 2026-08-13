from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal,Optional
import json

# Create FastAPI application
app = FastAPI()


# -----------------------------
# Patient Data Model
# -----------------------------
class Patient(BaseModel):
    id: Annotated[str, Field(..., description="Id of the patient", examples=["P001"])]
    name: Annotated[str, Field(..., description="Name of the Patient")]
    city: Annotated[str, Field(..., description="Name of the City")]
    age: Annotated[int, Field(..., gt=0, lt=120, description="Age of the Patient")]
    gender: Annotated[
        Literal["Male", "Female", "other"],
        Field(..., description="Gender of the Patient")
    ]
    height: Annotated[float, Field(..., gt=0, description="Height of the patient in meters")]
    weight: Annotated[float, Field(..., gt=0, description="Weight of the Patient in kgs")]

    # Calculate BMI automatically
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height ** 2), 2)
        return bmi

    # Return health verdict based on BMI
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "underweight"
        elif self.bmi < 25:
            return "normal"
        elif self.bmi < 30:
            return "Over weight"
        else:
            return "obese"

class PatientUpdate(BaseModel):
    name:Annotated[Optional[str] ,Field(default=None)]
    city:Annotated[Optional[str],Field(default=None)]
    age:Annotated[Optional[int],Field(default=None,gt=0)]
    gender:Annotated[Optional[Literal['Male','Female','other']],Field(default=None)]
    height:Annotated[Optional[float],Field(default=None,gt=0)]
    weight:Annotated[Optional[float],Field(default=None,gt=0)]


# -----------------------------
# Utility Functions
# -----------------------------

# Load patient data from the JSON file
def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data


# Save updated patient data to the JSON file
def save_data(data):
    with open("patients.json", "w") as f:
         json.dump(data, f)


# -----------------------------
# API Endpoints
# -----------------------------

# Root endpoint
@app.get("/")
def hello():
    return {"message": "Patient Management System API"}


# About endpoint
@app.get("/about")
def about():
    return {
        "message": "A Fully Functional API to manage patient records"
    }


# Get all patients
@app.get("/view")
def view():
    return load_data()


# Get a single patient by ID
@app.get("/patient/{patient_id}")
def view_patient(
    patient_id: str = Path(
        ...,
        description="ID of the patient in the database",
        examples=["P001"]
    )
):
    data = load_data()

    # Check whether the patient exists
    if patient_id in data:
        return data[patient_id]

    # Return 404 if the patient is not found
    raise HTTPException(
        status_code=404,
        detail="Patient not found"
    )


# Sort patients using query parameters
@app.get("/sort")
def sort_patients(
    sort_by: str = Query(
        ...,
        description="Sort on the basis of height, weight or bmi"
    ),
    order: str = Query(
        "asc",
        description="Sort in ascending or descending order"
    )
):

    # Allowed fields for sorting
    valid_fields = ["height", "weight", "bmi"]

    # Validate the sorting field
    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid field. Select from {valid_fields}"
        )

    # Validate the sorting order
    if order not in ["asc", "desc"]:
        raise HTTPException(
            status_code=400,
            detail="Invalid order. Select either asc or desc."
        )

    # Load patient records
    data = load_data()

    # Determine sorting direction
    sort_order = order == "desc"

    # Sort patient records
    sorted_data = sorted(
        data.values(),
        key=lambda x: x.get(sort_by, 0),
        reverse=sort_order
    )

    return sorted_data


# Create a new patient
@app.post("/create")
def create_patient(patient: Patient):

    # Load existing patient records
    data = load_data()

    # Check if the patient ID already exists
    if patient.id in data:
        raise HTTPException(
            status_code=400,
            detail="Patient Already Exists"
        )

    # Add the new patient (excluding the ID from stored data)
    data[patient.id] = patient.model_dump(exclude=["id"])

    # Save updated data to the JSON file
    save_data(data)

    # Return success response
    return JSONResponse(
        status_code=201,
        content={"message": "Patient Created Successfully"}
    )

    # update Patient
@app.put('/edit/{patient_id}')
def update_patient(patient_id:str,patient_update:PatientUpdate):
    # Load Existing Data
    data=load_data()
    # Check if patient exists
    if patient_id not in data:
        raise HTTPException(status_code=404,detail='Patient not Found')
    # Get Existing Patient Information
    existing_patient_info=data[patient_id]
    # Convert Pydantic object to Dictionary
    updated_patient_info=patient_update.model_dump(exclude_unset=True)
    # Update only Provided Fields
    for key,value in updated_patient_info.items():
        existing_patient_info[key]=value
    # Add id because the patient model requires it
    existing_patient_info['id']=patient_id
    # Convert Dictionary to patient object
    patient_obj=Patient(**existing_patient_info)
    # Convert back to dictionary
    existing_patient_info=patient_obj.model_dump(exclude={'id'})
    # Save Updated Patient
    data[patient_id]=existing_patient_info
    # Save Database
    save_data(data)
    return{
        'message':'Patient Updated Successfully'
    }

    # Delete Endpoint
@app.delete('/delete/{patient_id}')
def delete_patient(patient_id:str):
        
        # Load data
    data =load_data()

    # Check karain gy k jo patient provide kiya jaa ra wo exist bhi karta ha ya nahiii
    if patient_id not in data:
         
        raise HTTPException(status_code=404,detail='Patient not Found')
        
    # Agar Data ha to..
    del data[patient_id]

    # Save kiya data
    save_data(data)
# Return JSON Response
    return JSONResponse(status_code=200,content={'message':'Patient Deleted'})
# cvv



