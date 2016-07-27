import random


letters = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
numerals = ("0123456789")
def generator():
    password = []
    while len(password) != 6:
        for i in range(4):
            item = random.randint(0, len(letters)-1)
            password.append(letters[item])
        for i in range(2):
            item = random.randint(0, len(numerals)-1)
            password.append(numerals[item])
    random.shuffle(password)
    password = ''.join(password)
    return password

#print(generator())
