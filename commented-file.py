
"""
1. fast api k andar FastApi import karwaayen gy

2. The Path() function in FastAPI is used to provide metadata, validation rules,
and documentation hints for path parameters in your API endpoints.
Title
Description
Example
ge, gt, le, lt(greater then equal to ,greater then,less than equal to, less than)(yaani ya validation add kar sakty hain asy)
Min_length
Max_length
regex

3. Ab hum ya karain gy k agar client yaani jo id naa milii to hum status code generate karain gy 404
 aur iss k custom exception class chahiye jisko hum HttpException likhain gy

HTTPException is a special built-in exception in FastAPI used to return custom HTTP error responses
when something goes wrong in your API.Instead of returning a normal JSON or crashing the server,
 you can gracefully raise an error with:
 a proper HTTP status code (like 404, 400, 403, etc.)
 a custom error message
 (optional) extra headers

"""
from fastapi import FastAPI ,Path,HTTPException,Query
# json file ko read karny k liye json model kii zarorat parray gii
import json
# app object banaatay hain jo FastApi ka object hota ha
app=FastAPI()

# helper function
def load_data():
    with open('patients.json','r') as f:
        data =json.load(f)
    return data



'''
Endpoint k liye route define karna parray ga
hum server pa data da kar dekhna chahty hain iss liye get requests k baad decorator kii
 help sa route define karna ha yahan aur route hoga slash / ab path define kar liya ha
'''

@app.get("/")

# ab iss end point k liye method/function banaayen gy.function name hello ha aur iss ko kisi input
# kii zaroorat naee ha.aur ya wapis dictionary return karay gii jismy message hello world likha hoga
# ya humari first API ha

def hello():
    return {'message':'Patient Management System API'}


""" Ab file ko run karny k liye ya command ha
 uvicorn file name(main) : object name (app) phr space daal kar --reload
Jasy hii ya command run karain gy behind the scenes uvicorn server start ho jaaye ga
aur wo http pa request sunny lag jaaye ga


Ab humny project pa kaam start kiya ha aur iss file ko update kar ry hain
"""


@app.get("/about")
def about():
    return {"message":"A fully Functional API to manage to manage your patient records"}


'''
So This is how we create different different endpoints.Hum alag alag routes define karty hain
har route ma function banaaty hain aur uss function ma apna logic likhty hain

Ab agar hum apni API jo bnaaai iss pa slash/ laga k docs likh k eneter maarain gy to auto 
generated documentation dekhaai dega
Hum 2no endpoints pa jaa kar try it out kar sakty hain
'''


# Ab aik endpoint banaana ha jiska naam hoga view aur jasy hii koi iss endpoint ko hit karay ga
# to jitny bhi patients humaary hain unn ka data client ko bhaj dain gy 
# End point banaany sa pehly patients.json ma sa data load karny k liye aik function likhna 
# parray ga because ya kaam humy baar baar karna ha agy bhi jab hum endpoint banaayen gy patients.json
# file ma sa record nikaalny parrain gy...ab upar helper function banaayen gy


# Ya endpoints sab patients ka data cliet ko deta ha

@app.get("/view")
def view():
# jasy hii request atii ha sabsy pehly data fetch kar k laayen gy using load_data function
    data=load_data()
    # phr simply uss data ko as it isreturn kar dain gy
    return data

"""
Ab yahan aik endpoint create karain gy ya code hoga k client/user apni passand ka patient ka data
dekh sakta ha ya URL k through pata chalay ga k ya konsa patient hoga aur ya humy path parameters
k through pata chalay ga

Aur ab banaana start kiya aur yahan patient_Id variable kii tarha define kar diya,kyun k abhi humy
ni pata patient future ma kis patient ka data dekhna chahta ha

Ab view_patient naam sa function banaayen gy aur ab view_patient ko kaam karny k liye aik patient_id 
chahiye to humy opar route ma jo patient_id mil ree ha wohii yahan paas kar dain gy aur saath data
Type bhi specify kar dain gy jo k string ha kyun k json file ma string format ma hain ids.

Ab function ma definition create karna ha function ka logic likhna ha aur function ka logic boht simple
ha like sabsy pehly poora patient ka data load karain gy phir search karain gy k ya particular patient
id exist karta ha ya ni aur agar karta ha to wo data dekhaa dain gy agar ni to bolain gy its an error

Ab hum sab patients ko load karain gy(previous lecture ma humny aik utility function banaaya tha jis sy
data load kar sakty hain )

Yani ya particular patient_id as key humaary data ma exist kartii ha? Agar kartii ha to...

return karay data k andar sa patient_id

Agar nahi ha to error msg return karay patient not found

"""
@app.get('/patient/{patient_id}') 
#jahan par path parameter ko recieve kar ry hoty hain wahin par = path function call kar dety hain
# Aur three dots(...) ka matlab ha ya filed required ha  (aur ya sab karny sa readability improve hoii ha...aur ya first improvement kii humny )
def view_patient(patient_id:str=Path( ..., description='Id of the patient in the DB',example='P001')): 
    # load all the patients
    data=load_data()
    if patient_id in data:
        return data[patient_id]
    # return {'error':'patient not found'}  ya normal json return ho ree ha iss kii bajaayen hum gracefully error raise karain gy
    raise HTTPException(status_code=404,detail='Patient not found')
