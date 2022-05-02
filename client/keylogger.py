from pynput import keyboard
import time
import pandas as pd

special_keys = (keyboard.Key.esc, keyboard.Key.shift_l, keyboard.Key.alt_l, keyboard.Key.ctrl_l, keyboard.Key.enter, keyboard.Key.delete,
                keyboard.Key.backspace, keyboard.Key.caps_lock, keyboard.Key.cmd, keyboard.Key.down, keyboard.Key.end, keyboard.Key.left,
                keyboard.Key.num_lock, keyboard.Key.page_down, keyboard.Key.page_up, keyboard.Key.up, keyboard.Key.print_screen, keyboard.Key.right,)

class KeyLogger():
    def __init__(self, name) -> None:
        self.name = name
        self.keys = {
            'user': name,
            'data': []
        }


    def get_key_id(self, key):
        try:
            return key.vk
        except AttributeError:
            return key.value.vk

    def on_press(self, key):
        if key not in special_keys:
            self.keys['data'].append({'keycode': self.get_key_id(key), 'event': 'Down', 'time': time.time()})


    def on_release(self, key):
        if key not in special_keys:
            self.keys['data'].append({'keycode': self.get_key_id(key), 'event': 'Up', 'time': time.time()})

    def print_registration_information(self):        
        print('Введите следующий текст. В конце нажмите клавишу Enter.')
        print('Идейные соображения высшего порядка, а также начало повседневной работы по формированию позиции требуют определения и уточнения новых предложений.')    
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
            if len(self.keys['data'])>25 and self.keys['data'][-1]['event']=='Up':
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


