n = input()
s = [int(v) for v in input().split()[::-1]]
m = [int(v) for v in input().split()[::-1]]

while len(s) > 0 and len(m) > 0:
    sc = s.pop()
    mc = m.pop()
    if sc > mc:
        s.insert(0, sc)
    elif mc > sc:
        m.insert(0, mc)

if len(m) > 0:
    print('G')
elif len(s) > 0:
    print('P')
else:
    print('N')
