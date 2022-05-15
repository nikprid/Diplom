import requests
import sys

from keylogger import KeyLogger

def is_registred(server_url, user):
    answer = requests.post(server_url+':5000/is_registered', json={'user':user}).json()
    return True if answer['status']=='is_exist' else False

def registration(server_url, user):
    keylogger = KeyLogger(user)
    registration_data = keylogger.registration()
    answer = requests.post(server_url+':5000/new_client', json=registration_data).json()
    if answer['status'] == 'successfully':
        print('\n[+] Удачная регистрация')
    else: 
        print('\n[+] Неудачная регистрация')   

def check_user(server_url, user):
    keylogger = KeyLogger(user)
    capture_data = keylogger.keys_capture()
    answer = requests.post(server_url+':5000/check_client', json=capture_data).json()
    print(answer['result'])


def main():
    server_url = sys.argv[1]
    user = input('Введите ваше имя: ')
    if not is_registred(server_url, user):
        registration(server_url, user)
    else:
        print('[+] Пользователь уже существует в системе.')
    while True:
        check_user(server_url, user)

if __name__ == '__main__':
    main()    

