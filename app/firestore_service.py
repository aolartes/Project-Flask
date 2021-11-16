import collections
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from .forms import NewClientForm



project_id = 'modeloprograii'

credential = credentials.ApplicationDefault()
firebase_admin.initialize_app(credential, {
  'projectId': project_id,
})

# credential = credentials.ApplicationDefault()
# firebase_admin.initialize_app(credential)

db = firestore.client()


def get_users():
    return db.collection('users').get()


def get_user(user_id):
    return db.collection('users').document(user_id).get()


def user_put(user_data):
    user_ref = db.collection('users').document(user_data.username)
    user_ref.set({'password': user_data.password})


def get_todos(user_id):
    return db.collection('users')\
        .document(user_id)\
        .collection('todos').get()

def put_client (cedula,nombre,telefono,direccion):
    cliente_collection_ref = db.collection('cliente').document(cedula).collection('information')
    cliente_collection_ref.add({
                                'phone': telefono,
                                'address':direccion,
                                'client': nombre
                                })

def get_client (cedula):
    return db.collection('cliente')\
                .document(cedula)\
                .collection('information').get()
    

    

    



    #return doc()
    


    
    




# def put_todo(user_id, description):
#     todos_collection_ref = db.collection('users').document(user_id).collection('todos')
#     todos_collection_ref.add({'description': description})

