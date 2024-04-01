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

def read(prompt: str = "") -> str:
    return input(prompt)
def Aread(prompt: str = "") -> str | int | bool:
    answer = input(prompt)
    try:
        answer = int(answer)
    except Exception as _:
        pass
    return answer

class No_STOP_Error(Exception):
    def __init__(self):
        super().__init__("No STOP provided.")

STOP = None

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
allowed['true'] = True
allowed['false'] = False
allowed['maybe'] = bool
allowed['null'] = None
allowed['mhm'] = True # Spoiled Children Only
allowed['hmh'] = False # Spoiled Children Only

file = input(">> ")
with open(file, 'r') as f:
    content = f.read()
    f.close()
lines = content.split("\n")
start_end = False
line_NR = 0
if lines[0] == "START":
    start_end = True
if start_end and (lines[-1] != "END" and lines[-1] != "STOP"):
    raise No_STOP_Error()
for line in lines:
    line_NR += 1
    if line_NR == 1 and start_end:
        next
    else:
        exec(line, globals(), allowed)
