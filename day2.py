in_file = open('in/day2.txt')
st = in_file.read()
in_file.close()

ROCK = ('A', 'X')
PAPER = ('B', 'Y')
SCISSORS = ('C', 'Z')

LOSE = 'X'
DRAW = 'Y'
WIN = 'Z'

def det_winner(a, b):
    if a in ROCK and b in PAPER or \
        a in PAPER and b in SCISSORS or \
        a in SCISSORS and b in ROCK:
        return 6
    if b in ROCK and a in PAPER or \
        b in PAPER and a in SCISSORS or \
        b in SCISSORS and a in ROCK:
        return 0
    return 3


lines = [[c for c in line.split()] for line in st.split('\n')]

score = 0
for line in lines:
    me = line[1]
    if me in ROCK:
        score += 1
    elif me in PAPER:
        score += 2
    elif me in SCISSORS:
        score += 3
    score += det_winner(line[0], me)
        
print(f"Part 1: {score}")

score = 0
for line in lines:
    them = line[0]
    outcome = line[1]
    if outcome == LOSE:
        # me sciss
        if them in ROCK:
            score += 3
        # me rock
        elif them in PAPER:
            score += 1
        # me paper
        else:
            score += 2
    elif outcome == WIN:
        score += 6
        # me paper
        if them in ROCK:
            score += 2
        # me scissors
        elif them in PAPER:
            score += 3
        # me rock
        else:
            score += 1
    else:
        score += 3
        if them in ROCK:
            score += 1
        elif them in PAPER:
            score += 2
        else:
            score += 3

print(f"Part 2: {score}")