# Bir öğrenci kayıt sistemi yazdığımızı düşünelim. Sistemimizdeki öğrencileri bir listede sadece ad soyad olacak şekilde tutalım.

# Bu öğrenci kayıt sistemine;

# Aldığı isim soy isim ile listeye öğrenci ekleyen
# Aldığı isim soy isim ile eşleşen değeri listeden kaldıran
# Listeye birden fazla öğrenci eklemeyi mümkün kılan
# Listedeki tüm öğrencileri tek tek ekrana yazdıran
# Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
# Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)
# fonksiyonları geliştiriniz ve her bir fonksiyonu en az bir kere çağırarak konsolda test ediniz.

# Ödevde kullanacağınız döngülerin bir tanesi for bir tanesi while döngüsü olması istenmektedir.


print("Öğrenci Kayit Sistemi")
ogrenciler = ["Simge İsik", "Damla İsik", "Melikhan Yilmaz"]
print(ogrenciler)

def ogrencilerEkle(adiSoyadi):
    ogrenciler.append(adiSoyadi)


def listOgrenci():
    for i in range(len(ogrenciler)):
        print(ogrenciler[i])
        print("*****")

def ogrenciSilme(adiSoyadi):
    for ogrenci in ogrenciler:
        if ogrenci == adiSoyadi:
             ogrenciler.remove(ogrenci)
             print(ogrenciler)    
        else:
            print("Girdiginiz Ad-Soyad ile eşleyen bir ögrenci bulunamadi!!")



def ogrenciNumarasi(adiSoyadi):
    return ogrenciler.index(adiSoyadi)

def ogrencileriSilme():
    while True:
        ogrenci = int(input("Silmek istediğiniz ögrencinin numarasini giriniz:"))
        ogrenciler.pop(ogrenci)
        listOgrenci()


while True:
    print("1. Listeye ögrenci ekle")
    print("2. Listeden ögrenciyi sil")
    print("3. Listeye birden fazla ögrenci ekle")
    print("4. Listedeki ögrencileri yazdir")
    print("5. Girilen ögrencinin numarasini yazdir")
    print("6. Listede birden fazla ögrenciyi sil")
    secim = (input("1-6 arasinda bir numara seciniz : "))
    if secim == "1":        
        adiSoyadi = input("Eklemek istediğiniz kişinin Adi-Soyadini giriniz :")
        ogrencilerEkle(adiSoyadi)
        print("Kayit basarili!!")

    elif secim == "2":
        adiSoyadi = input("Listeden sileceginiz ögrencinin Adi-Soyadini yaziniz: ")
        ogrenciSilme(adiSoyadi)
       

    elif secim == "3":
        ogrenciEkle = int(input("Eklenecek ögrenci sayisini yaziniz: "))
        for i in range(ogrenciEkle):
            adiSoyadi = input("Listeye ekleyeceginiz ogrencilerin Adi-Soyadini giriniz: ")
            ogrencilerEkle(adiSoyadi)
            print("Ogrenciler basariyla eklenmistir.")

    elif secim == "4":
        listOgrenci()

    elif secim == "5":
        ogrenciNumarasi(adiSoyadi)

    elif secim == "6":
            sil = int(input("Silinecek ogrenci sayisini giriniz: "))
            for i in range(sil):
                ogrenciSilme(adiSoyadi)
    else:
        listOgrenci()
        continue        
        
        




        


                    











