def extra(fonk):
    def wrapper(sayılar):
        ciftler_toplamı = 0
        cift_sayılar = 0
        tekler_toplamı = 0
        tek_sayılar = 0

        for sayı in sayılar:
            if (sayı % 2 == 0):
                ciftler_toplamı += sayı
                cift_sayılar += 1
            else:
                tekler_toplamı += sayı
                tek_sayılar += 1

        print("Teklerin Ortalaması: ", tekler_toplamı/tek_sayılar)
        print("Çiftlerin Ortalaması: ", ciftler_toplamı/cift_sayılar)

        fonk(sayılar)
    return wrapper

@extra
def ortalama_bul(sayılar):

    toplam = 0

    for sayı in sayılar:
        toplam += sayı

    print("Genel ortalama: ", toplam/len(sayılar))


ortalama_bul([1,2,3,4,34,60,63,32,100,105])