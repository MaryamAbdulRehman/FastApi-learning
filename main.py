# fast api k andar FastApi import karwaayen gy
from fastapi import FastAPI
# app object banaatay hain jo FastApi ka object hota ha
app=FastAPI()

"""# endpoint k liye route define karna parray ga
hum server pa data da kar dekhna chahty hain iss liye get requestiss k baad
decorator kii help sa route define karna ha yahan aur route hoga slash / ab path define kar liya ha"""

@app.get("/")

# ab iss end point k liye method/function banaayen gy.function name hello ha aur iss ko kisi input
# kii zaroorat naee ha.aur ya wapis dictionary return karay gii jismy message hello world likha hoga
# ya humari first API ha

def hello():
    return {'message':'hello world'}


""" Ab file ko run karny k liye ya command ha
 uvicorn file name(main) : object name (app) phr space daal kar --reload
Jasy hii ya command run karain gy behind the scenes uvicorn server start ho jaaye ga
aur wo http pa request sunny lag jaaye ga"""


@app.get("/about")
def about():
    return {"message":"I am maryam"}


'''
So This is how we create different different endpoints.Hum alag alag routes define karty hain
har route ma function banaaty hain aur uss function ma apna logic likhty hain

Ab agar hum apni API jo bnaaai iss pa slash/ laga k docs likh k eneter maarain gy to auto 
generated documentation dekhaai dega
Hum 2no endpoints pa jaa kar try it out kar sakty hain
'''