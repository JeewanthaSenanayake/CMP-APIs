import database.firebase as firebaseCon

db = firebaseCon.get_firestore_client()

def uploadASlip(type:str, data:dict):
    doc_ref = db.collection('slips').document(type)
    try:
        allSlips = doc_ref.get().to_dict()
        
        SlipsList = allSlips["paymentSlips"]
        SlipsList.append(data)
        doc_ref.update({"paymentSlips":SlipsList})
    except:
        print("Creating new  class type")
        SlipsList = []
        SlipsList.append(data)
        doc_ref.set({"paymentSlips":SlipsList})


def getAllPaymentSlips(type:str):
    doc_ref = db.collection('slips').document(type)
    try:
        allSlips = doc_ref.get().to_dict()
        SlipsList = allSlips["paymentSlips"]
        return SlipsList
    except:
        emptyList = []
        return emptyList