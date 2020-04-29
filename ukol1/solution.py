import matplotlib.pyplot as plt
from math import log

K = 27 # den narození reprezentanta skupiny (1-31),
surname = "Pšenička"
L = len(surname) # počet písmen v příjmení reprezentanta,
X = ((K*L*23) % (20)) + 1
Y = ((X + ((K*5 + L*7) % (19))) % (20)) + 1

folder = "..//hw1-source//"
xxx = str(str(X).zfill(3)) + ".txt"
yyy = str(str(Y).zfill(3)) + ".txt"

def entropy(prob):
    ent = 0
    for p in prob:
        ent += p * log(p, 2)
    ent *= -1
    return ent

def char_prob(filename):
    with open(filename, "r") as file:
        chars = dict()
        char_count = 0
        for line in file:
            for c in line:
                if c == '\n': c = '\\n'
                if c == ' ': c = '␣'
                if c not in chars:
                    chars[c] = 1
                else:
                    chars[c] += 1
                char_count += 1

        for c, v in chars.items():
            chars[c] = v / char_count

        print("Char\t|  Count")
        print("--------------")
        sorted_chars = sorted(chars, key=chars.get, reverse=True)
        sorted_values = []
        print(sorted_chars)
        for c in sorted_chars:
            sorted_values.append(chars[c])
            print(f'"{c}"\t| {chars[c]}')

        ent = entropy(sorted_values)
        print(f'Chars entropy: {ent}')

        plt.bar(sorted_chars, sorted_values, width=0.5, color='g')
        plt.title("Grafické znázornění pravděpodobností znaků textu")
        plt.xlabel("Znaky výchozího textu")
        plt.ylabel("Pravděpodobnost")
        save_to = filename.split('//')[2]
        save_to = save_to.split('.')[0]
        plt.savefig(save_to + "_char_prob.png", dpi=350)

char_prob(folder+xxx)
char_prob(folder+yyy)

