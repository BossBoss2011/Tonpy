def display(*text, sep: str | None = " ", end="\n"):
    print(text, sep = sep, end = end)
print(locals())
file = input(">> ")
with open(file, 'r') as f:
    content = f.read()
    f.close()
lines = content.split("\n")
start_end = False
line_NR = 0
if lines[0] == "START":
    start_end = True
for line in lines:
    line_NR += 1
    if line_NR == 1 and start_end:
        next
    exec(line, globals())