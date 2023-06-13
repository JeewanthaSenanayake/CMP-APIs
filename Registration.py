from fastapi import APIRouter
import database.RegistrationDB as registration

registration_router = APIRouter(prefix="/cmp/api/v1/registration", tags=["Registration"])

@registration_router.get("/getRegiNum")
def getRegiNum(year:str):
    data = registration.getRegistrationNum(year)
    return {"message": data}

@registration_router.get("/getUser")
def getUser(regiNum:str):
    data = registration.getUser(regiNum)
    return {"message": data}

@registration_router.post("/createUser")
def createUser(regiNum:str,data:dict):
    registration.createAccount(regiNum,data)
    return {"message": "Success"}

@registration_router.delete("/deleteUser")
def deleteUser():
    return {"message": "This is getUser"}

