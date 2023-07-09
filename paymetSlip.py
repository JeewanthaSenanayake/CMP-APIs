from fastapi import APIRouter
import database.paymetSlipDB as payments
payment_router = APIRouter(prefix="/cmp/api/v1/payment", tags=["Payment"])

@payment_router.put("/uploadSilp")
def uploadSilp(type:str, data:dict):
    payments.uploadASlip(type,data)
    return {"message": "Success"}

@payment_router.get("/getAllSlips")
def getAllSlips(type:str):
    data = payments.getAllPaymentSlips(type)
    return {"message": data}