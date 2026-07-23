from fastapi import FastAPI, Path, HTTPException, Query
import json

# Create FastAPI app
app = FastAPI()


# Load data from JSON file
def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data


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


# View all patients
@app.get("/view")
def view():
    return load_data()


# View a single patient by ID
@app.get("/patient/{patient_id}")
def view_patient(
    patient_id: str = Path(
        ...,
        description="ID of the patient in the database",
        examples=["P001"]
    )
):
    data = load_data()

    if patient_id in data:
        return data[patient_id]

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

    # Validate sort field
    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid field. Select from {valid_fields}"
        )

    # Validate sorting order
    if order not in ["asc", "desc"]:
        raise HTTPException(
            status_code=400,
            detail="Invalid order. Select either asc or desc."
        )

    # Load patient data
    data = load_data()

    # True for descending, False for ascending
    sort_order = order == "desc"

    # Sort and return data
    sorted_data = sorted(
        data.values(),
        key=lambda x: x.get(sort_by, 0),
        reverse=sort_order
    )

    return sorted_data