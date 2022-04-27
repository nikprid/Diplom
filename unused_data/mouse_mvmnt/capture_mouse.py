from pynput import mouse
import time

class MouseLogger():
    def __init__(self, name, filename: str = "keylogs.csv") -> None:
        self.name = name
        self.filename = filename
        self.is_pressed = False
        with open(self.filename, 'w') as logs:
            logs.writelines('user,time,button,state,x,y\n')

    def on_move(self, x, y):
        if self.is_pressed == False:
            with open(self.filename, 'a') as logs:
                logs.writelines('{},{},{},{},{},{}\n'.format(self.name, time.time(), 'NoButton', 'Move', x, y))
        else:
            with open(self.filename, 'a') as logs:
                logs.writelines('{},{},{},{},{},{}\n'.format(self.name, time.time(), 'NoButton', 'Drag', x, y))    
                       

    def on_click(self, x, y, button, pressed):
        if not pressed:
            self.is_pressed = True
            with open(self.filename, 'a') as logs:
                logs.writelines('{},{},{},{},{},{}\n'.format(self.name, time.time(), button, 'Released', x, y))
        else:
            self.is_pressed = False
            with open(self.filename, 'a') as logs:
                logs.writelines('{},{},{},{},{},{}\n'.format(self.name, time.time(), button, 'Pressed', x, y))

    def main(self):
        listener = mouse.Listener(on_move=self.on_move, on_click=self.on_click)
        listener.start()
        try:
            listener.wait()
            input()
        finally:    
            listener.stop()


if __name__ == '__main__':
    name = input('Input your name: ')
    logger = MouseLogger(name, name+'_logs.csv')
    logger.main()