import database.firebase as firebaseCon

db = firebaseCon.get_firestore_client()

def getUser(regiNo):
    doc_ref = db.collection('Users')
    all_docs = doc_ref.get()

    userData = 'no user found'

    for doc in all_docs:
        if doc.to_dict()['data']['regiNo'] == regiNo:
            userData = doc.to_dict()
            break
    
    return userData

        

    
def getRegistrationNum(year):
    doc_ref = db.collection('yearOfAl').document('count')
    data = doc_ref.get().to_dict()
    reg = year[2]+year[3]+'CMP'+str(data['count'])
    count = {"count":data['count']+1}
    doc_ref.update(count)
    return reg

def createAccount(regiNum:str,data:dict):
    doc_ref = db.collection('Users').document(str(regiNum))
    doc_ref.set({"data":data})