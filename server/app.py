from flask import Flask, request, jsonify

import datetime

from keystroke.keys_processed import *
from keystroke.model import *

app = Flask(__name__)

def find_user(user):
    with open('users.txt', 'r') as f:
        users = f.read().splitlines()
        
    return True if user in users else False 

def add_user(user):
    with open('users.txt', 'a+') as f:
        f.write(f'\n{user}')

def write_to_log_file(user, proba):
    with open('users.txt', 'a+') as f:
        f.write(f'\n[+] {datetime.datetime.now()} - {user} - {proba}')

@app.route("/new_client",  methods=['GET', 'POST'])
def new_client():
    if request.method == 'POST':
        data = request.get_json()
        try:
            user = data['user']
            add_user(user)
            keys = data['data']
            keys = convert_json(keys)
            save_capture_data_to_file(user, keys)
            processed_keys = processing_keys(keys)
            save_processed_data_to_file(user, processed_keys)
            create_and_train_model(user)
            return jsonify({'user':user, 'status':'successfully'})
        except:
            return jsonify({'user':user, 'status':'unsuccessfully'})    
    else:
        return jsonify({'description':'Add new user to system'})


@app.route("/is_registered",  methods=['GET', 'POST'])
def is_registred():
    if request.method == 'POST':
        data = request.get_json()
        user = data['user']
        if find_user(user):
            return jsonify({'user':user, 'status':'is_exist'})
        else:
            return jsonify({'user':user, 'status':'does_not_exist'})    
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
        proba = check_user(user, processed_keys)
        write_to_log_file(user, proba)
        if  proba>0.65:
            return jsonify({'user':user, 'result': f'valid - {proba}'})
        else:
            return jsonify({'user':user, 'result': f'intruder - {proba}'})
    else:
        return jsonify({'description':'Check user'})  


        