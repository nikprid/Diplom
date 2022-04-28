import requests
import sys

from keylogger import KeyLogger

def is_registred(server_url, user):
    answer = requests.post(server_url+':5000/is_registered', json={'user':user}).json()
    return True if answer['status']=='Successfully' else False

def registration(server_url, user):
    keylogger = KeyLogger(user)
    registration_data = keylogger.registration()
    print(registration_data)
    answer = requests.post(server_url+':5000/new_client', json=registration_data).json()
    if answer['status'] == 'Successfully':
        print('\n[+] Successfully registration')
    else: 
        print('\n[+] Unsuccessfully registration')   

def check_user(server_url, user):
    keylogger = KeyLogger(user)
    capture_data = keylogger.keys_capture()
    answer = requests.post(server_url+':5000/check_client', json=capture_data).json()
    print(answer['result'])


def main():
    server_url = sys.argv[1]
    user = input('Input your name: ')
    if not is_registred(server_url, user):
        registration(server_url, user)
    while True:
        check_user(server_url, user)

if __name__ == '__main__':
    main()    

