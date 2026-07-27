# Ya import karna laazmi ha
from pydantic import BaseModel,EmailStr,AnyUrl
from pydantic import Field
# Typing Module sa list ko import kiya
from typing import List
# Typing Module sa dict ko import kiya
from typing import Dict
# Typing Module sa dict ko import kiya
from typing import Optional,Annotated

# =============Step1
# Ya pydantic class ha iss ma BaseModel agar hoa tab hii ya Pydantic Model banay ga otherwise nahi.
# Aur ab apna ideal schema design kiya
class Patient(BaseModel):
    name:str=Field(max_length=50)
    age:int =Field(gt=0 ,lt=120) #age pa range define kii humny
    email:EmailStr
    weight:float=Field(gt=0)   #ya constraint lagaya k koi bhi weight 0 sa kam set ni kar sakta
    married:bool
    linkedin_url:AnyUrl
    allergies:Optional[List[str]]=None #Yahan ab agar hum koi field add ni karty to yahan None dekhaaye ga
    allergies:Optional[List[str]]=Field(max_length=5)


      #Humny idhar akela List iss liye ni likha kyun k humny list k saath ya bhi validate karna tha k list k andar jo values hongee wo string type kii hongee 
    contact_details:Dict[str,str] # Isii tarha Humny idhar akela Dict iss liye ni likha kyun k humny Dictionary k saath ya bhi validate karna tha k Dictionary k andar jo keys hongee wo bhi string type ma hongee aur jo values hongee wo bhii string type ma
# ============= Step 2
# Object banany k liye dictionary banaii.
# Aur ab iss raw dictionary kii help sa hum apny pydantic object ko instantiate karain gy
patient_info={'name':"Maryam",'age':88,'weight':70.5,"married":"True",'contact_details':{'email':'maryam@gmail.com','phone':'03132345654'},'email':"maryam11@gmail.com","linkedin_url":'http://linkedin.com'}
# Yahan ** means dictionary ko unpack kiya
patient1=Patient(**patient_info)
# ============== Step 3
# Pydantic object ko apna kaam karny k liye patient object mil ra ha jo function k paas bhaj dena ha
def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)

    print('inserted')
# Ab chahay jitny bhi functions banaa lain rules start ma define ho chuky hain
def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('updated')
update_patient_data(patient1)

insert_patient_data(patient1)

# ========Ya humny barra aur complex banaana seekha aur use karna