"""
2nd improvement: Http status code are 3 digit numbers returned by a web server like FastApi
 to indicate the result of a clients requests like from browser or API consumer

 Ab iss ma problem ya ha k patioent ma jaa k  agar hum asee id daalty hain jo present hii ni 
 ha wahaan to humy 200 hii dekha ra means success humy not found dekhaana chhaiye like 404

 Ab hum ya karain gy k agar client yaani jo id naa milii to hum status code generate karain gy 404
 aur iss k custom exception class chahiye jisko hum HttpException likhain gy
"""



"""
Definition Query Parameter
 Query parameters are optional key-value pairs appended to the end of a URL, used to pass
 additional data to the server in an HTTP request. They are typically employed for operations 
 like filtering, sorting, searching, and pagination, without altering the endpoint path itself.
URL Example:
   /patients?city=Delhi&sort_by=ageKey 
Rules:
   The ? marks the start of query parameters.
   Each parameter is a key-value pair: key=value
   Multiple parameters are separated by &
Breakdown of the Example
   In this case:
   city=Delhi is a query parameter for filtering
   sort_by=age is a query parameter for sorting

"""
''' Aik endpoint banaye gy ehich will be able to sort patients 2 query parameters milain gy

1.sort by bataya jaaye ga kis key kii base pa sorting karni ha weight,height,bmi
2.kis order ma sorting karnii ha ascending ya descending

Ya sab query parameter kii help sa hoga'''


#iss function ko apna kaam karny k liye 2 query parameters chahiye aik hoga sort_by aur
# ya hoga aik string iss k opar path parameters kii tarha description examples aur data
# validation add kar sakty hain path parameters ma path() tha aur isi tarha query () ha
# query parameters ma


# Query() is a utility function provided by FastAPI to declare, validate, and document 
# query parameters in your API endpoints.

# It allows you to:
# • Set default values
# • Enforce validation rules
# • Add metadata like description, title, examples

# default                  Set default value (e.g., Query(0))
# title                    Displayed in API docs
# description              Detailed explanation in Swagger
# example / examples       Provide sample inputs
# min_length, max_length   Validate string length
# ge, gt, le, lt           Validate numeric bounds
# regex                    Pattern match for strings


@app.get('/sort')
def sort_patients(sort_by:str=Query(..., description="Sort on the basis of height ,weight or bmi" ),order:str =Query('asc',description="sort in asc or desc order")):
# Ab aik variable banaayen gy
 valid_fields=['height','weight','bmi']
#   check karain gy k agar sort_by valif field k andar nahii ha to seedha httpException raise ho jaaye gii status code of 400 pa yaani bad request aur f string banaa liya taaky valid_fields ka value print ho jaaye
 if sort_by not in valid_fields:
    raise HTTPException(status_code=400,detail=f'invalid field select from{valid_fields}')
 if order not in ['asc','desc']:
     raise HTTPException(status_code=400,detail='invalid order select between asc and desc')
#  Ab imagine kiya k sort_by aur order kii value thk aii ha to data ko load karain gy
 data =load_data()

#  agar query parameter ka value descending ha to True otherwise False
 sort_order=True if order=='desc' else False
 sorted_data=sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=sort_order)

 return sorted_data

"""
1. Path Parameters
Path parameters URL ka dynamic hissa hote hain.
In ki madad se hum kisi specific resource ko fetch kar sakte hain.
Ye zyada tar Retrieve (GET), Update (PUT/PATCH) aur Delete (DELETE) operations mein use hote hain.
Path parameters required hote hain, yani in ki value dena zaroori hota hai.

2. Query Parameters
Query parameters tab use hote hain jab hum existing endpoint mein additional features add karna chahtay hain.
Jaise:
Searching
Filtering
Sorting
Pagination
Query parameters aam tor par optional hote hain

"""
# ===========  why-pydantic.py File

# Ya import karna laazmi ha
from pydantic import BaseModel,EmailStr,AnyUrl
from pydantic import Field
# Typing Module sa list ko import kiya
from typing import List
# Typing Module sa dict ko import kiya
from typing import Dict
# Typing Module sa dict ko import kiya
from typing import Optional

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
    @field_validator('age',mode="after")   #Aur default value yaani mode hataa dain to default value after hii hotii ha
         #yahan agar mode before set karain to ya type coercion ni hogii aur age ma error aye ga jis sa age ma jo value ha wo string show hogiii jo k type coercion sa pehly waali value hogii
    @classmethod
    def validate_age(cls,value):
        if 0<value<100:
           return value
        raise('Age should be in between o and 100')
    


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
# Next Step is Field validator

