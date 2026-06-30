from fastapi import FastAPI
from pydantic import BaseModel, field_validator
app=FastAPI()

class Inputemail(BaseModel):
    email:str

    @field_validator("email")
    @classmethod
    def checkemail(cls,value):
        return "".join(value.strip().lower().split())
    
@app.post("/student")
def checkmail(email:Inputemail):
    return email