import matplotlib.pyplot as plt
from math import log
import numpy as np
from collections import defaultdict
from termcolor import colored
import pandas as pd
import os
from scipy.stats import chi2_contingency
from scipy.stats import ttest_ind

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


def task_1(filename, word_lengths, word_lengths_dic):
    print(colored("File {} - mean: {}; variance: {}".format(filename, np.mean(word_lengths), np.var(word_lengths)),
    'green'))
    df1 = pd.DataFrame.from_dict(word_lengths_dic, orient='index', columns=['cnt']).sort_index()
    plot = df1.plot.bar(y='cnt', rot=0)
    plot.set_xlabel('Délka slova')
    plot.set_ylabel('Počet')
    plot.get_legend().remove()
    plot.get_figure().savefig("hw2_plot1_{}.pdf".format(filename))


def task_3(word_dic_1, word_dic_2):
   df1 = pd.DataFrame.from_dict(word_dic_1, orient='index', columns=['cnt']).sort_index()
   df2 = pd.DataFrame.from_dict(word_dic_2, orient='index', columns=['cnt']).sort_index()

   arr = [df1['cnt'], df2['cnt']]

   print(arr)

   chi2, p, dof, ex = chi2_contingency(arr)
   print (colored(f'chi2={chi2}, p-val={p}', 'green'))

def task_4(words_1, words_2):
   t, p = ttest_ind(words_1,words_2, equal_var = False)
   print (colored(f'test value={t}, p-val={p}', 'green'))


def process_file(filename, chars, word_lengths, word_lengths_dic):
    
    basename = os.path.basename(filename)
    with open(filename, "r") as f:
        next(f) #skip the first line of the input
        for line in f:
            for word in line.split():
                word_lengths.append(len(word))
                word_lengths_dic[len(word)] += 1
                for c in word:
                    chars[c] += 1


        task_1(basename, word_lengths, word_lengths_dic)
        
        #task_2 is already done in hw1


if __name__ == "__main__":

    print([K, L, X, Y])



    chars_1 = defaultdict(lambda: 0)
    word_lengths_1 = []
    word_lengths_dic_1 = defaultdict(lambda: 0)
    process_file(folder+yyy, chars_1, word_lengths_1, word_lengths_dic_1)
    
    chars_2 = defaultdict(lambda: 0)
    word_lengths_2 = []
    word_lengths_dic_2 = defaultdict(lambda: 0)
    process_file(folder+xxx, chars_2, word_lengths_2, word_lengths_dic_2)
    word_lengths_dic_2[14] = 0


    task_3(word_lengths_dic_1, word_lengths_dic_2)
    task_4(word_lengths_1, word_lengths_2)

    
    for c in chars_1:
        if c not in chars_2:
            chars_2[c] = 0

    for c in chars_2:
        if c not in chars_1:
            chars_1[c] = 0

    task_3(chars_1, chars_2)



