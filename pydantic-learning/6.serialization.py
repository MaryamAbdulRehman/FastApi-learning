# Iss ma hum dekhain gy k kesay hum apnay pydantic model objects ko as a dictionary aur as a json format ma export kar sakty hain


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

# Ya existing pydantic model object ko aik python dictionary ma convert kar dega
temp=patient1.model_dump(include=['name','gender','address']) #Aur yahan hum ya bhi control kar sakty hain k humy kon konse fields ko export karna aur include parameter ko use karna aur list ma field paas kar denii ha


# =========Agar yahan kaafi fields ma sa selected fields export nahii kaenii like address 

# temp=patient1.model_dump(exclude=['address'])  ya code hoga phr



print(temp)
print(type(temp))  #iss kii type dict ho gaee yaani pydantic model object dictionary ma convert ho gaya

temp2=patient1.model_dump_json()
print(temp2)
print(type(temp2))  #Python iss ko as string recieve karay ga aur Agar iss ko export karna chahain model ko to ya proper json format ma export ho jaaye ga




# ========exclude_unset(True)
# Iss ka matlab ha object banaaty howy jo cheezain set nahii kii gaee wo export naee hongee like agar gender set ni kiya to error ni aye ga aur na hii wo show hoga

# ======Code ya ha
# temp=patient1.model_dump(exclude_unset(True))
