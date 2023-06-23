import database.firebase as firebaseCon

db = firebaseCon.get_firestore_client()

def createClass(classType:str,data:dict):
    doc_ref = db.collection('cmp').document(classType)
    
    try:
        count = doc_ref.get().to_dict()
        newData = {str(count['count']):data, 'count':count['count']+1}
        doc_ref.update(newData)
    except:
        print("Creating new document")
        doc_ref.set({"0":data, 'count':1})

def getAllClass(classType:str):
    doc_ref = db.collection('cmp').document(classType)
    data = doc_ref.get().to_dict()
    dataList = []
    for i in range(0,int(data['count'])):
        dataList.append(data[str(i)])
    return dataList
         
    