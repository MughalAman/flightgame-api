import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account. place the json file in the same directory as this file
cred = credentials.Certificate('db_credentials.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()