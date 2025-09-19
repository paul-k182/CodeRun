# 67. Симметричная последовательность
# https://coderun.yandex.ru/problem/symmetric-sequence/description

from sys import stdin
Yes = True
No = False
N = int(input())
a = [int(i) for i in input().split()]
mid = (N + 1) // 2
sym = No
s = ''
for k in a:
    s += str(k)
while not sym and mid <= N-1:
    su = s[ :mid-1 :-1]
    l = len(su)
    sb = s[mid-l-1 :mid-1]
    sh = s[mid-l :mid-1]
    s[mid-l-1 :mid-1]
    if sb == su:
        sym = Yes
        ss = s[0 :mid - l-1]
    elif sh + s[mid -1] == su:
        sym = Yes
        ss = s[0 :mid - l]
    mid += 1
if not sym:
    ss = s[0 :-1]
sa = ss[:: -1]
print(len(sa))
sa = " ".join(sa)
print(sa)