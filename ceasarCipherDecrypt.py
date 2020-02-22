
locations = ["arena", "forum", "hills", "river"]

for k in range(1, 26):
    c = list("evire")
    for i in range(0, len(c)):
        if(ord(c[i])-k < ord('a')):
            c[i] = chr((ord(c[i]) - k +26))
            continue
        c[i] = chr((ord(c[i])-k))
    if ("".join(c) in locations):
        print(str(k) + " is a possible key and results in " + "".join(c))
