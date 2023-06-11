from fastapi import APIRouter
import database.AlYearDB as registration

year_of_al = APIRouter(prefix="/cmp/api/v1/alyears", tags=["A/L Years"])

@year_of_al.get("/getAlYears")
def getYear():
    data = registration.getData()
    return {"message": data}

@year_of_al.put("/setAlYears")
def setYear():
    return {"message": "This is getUser"}



