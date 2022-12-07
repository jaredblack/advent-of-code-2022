# sliding windo beby
in_file = open('in/day6.txt')
st = in_file.read()
in_file.close()

for i in range(len(st) - 4):
    sub = set(st[i:i+4])
    if len(sub) == 4:
        print(i+4)
        break

for i in range(len(st) - 14):
    sub = set(st[i:i+14])
    if len(sub) == 14:
        print(i+14)
        break