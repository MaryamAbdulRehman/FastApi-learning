# FastApi-learning
FastAPI Project Overview 

Project ka Overview

Is project mein hum FastAPI use karke ek Doctor Patient Management System ki Backend API banayenge.

Yeh project humein sikhayega ke backend APIs kaise banti hain aur frontend un APIs ko kaise use karta hai.

Sab kuch hands-on aur practical hoga. Hum sirf theory nahi parhenge, balki ek real-world project bana kar FastAPI seekhenge.


---

Problem Statement

Agar aap kabhi doctor ke clinic gaye hon, to aap ne dekha hoga ke doctor ek prescription paper deta hai.

Is paper par doctor:

Patient ka naam likhta hai.

Medicines likhta hai.

Apne remarks likhta hai.

Next visit ki date ya instructions likhta hai.


Doctor patient ko kehta hai ke agli visit par ye paper saath lana.

Har visit par naya paper milta rehta hai aur patient ko saare papers ek file mein sambhal kar rakhne padte hain.


---

Is System ki Problems

Ye poora system offline hai.

Is wajah se bohot si problems hoti hain.

Patient Side Problems

Prescription paper gum ho sakta hai.

Purana record dhoondhna mushkil hota hai.

Kai saalon ke records maintain karna difficult hota hai.


Doctor Side Problems

Doctor ke paas bhi patient ki copy hoti hai.

Wo bhi:

Misplace ho sakti hai.

Damage ho sakti hai.

Search karna difficult hota hai.


Yani doctor aur patient dono ko records maintain karne mein problem hoti hai.


---

Hamara Solution

Hum is problem ko solve karne ke liye ek startup ka backend bana rahe hain.

Idea ye hai ke paper ki jagah saara data online store ho.

Doctor ke paas ek application hogi.

Us application ke through doctor har patient ka complete profile maintain karega.


---

Patient Profile

Har patient ke liye hum kuch information store karenge.

Jaise:

Patient ID

Name

City

Age

Gender

Height

Weight

BMI

Verdict


Video mein sirf basic information use ki gayi hai kyun ke ye beginner project hai.

Lekin real project mein aur bhi information add ki ja sakti hai.

Jaise:

Blood Group

Disease History

Allergies

Medicines

Reports

Sugar Level

Blood Pressure


Yani project ko future mein easily expand kiya ja sakta hai.


---

Data Kahan Store Hoga?

Ideal world mein humein data Database mein store karna chahiye.

Jaise:

MySQL

PostgreSQL

MongoDB


Lekin kyun ke ye basic FastAPI project hai, isliye database use nahi karenge.

Hum JSON File use karenge.

Yani jab bhi naya patient add hoga, uska record JSON file mein save hoga.

Video mein instructor ne bhi kaha tha:

> Method bilkul same rahega. Sirf Database ki jagah JSON file use kar rahe hain.



Yani CRUD ka logic database aur JSON dono mein almost same hota hai.


---

Doctor Kya Kar Sakega?

Doctor application ke through ye kaam karega:

1. New Patient Create

Doctor naya patient register karega.


---

2. Patient Profile View

Doctor kisi bhi patient ka profile dekh sakega.


---

3. Update Patient

Agar patient ka weight change ho gaya.

Ya city change ho gayi.

Ya age update karni ho.

To doctor uska record update karega.

Agar Height ya Weight change hogi.

To BMI bhi automatically dobara calculate ho jayega.

Ye point instructor ne specially mention kiya tha.


---

4. Delete Patient

Agar record ki zarurat na ho.

To doctor us patient ko delete bhi kar sakta hai.


---

Hamara Kaam Kya Hai?

Ye point bohot important hai.

Hum application nahi bana rahe.

Application banana Frontend Developer ka kaam hai.

Hum sirf Backend Engineers hain.

Hamara kaam sirf APIs develop karna hai.

Baad mein koi bhi developer:

Mobile App

Website

Desktop App


bana kar hamari APIs ko use kar sakta hai.

Yani Frontend aur Backend alag alag hote hain.


---

APIs Jo Hum Banayenge

Hum total 5 Endpoints banayenge.


---

1. Create Patient API

Method:

POST

Kaam:

Doctor form fill karega.

API us data ko receive karegi.

Aur JSON file mein save kar degi.


---

2. Get All Patients API

Method:

GET

Kaam:

JSON file ke andar jitne bhi patients honge.

Sab return kar dega.


---

3. Get Single Patient API

Method:

GET

Kaam:

Doctor kisi specific Patient ID ka record dekh sakega.

Example:

Patient ID 1

Patient ID 5

Patient ID 10


---

4. Update Patient API

Method:

PUT

Kaam:

Existing patient ki information update hogi.

Jaise:

Weight

Age

City

Height

Gender

etc.

BMI bhi automatically update ho sakta hai.


---

5. Delete Patient API

Method:

DELETE

Kaam:

Given Patient ID ka record JSON file se delete kar dega.


---

HTTP Methods

FastAPI mein hum HTTP Methods use karte hain.

Ye batate hain ke client server se kya kaam karwana chahta hai.


---

GET

Kaam:

Sirf data read ya fetch karna.

Is method se data change nahi hota.

Example:

Doctor saare patients dekhna chahta hai.

Ya kisi ek patient ka profile dekhna chahta hai.


---

POST

Kaam:

Naya data create karna.

Example:

Naya patient add karna.


---

PUT

Kaam:

Purana record update karna.

Example:

Weight change karna.

City change karna.

Age update karna.


---

DELETE

Kaam:

Record remove karna.

Example:

Patient ko system se delete karna.


---

HEAD

Video mein instructor ne HEAD method bhi mention kiya tha.

Ye actual data return nahi karta.

Sirf response ke baare mein information (Metadata) return karta hai.

Jaise:

Response available hai ya nahi.

Content Type kya hai.

Response Headers kya hain.


Body return nahi hoti.


---

JSON File

JSON ka matlab hai:

JavaScript Object Notation

Ye ek lightweight format hai jisme data key-value pairs ki form mein store hota hai.

Example:

id

name

city

age

gender

height

weight

bmi

verdict



---

Project Flow

Doctor
   │
   ▼
Frontend App
   │
HTTP Request
(GET / POST / PUT / DELETE)
   │
   ▼
FastAPI Backend
   │
Business Logic
   │
Read / Write
   │
   ▼
JSON File

Flow ki Explanation

1. Doctor frontend app mein patient ki details enter karega.


2. Frontend HTTP Request FastAPI Backend ko bhejega.


3. Backend request receive karega.


4. Backend validation aur business logic apply karega.


5. Backend JSON file se data read ya write karega.


6. Backend Response frontend ko bhej dega.


7. Frontend doctor ko updated information dikha dega.




---

Is Project se Hum Kya Seekhenge?

FastAPI project structure

API kya hoti hai

Endpoints banana

CRUD Operations

GET, POST, PUT, DELETE aur HEAD methods

Request aur Response ka flow

Path Parameters

JSON data handle karna

Backend aur Frontend ka connection

Real-world API development ki basic understanding


