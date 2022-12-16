in_file = open('in/day10.txt')
st = in_file.read()
in_file.close()

cmd_i = 0
cmds = st.splitlines()
time_to_add = False
amt = 0
X = 1
sig_strength = 0
for i in range(1, 221):
    if (i - 20) % 40 == 0:
        sig_strength += X * i
    if not time_to_add:
        if cmd_i >= len(cmds):
            break
        if cmds[cmd_i].startswith("addx"):
            amt = int(cmds[cmd_i].split()[1])
            time_to_add = True
        cmd_i += 1
    else:
        X += amt
        time_to_add = False

print("Part 1")
print(sig_strength)

cmd_i = 0
X = 1
time_to_add = False
line = -1
for i in range(1, 241):
    if (i - 1) % 40 == 0:
        print()
        line += 1
    c = ' '
    if X in range(i-2 - line * 40, i+1 - line * 40):
        c = '#'
    print(c, end='')
    if not time_to_add:
        if cmd_i >= len(cmds):
            break
        if cmds[cmd_i].startswith("addx"):
            amt = int(cmds[cmd_i].split()[1])
            time_to_add = True
        cmd_i += 1
    else:
        X += amt
        time_to_add = False
