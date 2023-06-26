import database.firebase as firebaseCon

db = firebaseCon.get_firestore_client()

def registerForClass(classType:str, classId:int, studentId:str):
    doc_ref = db.collection('cmp').document(classType)
    try:
        classData = doc_ref.get().to_dict()
        data = classData[str(classId)]
        regiList = data['regiStudents']
        regiSet = set(regiList)
        regiSet.add(studentId)
        newData= {str(classId):{"regiStudents":list(regiSet)}}
        doc_ref.update(newData)
        return "Success"
    except:
        print("Creating new document")
        return "Error"
        

def setClassData(classType:str, classId:int, data:dict):
    colname = classType + 'Class'
    doc = 'class'+str(classId)
    doc_ref = db.collection(colname).document(doc)
    try:
        day = doc_ref.get().to_dict()
        data["day"] = day['day']
        data['classId'] = classId
        newData = {str(day['day']):data, 'day':day['day']+1}
        doc_ref.update(newData)
    except:
        print("Creating new document")
        data["day"] = 0
        data['classId'] = classId
        doc_ref.set({"0":data, 'day':1})

def createClass(classType:str,data:dict):
    doc_ref = db.collection('cmp').document(classType)
    
    try:
        count = doc_ref.get().to_dict()
        data["id"] = count['count']
        data["regiStudents"]=[]
        newData = {str(count['count']):data, 'count':count['count']+1}
        doc_ref.update(newData)
    except:
        print("Creating new document")
        data["id"] = 0
        data["regiStudents"]=[]
        doc_ref.set({"0":data, 'count':1})

def getAllClass(classType:str):
    doc_ref = db.collection('cmp').document(classType)
    data = doc_ref.get().to_dict()
    dataList = []
    for i in range(0,int(data['count'])):
        dataList.append(data[str(i)])
    return dataList
         
    