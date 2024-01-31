
with open("D:/Steam/steamapps/common/Noita/noita.exe", "rb") as f:
    txt = f.read()

#src = "data/entities/items/orbs/orb_13.xml"
#src = b"data/entities/items/orbs/orb_11.xml"[1::2]
#src = "[__34_orb_end_credits]"
#src = "data/weather_gfx/background_cave_02.png"
src = b"void_liquid"
src = b"a2332a"
src = b"830000"
for off in range(1, 1000):
    print(off)
    for alpha in range(off):
        sl = txt[alpha::off]
        f = sl.find(src)
        if f != -1:
            print(alpha, off, f, sl[f:f+len(src)], txt[f*off+alpha:(f+len(src))*off+alpha])