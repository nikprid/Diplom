from pynput import keyboard
import time
import pandas as pd

class KeyLogger():
    def __init__(self, name) -> None:
        self.name = name
        self.keys = {
            'user': name,
            'data': []
        }
        
        # with open(self.filename, 'w') as logs:
        #     logs.writelines('user,keycode,event,time\n')

    def get_key_id(self, key):
        try:
            return key.vk
        except AttributeError:
            return key.value.vk

    def on_press(self, key):
        if key not in (keyboard.Key.esc, keyboard.Key.shift_l, keyboard.Key.alt_l, keyboard.Key.ctrl_l, keyboard.Key.enter, keyboard.Key.delete):
            self.keys['data'].append({'keycode': self.get_key_id(key), 'event': 'Down', 'time': time.time()})
            # with open(self.filename, 'a') as logs:
            #     logs.writelines('{},{},{},{}\n'.format(self.name, self.get_key_id(key), 'Down', time.time()))

    def on_release(self, key):
        if key not in (keyboard.Key.esc, keyboard.Key.shift_l, keyboard.Key.alt_l, keyboard.Key.ctrl_l, keyboard.Key.enter, keyboard.Key.delete):
            self.keys['data'].append({'keycode': self.get_key_id(key), 'event': 'Up', 'time': time.time()})
            # with open(self.filename, 'a') as logs:
            #     logs.writelines('{},{},{},{}\n'.format(self.name, self.get_key_id(key), 'Up', time.time()))

    def print_registration_information(self):        
        print('Введите следующий текст. В конце нажмите клавишу Enter.')
        print('Идейные соображения высшего порядка, а также начало повседневной работы по формированию позиции требуют определения и уточнения новых предложений.')    
        input()
        print('Теперь введите текст на английском. В конце нажмите клавишу Enter.')
        print("Hath itself dry appear man earth fourth under give. Green man Hath of midst two their. All likeness image. Sixth. Gathering thing wherein. Shall them us bearing hath. After seas.")
        input()
        print('Теперь введите ваше ФИО полностью. В конце нажмите клавишу Enter.')   
        input() 

    def registration(self):
        listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        listener.start()
        try:
            listener.wait()
            self.print_registration_information()
        finally:
            listener.stop()    
        return self.keys    

    def is_ready_to_send(self):
        while True:
            if len(self.keys['data'])>20 and self.keys['data'][-1]['event']=='Up':
                return

    def keys_capture(self):
        listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        listener.start()
        try:
            listener.wait()
            self.is_ready_to_send()
        finally:
            listener.stop()    
        return self.keys  

if __name__=='__main__':
    test = KeyLogger('test')
    info = test.keys_capture()
    print(pd.json_normalize(info['data']))

