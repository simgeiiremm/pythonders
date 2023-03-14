print("Kodlama.io")
baslik = "Taşıt Kredisi"
print(baslik)
#string => metinsel ifade
baslik = "İhtiyaç Kredisi"
print(baslik)

vade = 36
ekVade = 6
vade2 = "36"

aylikOdeme = 200.5

#bool, boolean => True veya false
yukselisteMi = True

#matematiksel operatörler

print(5 + 5)
print(vade + 12)
print(vade + ekVade)
print(36 + 6)

# -
print(5-5)
print(vade-ekVade)


# *
print(5*5)
print(vade*2)
print(vade*ekVade)
print(10*10)


# /
print(5/5)
print(vade/2)
print(vade/ekVade)
print(10/2)

yeniVade = vade / 2
fiyat = 100
indirimFiyat = fiyat - 20

print(yeniVade)
print(indirimFiyat)

# % => mod operator
print(10%2)
print(vade % 5)
print(30 % 10)

# mantıksal operatörler
print(1 == 1)
print(1 == 2)

# CTRL K CTRL C 
# print(1 > 2)
# print(3 > 1)
# print(1 > 1)
# print(1 >= 1)

print(1 < 2)
print(3 < 1)
print(1 <= 1)

print(1 != 1)
print(1 != 2)

# or and

#or => veya
print(1 > 2 or 5 > 2)
print(1 > 2 and 5 > 2)
print(1 > 2 or 5 > 2 and 3 > 2)

print(1 > 2 and 5 > 2 and 3 > 2)

print(2 > 1 or 1 > 2 and 3 > 2)

#karar yapıları
# if elif else

sayi1 = 20
sayi2 = 15
#sayi1 sayi2 den büyük ise ekrana sayi 1 daha büyük yazdır

if sayi1 < sayi2:
   print("Sayi1 Sayi2'den daha küçüktür.")
elif sayi1 == sayi2:
    print("İki sayı eşittir.")
else:
    print("Sayi 1 Sayi 2 den büyüktür.")

print("Burası if bloğunun dışındadır")