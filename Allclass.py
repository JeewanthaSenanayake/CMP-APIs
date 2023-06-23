from fastapi import APIRouter
import database.classDB as registration

class_router = APIRouter(prefix="/cmp/api/v1/class", tags=["Class"])

@class_router.post("/createClass")
def createClass(classType:str , data:dict):
    registration.createClass(classType,data)
    return {"message": "Success"}

@class_router.get("/getAllClass")
def getClass(classType:str ):
    data = registration.getAllClass(classType)
    return {"message": data}