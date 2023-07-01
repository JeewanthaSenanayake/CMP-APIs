import database.firebase as firebaseCon
from datetime import date

db = firebaseCon.get_firestore_client()

def registeredClassData(classType: str, studentId: str):
    today = date.today()
    classYearMonuth = today.strftime("%Y-%B")
    registerdClassList = []
    doc_ref = db.collection('cmp').document(classType)
    payment_ref = db.collection('payment').document(studentId)
    payment = payment_ref.get().to_dict()
    data = doc_ref.get().to_dict()
    dataList = []
    for i in range(0, int(data['count'])):
        if studentId in data[str(i)]['regiStudents']:
            dataList.append(data[str(i)])
    
    for classData in dataList:
        classId = classData['id']
        try:
            class_ref = db.collection(f'{classType}Class').document(f"class{classId}")
            classDataSet = class_ref.get().to_dict()
            TodayClassData = classDataSet[str(classDataSet['day']-1)]
            paymentData = payment[classType][str(classId)][classYearMonuth]
            if(paymentData == True):
                TodayClassData['paymentDone'] = 1
            else:
                TodayClassData['paymentDone'] = 0
            registerdClassList.append(TodayClassData)
        except:
            print("No Class Data")

    return registerdClassList

def registerForClass(classType: str, classId: int, studentId: str):
    doc_ref = db.collection('cmp').document(classType)
    payment_ref = db.collection('payment').document(studentId)
    today = date.today()
    year = today.strftime("%Y")
    # d3 = today.strftime("%Y-%B")
    try:
        # register for class
        classData = doc_ref.get().to_dict()
        data = classData[str(classId)]
        regiList = data['regiStudents']
        regiSet = set(regiList)
        regiSet.add(studentId)
        data['regiStudents'] = list(regiSet)
        newData = {str(classId): data}
        doc_ref.update(newData)
        # payement
        try:
            paymentData = payment_ref.get().to_dict()
            paymentData[classType][str(classId)] = {

                f"{year}-January": 0,
                f"{year}-February": 0,
                f"{year}-March": 0,
                f"{year}-April": 0,
                f"{year}-May": 0,
                f"{year}-June": 0,
                f"{year}-July": 0,
                f"{year}-August": 0,
                f"{year}-September": 0,
                f"{year}-October": 0,
                f"{year}-November": 0,
                f"{year}-December": 0

            }
            payment_ref.update(paymentData)
            return "Success"
        except:
            print("Creating new document 2")
            data = {
                str(classId): {
                    f"{year}-January": 0,
                    f"{year}-February": 0,
                    f"{year}-March": 0,
                    f"{year}-April": 0,
                    f"{year}-May": 0,
                    f"{year}-June": 0,
                    f"{year}-July": 0,
                    f"{year}-August": 0,
                    f"{year}-September": 0,
                    f"{year}-October": 0,
                    f"{year}-November": 0,
                    f"{year}-December": 0
                }
            }
            payment_ref.set({classType: data})
            return "Success"
    except:
        print("Creating new document")
        return "Error"


def setClassData(classType: str, classId: int, data: dict):
    colname = classType + 'Class'
    doc = 'class'+str(classId)
    doc_ref = db.collection(colname).document(doc)
    try:
        day = doc_ref.get().to_dict()
        data["day"] = day['day']
        data['classId'] = classId
        newData = {str(day['day']): data, 'day': day['day']+1}
        doc_ref.update(newData)
    except:
        print("Creating new document")
        data["day"] = 0
        data['classId'] = classId
        doc_ref.set({"0": data, 'day': 1})


def createClass(classType: str, data: dict):
    doc_ref = db.collection('cmp').document(classType)

    try:
        count = doc_ref.get().to_dict()
        data["id"] = count['count']
        data["regiStudents"] = []
        newData = {str(count['count']): data, 'count': count['count']+1}
        doc_ref.update(newData)
    except:
        print("Creating new document")
        data["id"] = 0
        data["regiStudents"] = []
        doc_ref.set({"0": data, 'count': 1})


def getAllClass(classType: str):
    doc_ref = db.collection('cmp').document(classType)
    data = doc_ref.get().to_dict()
    dataList = []
    for i in range(0, int(data['count'])):
        dataList.append(data[str(i)])
    return dataList
