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

@class_router.put("/setClassData")
def setClassData(classType:str , classId:int, data:dict):
    registration.setClassData(classType, classId, data)
    return {"message": "Success"}

@class_router.put("/registerForClass")
def registerForClass(classType:str , classId:int, studentId:str):
    data = registration.registerForClass(classType, classId, studentId)
    return {"message": data}

@class_router.get("/registeredClassData")
def registeredClassData(classType:str , studentId:str):
    data = registration.registeredClassData(classType, studentId)
    return {"message": data}