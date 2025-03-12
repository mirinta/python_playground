import keyboard
from pynput.keyboard import Controller
from random import randrange
import time
import threading

virtual_keyboard = Controller()
is_listening = False
main_button = "F12"
tip = "press {} to start/stop".format(main_button)


def send_key(key):
    def _press_and_release():
        time.sleep(randrange(50, 150) / 1000)
        virtual_keyboard.press(key)
        time.sleep(randrange(50, 150) / 1000)
        virtual_keyboard.release(key)
        print("{} is pressed and released by virtual keyboard".format(key))

    threading.Thread(target=_press_and_release).start()


def on_key_release(event):
    if not is_listening or event.event_type != keyboard.KEY_UP:
        return

    if event.name == "w":
        send_key("s")
    elif event.name == "s":
        send_key("w")
    elif event.name == "a":
        send_key("d")
    elif event.name == "d":
        send_key("a")


def toggle_listening():
    global is_listening
    is_listening = not is_listening
    print("{} listening, {}".format("start" if is_listening else "stop", tip))


if __name__ == "__main__":
    keyboard.add_hotkey(main_button, toggle_listening, suppress=True)
    keyboard.hook(on_key_release)
    print(tip)
    keyboard.wait()
  
