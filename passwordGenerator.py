import random, string, re

candidates = []

def generate():
    #x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + 
    #    string.punctuation) for _ in range(16)) 

    random_uppercase = ''.join(random.choice(string.ascii_uppercase) for _ in range(random.randint(0, 5)))
    x = random_uppercase + ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(0, 5)))
    x = x + ''.join(random.choice(string.digits) for _ in range(random.randint(0, 5)))
    # write a python test
    return x

def fitness(candidate):
    # a candidate is a password that is generated from generate()
    # add processing for rules
    score = 0
    n = len(candidate)
    for i in range(0, n):
        char = candidate[i]

        # adds one to score for each char
        if re.match("^[a-zA-Z0-9_]*", char):
            score += 1

        #take 3 off score for seqs of 3 or more of the same char in a row
        if i < n - 2 == candidate[i + 1] and candidate[i + 2]:
            score -= 3

        # adds an add'l point if the letter is different
        if i > 0 and candidate[i] != candidate[i - 1]:
            score += 1

        # adds two to score if char is a special char
        if re.match("[!@#$%^&*()~`]{1,}", char):
            score += 2
        # run the function, get some numbers, then figure out a good minimum number
        # to have as a baseline for a "good" password (keep the ones with a good score)
        # throw out the scores that aren't good
   
    if score > 12:
        return score

    elif score < 12:
        # knocks off the current element if its score is too low
        candidate.pop()

    return score

for possibility in range(0, 100):
    candidates.append(generate())
    print(candidates[possibility])

    score2 = fitness(candidates[possibility])
    print(score2)