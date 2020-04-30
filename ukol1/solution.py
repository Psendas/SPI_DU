import matplotlib.pyplot as plt
from math import log


# --------------------- File selection ----------------------------------------
K = 27 # den narození reprezentanta skupiny (1-31)
surname = "Pšenička"
L = len(surname) # počet písmen v příjmení reprezentanta
X = ((K*L*23) % (20)) + 1
Y = ((X + ((K*5 + L*7) % (19))) % (20)) + 1

folder = "..//hw1-source//"
xxx = str(str(X).zfill(3)) + ".txt"
yyy = str(str(Y).zfill(3)) + ".txt"
# -----------------------------------------------------------------------------

def entropy(prob):
    ent = 0
    for p in prob:
        ent += p * log(p, 2)
    ent *= -1
    return ent

def char_prob(filename):
    with open(filename, "r") as f:
        print(f'\nProcessing file {filename}')
        print("-----------------------------")
        chars = dict()
        char_count = 0
        for line in f:
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

        print("Char\t|  Probability")
        print("-----------------------------")
        sorted_chars = sorted(chars, key=chars.get, reverse=True)
        sorted_values = []
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

        huf_code(sorted_chars, sorted_values)

class Node:
    def __init__(self, char='', prob=0):
        self.left = None
        self.right = None 
        self.char = char
        self.prob = prob

def show_code(node, chars, h_code):
    if node.left != None:
        show_code(node.left, chars+"0", h_code)
    if node.right != None:
        show_code(node.right, chars+"1", h_code)
        
    if node.right == None and node.left == None:
        h_code[node.char] = chars
        return

def code_len(code, chars, probs):
    sum = 0
    for char, c in code.items():
        index = chars.index(char)
        sum += len(c) * probs[index]
    return sum

def huf_code(chars, probs):
    que = []
    for i in range(len(chars)):
        n = Node(chars[i], probs[i])
        que.append(n)

    while len(que) > 1:
        que = sorted(que, key=lambda node: node.prob)
        first = que.pop(0)
        second = que.pop(0)
        new_n = Node('', first.prob + second.prob)
        new_n.left = first
        new_n.right = second
        que.append(new_n)
    
    root = que[0]

    h_code = dict()
    show_code(root, "", h_code)
    sorted_code_chars = sorted(h_code, key=lambda k: h_code[k])
    sorted_code_chars = sorted(sorted_code_chars, key=lambda k: len(h_code[k]))

    for char in sorted_code_chars:
        print(char + " : " + h_code[char])

    c_len = code_len(h_code, chars, probs)
    print(f'Code len = {c_len}')

if __name__ == "__main__":

    char_prob(folder+xxx)
    char_prob(folder+yyy)


