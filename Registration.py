from fastapi import APIRouter
import database.RegistrationDB as registration

registration_router = APIRouter(prefix="/cmp/api/v1/registration", tags=["Registration"])

@registration_router.get("/getUser")
def getUser():
    registration.setData()
    return {"message": "This is getUser"}

@registration_router.put("/createUser")
def createUser():
    return {"message": "This is getUser"}

@registration_router.delete("/deleteUser")
def deleteUser():
    return {"message": "This is getUser"}

