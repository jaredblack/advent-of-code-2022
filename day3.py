in_file = open('in/day3.txt')
st = in_file.read()
in_file.close()

def get_score(c):
    if c.isupper():
        return ord(c) - 38
    else:
        return ord(c) - 96

score = 0
for line in st.split('\n'):
    c1 = set(line[:len(line)//2])
    c2 = set(line[len(line)//2:])
    common = c1.intersection(c2)
    for c in common:
        score += get_score(c)

print(f"Part A: {score}")

score = 0
lines = st.split('\n')
for i in range(0, len(lines), 3):
    s = set(lines[i])
    for j in range(2):
        s = s.intersection(lines[i+j+1])
    for c in s:
        score += get_score(c)

print(score)