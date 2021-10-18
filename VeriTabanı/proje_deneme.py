from kütüphane import *

print("""************************************************

Kütüphane Programına Hoşgeldiniz.

İşlemler:

1. Kitapları Göster

2. Kitap Sorgulama

3. Kitap Ekle

4. Kitap Sil

5. Baskı Yükselt

Çıkmak için 'q' ya basınızz

************************************************""")


kütüphane = Kütüphane()

while True:
    islem = input("Yapacağınız işlem: ")

    if (islem == "q" or islem =="Q"):
        print("Program Sonlandırılıyor")
        print("Yine Bekleriz...")
        break

    elif (islem == "1"):
        kütüphane.kitapları_goster()

    elif (islem == "2"):
        isim = input("Hangi kitabı istiyorsunuz?: ")
        print("Kitap Sorgulanıyor.....")
        time.sleep(2)

        kütüphane.kitap_sorgula(isim)

    elif (islem == "3"):
        isim = input("Kitabın İsmi: ")
        yazar = input("Yazar: ")
        yayınevi = input("Yayınevi: ")
        tür = input("Tür: ")
        baskı = int(input("Baskı: "))
        
        yeni_kitap = Kitap(isim, yazar, yayınevi, tür, baskı)
        print("Kitap Ekleniyor....")

        time.sleep(3)
        kütüphane.kitap_ekle(yeni_kitap)

        print("Kitap Eklendi!..")

    elif (islem == "4"):
        isim = input("Hangi Kitabı Silmek İstiyorsunuz?: ")

        cevap = input("Emin misiniz ? (E/H)")

        if cevap == "E":
            print("Kitap Siliniyor.....")
            time.sleep(3)
            kütüphane.kitap_sil(isim)
            print("Kitap Silindi!...")

    elif (islem == "5"):
        isim = input("Hangi Kitabın Baskısını Yükseltmek İstiyorsunuz?: ")
        print("Baskı Yükseltiliyor....")
        time.sleep(3)
        kütüphane.baskı_yukselt(isim)
        print("Baskı Yükseltildi!...")

    else:
        print("Geçersiz İşlem!.....")





























