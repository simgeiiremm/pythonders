#region Soru 1-)Python'da Veri Tiplerini araştırınız, 
#her bir veri tipi için kendi cümlelerinizle açıklamalar yazınız.
## 1-) String (metin) veri tipleri => str => Metinsel veri tipleri string veri tipi olarak tanımlanır.
#Tek ve çift tırnak kullanılarak bir karakter kümesi oluşturulur.

print()
str = "Kodlama.io"
str1 = "Python dersinin 1. ödevi"
print(str)
print(str1)

## 2-) Numerik (sayısal) veri tipleri => int, float, complex ==> Sayı nesneleri, onlara bir değer atadığınızda oluşturulur.
#int : sınırsız uzaklıktaki işaretli tamsayıları tutar. Örn. 1,2,3.. vs 
#float : Değişken ondalık sayıları tutar. Örn. 1.024, 1.25 vs.
#complex : karmaşık sayıları tutar. Örn. 3+6j

#integer değerle ilgili bir örnek aşağıdadır.
num1 = 25
print(num1, "bir tamsayidir.", type(num1))

#float değerle ilgili bir örnek aşağıdadır.

num2 = 3.1415
print(num2, "bir odalik sayidir", type(num2))

#complex değerle ilgili bir örnek aşağıdadır.

num3 = 3 + 6j
print(num3, "bir karmasik sayidir.", type(num3))


## 3-) Sequence (sıralama) veri tipleri => list, tuple, range 
#=> Çok yönlü bleşik veri türleridir. Ögeler köşeli parantez içerisine virgülle ayrılarak kullanılır.

list = ["Ayşe", "Fatma", 25, 10.9, 'Simge']
print(list)

#tuple, listeye benzeyen başka bir dizi veri türüdür. Listeden farklı olarak ögeler parantez içine alınır ve değiştirilemez.
tuple = ("Ayşe", "Fatma", 25, 10.9, 'Simge')
print(tuple)

#range, 0'dan başlayıp belirli bir sayıya ulaşana kadar artan bir sayı dizisi döndüren yerleşik bir veri tipidir.
#bir sayı dizisi oluştururken for ve while döngüsüyle birlikte range işlevini de kullanabiliriz.

for i in range(3):
    print(i)

## 4-) Mapping (haritalama) veri tipleri => dict
#İçerisinde yer alan veriler anahtar ve bu anahtarların karşılığına gelen değerler olarak tutulur. Python dilinde dictionary olarak bilinen bu veri tipinde küme parantez içerisine tanımlamalar kullanılır ve değer atamaları köşeli parantezler ile yazılır. 

pythonDict = {}
pythonDict ['fullName'] = "Simge İrem Işık"
pythonDict ['eMail'] = "simge@gmail.com" 
pythonDict ['password'] = 12345
print(pythonDict)

## 5-) Set veri tipleri => set, frozenset 
#Set : Liste, sözlük ve demet veri türü gibi birden çok veri türünün birlikte kullanıldığı veri tipidir. Kümeler ile ilgili her işlev bu veri tipiyle yazılabilir.
#Frozenset : Set ile kullanımı aynıdır fakat frozenset de kümeler içerisinde değişiklik yapılamaz.

set = {"Full Name", "EMail", 12345, 'a', 3.1415, "Full Name"}
print(set)

#Boolean / bool veri tipleri => bool => Girilen ifade doğru ise true, yanlış ise false döndürür.

sayi1 = 5
sayi2 = 7
print(bool(sayi1 == sayi2))

print()
#endregion



#region Soru 2) Kodlama.io sitesinde değişken olarak kullanıldığını düşündüğünüz verileri, 
#veri tipleriyle birlikte örneklendiriniz.

#Kurslarım, Tüm Kurslar, Kariyer, Sık Sorulan Sorular string veri tipine örnektir.
#Kategori, Eğitmen list veri tipine örnektir.
#Profil kısmı list veri tipine örnektir.
#Profil sayfasında bulunan,
    #Full Name, Email, password  => string
     
#Kart Bilgisi ekle veya değiştir sayfasında bulunan,
    #Name on Card => string
    #Kart Numarası, CVC kodu, Posta Kodu => integer
    #Ülke => list
#endregion

#region Soru 3) Kodlama.io sitesinde şart blokları kullanıldığını düşündüğünüz kısımları örneklendiriniz 
# ve Python dilinde bu örnekleri koda dökünüz.

   
mail = "simge@gmail.com"
password = 12345

while True:
    kullanici_mail = input("Email adresi giriniz:")
    kullanici_password = input("Şifrenizi giriniz:")
    # ikisi de doğru ise
    if kullanici_mail == mail and kullanici_password == password:
        print("Giriş başarili")
        break
    # kullanıcı adı doğru şifre yanlış ise
    elif kullanici_mail == mail and kullanici_password != password:
        print("Yanliş şifre girdiniz.\n")
    # şifre doğru kullacı adı yanlış
    elif kullanici_mail != mail and kullanici_password == password:
        print("Mail adresiniz geçersizdir.\n")
    # ikisi de yanlış ise
    else:
        print("Kullanici mail adresiniz ve sifreniz gecersizdir.\n")

#endregion





