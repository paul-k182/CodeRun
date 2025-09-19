# 439. Пара букв
# https://coderun.yandex.ru/problem/couple-of-letters/description

def main():
    
    pass

if __name__ == '__main__':
    main()

s = input()
slv = {}
for i in range(len(s)-1):
    if s[i] != ' ' and s[i+1] != ' ':
        ab = s[i] + s[i+1]
        if ab in slv:
            slv[ab] = slv[ab] + 1
        else:
            slv[ab] = 1
lxm = ab
mx = slv[ab]
slv1 = dict(sorted(slv.items()))
for k, j in slv1.items():
    if j >= mx:
        lxm = k
        mx = j
print (lxm)