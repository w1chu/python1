inputString = str(input("напишіть будь-яке речення англійською: "))

a = "a"
A = "A"
e = "e"
E = "E"
o = "o"
O = "O"
u = "u"
U = "U"
i = "i"
I = "I"

acount = 0
ecount = 0
ocount = 0
ucount = 0
icount = 0

if A or a in str:
     acount = acount + 1

if E or e in str:
     ecount = ecount + 1

if o or O in str:
     ocount = ocount + 1

if u or U in str:
     ucount = ucount + 1

if I or i in str:
    icount = icount + 1

print(acount, ecount, ocount, ucount, icount)