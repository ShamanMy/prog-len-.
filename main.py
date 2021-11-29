def lenkuParbaude(len1,len2,len3):
  rezultats = False
  if len1+len2+len3==180:
    rezultats = True
  return rezultats

len1 = int(input("Ievādi 1. lenķi"))
len2 = int(input("Ievādi 2. lenķi"))
len3 = int(input("Ievādi 3. lenķi"))
rez = lenkuParbaude(len1,len2,len3)
if rez:
  print("Trijsturis eksistē!")
else:
  print("Trijsturis neeksistē!")