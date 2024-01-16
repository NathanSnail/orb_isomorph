with open("D:/Steam/steamapps/common/Noita/noita.exe", "rb") as f:
    txt = f.read()

#src = "data/entities/items/orbs/orb_13.xml"
#src = "data/entities/items/orbs/orb_11.xml"[::2]
#src = "[__34_orb_end_credits]"
src = "data/weather_gfx/background_cave_02.png"
#src = "void_liquid"
m = {}
pattern = []
idx = 0
for c in src:
    if c in m.keys():
        pattern.append(m[c])
    else:
        pattern.append(idx)
        m[c] = idx
        idx += 1
l = len(pattern)
print(pattern)

def matches(src, alpha, off):
    o = 0
    bl = len(src)
    while o < bl - l:
        sub = src[o:o+l]
        nm = {}
        seen = set()
        good = True
        for k, v in enumerate(pattern):
            if v in nm.keys():
                if nm[v] != sub[k]:
                    good = False
                    break
            else:
                if sub[k] in seen:
                    good = False
                    break
                seen.add(sub[k])
                nm[v] = sub[k]
        if good:
            print(alpha, off, o, sub, txt[o*off+alpha:(o+l)*off+alpha])
        o += 1


for off in range(1, 100):
    print(off)
    for alpha in range(off):
        sl = txt[alpha::off]
        matches(sl, alpha, off)
