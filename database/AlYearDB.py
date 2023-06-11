import database.firebase as firebaseCon

db = firebaseCon.get_firestore_client()

# Use db to interact with Firestore
def getData():
    doc_ref = db.collection('yearOfAl').document('years')
    data = doc_ref.get().to_dict()
    return data

    
