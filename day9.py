in_file = open('in/day9.txt')
st = in_file.read()
in_file.close()

LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, 1)
DOWN = (0, -1)

def get_dir(d):
    if d == 'L':
        return LEFT
    elif d == 'R':
        return RIGHT
    elif d == 'U':
        return UP
    elif d == 'D':
        return DOWN

def tsum(a,b):
    return tuple(sum(x) for x in zip(a,b))

head_pos = 0, 0
tail_pos = 0, 0
tail_pos_hist = {tail_pos}
for line in st.splitlines():
    dir, mag = line.split()
    dir = get_dir(dir)
    mag = int(mag)
    for i in range(mag):
        head_pos = tsum(head_pos, dir)
        if head_pos[0] == tail_pos[0]:
            if head_pos[1] > tail_pos[1] + 1:
                tail_pos = tsum(tail_pos, UP)
            elif head_pos[1] < tail_pos[1] - 1:
                tail_pos = tsum(tail_pos, DOWN)
        elif head_pos[1] == tail_pos[1]:
            if head_pos[0] > tail_pos[0] + 1:
                tail_pos = tsum(tail_pos, RIGHT)
            elif head_pos[0] < tail_pos[0] - 1:
                tail_pos = tsum(tail_pos, LEFT)
        else:
            if head_pos[0] > tail_pos[0] and head_pos[1] > tail_pos[1]:
                new_pos = tsum(tail_pos, tsum(RIGHT, UP))
            elif head_pos[0] > tail_pos[0] and head_pos[1] < tail_pos[1]:
                new_pos = tsum(tail_pos, tsum(RIGHT, DOWN))
            elif head_pos[0] < tail_pos[0] and head_pos[1] < tail_pos[1]:
                new_pos = tsum(tail_pos, tsum(LEFT, DOWN))
            elif head_pos[0] < tail_pos[0] and head_pos[1] > tail_pos[1]:
                new_pos = tsum(tail_pos, tsum(LEFT, UP))
            if new_pos != head_pos:
                tail_pos = new_pos
        tail_pos_hist.add(tail_pos)

print("Part 1")
print(len(tail_pos_hist))

head_pos = 0, 0
snake = [(0, 0) for _ in range(9)]
tail_pos_hist = {(0,0)}
for line in st.splitlines():
    dir, mag = line.split()
    dir = get_dir(dir)
    mag = int(mag)
    for i in range(mag):
        head_pos = tsum(head_pos, dir)
        prev = head_pos
        for i, tail_pos in enumerate(snake):
            if prev[0] == tail_pos[0]:
                if prev[1] > tail_pos[1] + 1:
                    tail_pos = tsum(tail_pos, UP)
                elif prev[1] < tail_pos[1] - 1:
                    tail_pos = tsum(tail_pos, DOWN)
            elif prev[1] == tail_pos[1]:
                if prev[0] > tail_pos[0] + 1:
                    tail_pos = tsum(tail_pos, RIGHT)
                elif prev[0] < tail_pos[0] - 1:
                    tail_pos = tsum(tail_pos, LEFT)
            else:
                if prev[0] > tail_pos[0] and prev[1] > tail_pos[1]:
                    new_pos = tsum(tail_pos, tsum(RIGHT, UP))
                elif prev[0] > tail_pos[0] and prev[1] < tail_pos[1]:
                    new_pos = tsum(tail_pos, tsum(RIGHT, DOWN))
                elif prev[0] < tail_pos[0] and prev[1] < tail_pos[1]:
                    new_pos = tsum(tail_pos, tsum(LEFT, DOWN))
                elif prev[0] < tail_pos[0] and prev[1] > tail_pos[1]:
                    new_pos = tsum(tail_pos, tsum(LEFT, UP))
                if new_pos != prev:
                    tail_pos = new_pos
            snake[i] = tail_pos
            prev = tail_pos
        tail_pos_hist.add(tail_pos)
print("Part 2: ")
print(len(tail_pos_hist))
