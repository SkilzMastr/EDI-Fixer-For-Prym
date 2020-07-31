import os
from time import sleep

DIR = os.getcwd() 
LIST = os.listdir(fr'{DIR}\filesIncorrect')
DIR_INCORRECT = fr'{DIR}\filesIncorrect'
DIR_CORRECT = fr'{DIR}\filesCorrect'

for files in LIST:
    fin = open(fr'{DIR_INCORRECT}\{files}', "rt")
    fout = open(fr'{DIR_CORRECT}\{files}', "wt")

    for line in fin:
        fout.write(line.replace('*>*', '*:*'))
    fin.close()
    fout.close()


print('DO NOT RUN AGAIN THE PROGRAM WORKED. CORRECT FILES ARE IN filesCorrect.')
sleep(30)
