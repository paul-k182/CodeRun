# 5313. Ча-ча-ча
# https://coderun.yandex.ru/problem/cha_cha/description?compiler=pypy

import sys

def main():
    pass

if __name__ == '__main__':
    main()

# инициализация
ABC = {'A':25, 'B':24, 'C':23, 'D':22, 'E':21, 'F':20, 'G':19, 'H':18, 'I':17, 'J':16, 'K':15, 'L':14, \
     'M':13, 'N':12, 'O':11, 'P':10, 'Q':9, 'R':8, 'S':7, 'T':6, 'U':5, 'V':4, 'W':3, 'X':2, 'Y':1, 'Z':0}
amount = 0
worst = ABC['A']

s = input() # Ввод данных
for i in range(len(s)):
    si = ABC[s[i]]
    amount = amount + si
    worst = min(worst, si)
#average = int(amount / len(s) + 0.5)
m = min(worst + 1, int(amount / len(s) + 0.5))

for key in ABC:
    if ABC[key] == m:
        print(key)
        break