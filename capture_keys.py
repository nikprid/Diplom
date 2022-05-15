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
    name = input('Введите ваше имя: ')
    logger = KeyLogger(name, name+'_logs.csv')
    print('Введите следующий текст. В конце нажмите клавишу Enter.')
    print('When the ladies removed after dinner, Elizabeth ran up to her sister, and seeing her well guarded from cold. What could be more natural than his asking you again?')
    logger.main()
    print('Теперь введите. В конце нажмите клавишу Enter.')
    print("These reflections just here are occasioned by the circumstance that after we were all seated at the table. But to be candid without ostentation or design to take the good of everybody's character and make it still better.")
    logger.main()