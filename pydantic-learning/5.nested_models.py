from pydantic import field_validator
from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pin:str

class Patient(BaseModel):
    name:str
    gender:str
    age:int
    address:Address

address_dict={
    'city':'Beiging',
    'state':'China',
    'pin':'166200'
}
address1=Address(**address_dict)

patient_dict={
    'name':'Taana',
    'gender':'Male',
    'age':79,
    'address':address1

}
patient1=Patient(**patient_dict)
print(patient1)
print(patient1.name)
print(patient1.address)
print(patient1.address.pin)






