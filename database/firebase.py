import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

path = 'database/cmp--api-firebase-adminsdk-2wyij-04936aafb4.json'
cred = credentials.Certificate(path)
firebase_admin.initialize_app(cred)

def get_firestore_client():
    return firestore.client()


