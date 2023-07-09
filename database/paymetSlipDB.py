import database.firebase as firebaseCon
from datetime import datetime

db = firebaseCon.get_firestore_client()

def uploadASlip(type:str, data:dict):
    doc_ref = db.collection('slips').document(type)
    try:
        allSlips = doc_ref.get().to_dict()
        
        SlipsList = allSlips["paymentSlips"]
        SlipsList.append(data)
        doc_ref.update({"paymentSlips":SlipsList})
        
        # Convert the string to a datetime object
        date_object = datetime.strptime(data["month"], "%Y-%m")
        # Convert the datetime object to the desired format
        formatted_date = date_object.strftime("%Y-%B")
        changePaymentStatus(data["uid"],type,data["id"],formatted_date,1)
    except:
        print("Creating new  class type")
        SlipsList = []
        SlipsList.append(data)
        doc_ref.set({"paymentSlips":SlipsList})
        # Convert the string to a datetime object
        date_object = datetime.strptime(data["month"], "%Y-%m")
        # Convert the datetime object to the desired format
        formatted_date = date_object.strftime("%Y-%B")
        changePaymentStatus(data["uid"],type,data["id"],formatted_date,1)


def getAllPaymentSlips(type:str):
    doc_ref = db.collection('slips').document(type)
    try:
        allSlips = doc_ref.get().to_dict()
        SlipsList = allSlips["paymentSlips"]
        return SlipsList
    except:
        emptyList = []
        return emptyList
    
def changePaymentStatus(uid:str,type:str,classId:int,month:str,status:int):
    doc_ref = db.collection('payment').document(uid)
    try:
        allRegisterdClasss=doc_ref.get().to_dict()
        allRegisterdClasss[type][str(classId)][month]=status
        doc_ref.update(allRegisterdClasss)
    except:
        print("No data found")
