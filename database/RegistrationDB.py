import database.firebase as firebaseCon

db = firebaseCon.get_firestore_client()

# Use db to interact with Firestore
def setData():
    doc_ref = db.collection('collection_name').document('document_id')
    doc_ref.set({'field1': 'dfd', 'field2': 'value2','field3': 'value3'})