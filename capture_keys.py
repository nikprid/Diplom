from pynput import keyboard
import time

class KeyLogger():
    def __init__(self, name, filename: str = "keylogs.csv") -> None:
        self.name = name
        self.filename = filename
        with open(self.filename, 'w') as logs:
            logs.writelines('keycode,event,time\n')

    def get_key_id(self, key):
        try:
            return key.vk
        except AttributeError:
            return key.value.vk

    def on_press(self, key):
        if key not in (keyboard.Key.esc, keyboard.Key.shift_l, keyboard.Key.alt_l, keyboard.Key.ctrl_l, keyboard.Key.enter, keyboard.Key.delete):
            with open(self.filename, 'a') as logs:
                logs.writelines('{},{},{}\n'.format(self.get_key_id(key), 'Down', time.time()))

    def on_release(self, key):
        if key not in (keyboard.Key.esc, keyboard.Key.shift_l, keyboard.Key.alt_l, keyboard.Key.ctrl_l, keyboard.Key.enter, keyboard.Key.delete):
            with open(self.filename, 'a') as logs:
                logs.writelines('{},{},{},{}\n'.format(self.get_key_id(key), 'Up', time.time()))

    def main(self):
        listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        listener.start()
        try:
            listener.wait()
            input()
        finally:
            listener.stop()


if __name__ == '__main__':
    name = input('Input your name: ')
    logger = KeyLogger(name, name+'_logs.csv')
    print('Введите следующий текст. В конце нажмите клавишу Enter.')
    print('Идейные соображения высшего порядка, а также начало повседневной работы по формированию позиции требуют определения и уточнения новых предложений.')
    logger.main()
    print('Теперь введите. В конце нажмите клавишу Enter.')
    print("Hath itself dry appear man earth fourth under give. Green man Hath of midst two their. All likeness image. Sixth. Gathering thing wherein. Shall them us bearing hath. After seas.")
    logger.main()
    print('Теперь введите ваше ФИО. В конце нажмите клавишу Enter.')
    logger.main()