# Ya import karna laazmi ha
from pydantic import BaseModel
# =============Step1
# Ya pydantic class ha iss ma BaseModel agar hoa tab hii ya Pydantic Model banay ga otherwise nahi.
# Aur ab apna ideal schema design kiya
class Patient(BaseModel):
    name:str
    age:int
# ============= Step 2
# Object banany k liye dictionary banaii.
# Aur ab iss raw dictionary kii help sa hum apny pydantic object ko instantiate karain gy
patient_info={'name':"Maryam",'age':88}
# Yahan ** means dictionary ko unpack kiya
patient1=Patient(**patient_info)
# ============== Step 3
# Pydantic object ko apna kaam karny k liye patient object mil ra ha jo function k paas bhaj dena ha
def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('inserted')
# Ab chahay jitny bhi functions banaa lain rules start ma define ho chuky hain
def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('updated')
update_patient_data(patient1)

insert_patient_data(patient1)
