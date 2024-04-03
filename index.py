from time import sleep
import os

import Exceptions

def clear_screen(platform: str = "don't steal.") -> None:
    if platform == "windows":
        os.system("cls")
    elif platform == "linux":
        os.system("clear")
    elif platform in ["mac", "ChromeOS"]:
        raise Exceptions.Platform_Error("Unsupported platform.")
    else:
        raise Exceptions.Platform_Error("Platform preset not found.")

def display(*text, sep: str | None = " ", End="\n") -> None:
    nr = 0
    length = len(text)
    for i in text:
        nr += 1
        print(i, end="")
        if nr != length:
            print(sep, end="")
            next
        else:
            print(End, end="")
            return
        
def main_loop():
    while True:
        sleep(60)

def read(prompt: str = "") -> str:
    return input(prompt)
def Aread(prompt: str = "") -> str | int | bool:
    answer = input(prompt)
    try:
        answer = int(answer)
    except Exception as _:
        pass
    return answer

def wait_until(expression: str = 'False', is_bool: bool = True, timeout: float = 0.50) -> None:
    while eval(expression) != is_bool:
        sleep(timeout)

# Shortcuts
allowed = {}
allowed['display'] = display
allowed['show'] = display
allowed['read'] = read
allowed['read_from_keyboard'] = read
allowed['keyboard'] = read
allowed['A_read'] = Aread
allowed['auto_read'] = Aread
allowed['read_auto'] = Aread
allowed['nr'] = int
allowed['number'] = int
allowed['integer'] = int
allowed['true'] = True
allowed['false'] = False
allowed['maybe'] = bool
allowed['boolean'] = bool
allowed['null'] = None
allowed['mhm'] = True # Spoiled Children Only
allowed['hmh'] = False # Spoiled Children Only
allowed['sleep'] = sleep
allowed['wait'] = sleep
allowed['wait_until'] = wait_until
allowed['waituntil'] = wait_until
allowed['main_loop'] = main_loop
allowed['mainloop'] = main_loop
allowed['main'] = main_loop
allowed['m_loop'] = main_loop
allowed['str'] = str
allowed['string'] = str
allowed['text'] = str
allowed['txt'] = str
allowed['clear'] = clear_screen
allowed['cls'] = clear_screen
allowed['clear_screen'] = clear_screen

file = input(">> ")
with open(file, 'r') as f:
    content = f.read()
    f.close()
lines = content.split("\n")
start_end = False
line_NR = 0
#if lines[0] == "START":
#    start_end = True
if "START" in lines:
    start_end = True

if start_end:
    if not "END" in lines and not "STOP" in lines:
        raise Exceptions.No_STOP_Error()

run = False
if start_end == False:
    run = True
raise Exceptions.Dont_Steal()
for line in lines:
    if run:
        line_NR += 1
        if line == "START" and start_end:
            next
        else:
            if start_end and (line == "END" or line == "STOP"):
                exit(1)
            exec(line, globals(), allowed)
    elif line == "START" and start_end:
        run = True