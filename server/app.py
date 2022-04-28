from flask import Flask, request, jsonify

from keystroke.keys_processed import *
from keystroke.model import *

app = Flask(__name__)

def find_user(user):
    with open('keystroke/userdata/users.txt', 'r') as f:
        users = f.read().splitlines()
        
    return True if user in users else False 

def add_user(user):
    with open('keystroke/userdata/users.txt', 'a+') as f:
        f.write(f'\n{user}')


@app.route("/new_client",  methods=['GET', 'POST'])
def new_client():
    if request.method == 'POST':
        data = request.get_json()
        user = data['user']
        add_user(user)
        keys = data['data']
        keys = convert_json(keys)
        save_capture_data_to_file(user, keys)
        processed_keys = processing_keys(user, keys)
        save_processed_data_to_file(user, processed_keys)
        create_and_train_model(user)
        return jsonify({'user':user, 'status':'Successfully'})
    else:
        return jsonify({'description':'Add new user to system'})


@app.route("/is_registered",  methods=['GET', 'POST'])
def is_registred():
    if request.method == 'POST':
        data = request.get_json()
        user = data['user']
        if find_user(user):
            return jsonify({'user':user, 'status':'Successfully'})
        else:
            return jsonify({'user':user, 'status':'Unsuccessfully'})    
    else:
        return jsonify({'description':'Check if user is registered'})


@app.route("/check_client",  methods=['GET', 'POST'])
def check_client():
    if request.method == 'POST':
        data = request.get_json()
        user = data['user']
        keys = data['data']
        keys = convert_json(keys)
        processed_keys = processing_keys(user, keys)
        return jsonify(check_user(user, processed_keys))
    else:
        return jsonify({'description':'Check user'})  


        