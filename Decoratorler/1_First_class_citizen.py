# Dinamik olarak oluşturulabilen, yok edilebilen, bir fonksiyona parametre olarak verilebilen
# ya da bir fonksiyondan sonuç değeri olarak döndürülebilen, değişkenlerle aynı haklara sakip 
# varlıklara birinci sınıf nesne ya da "birinci sınıf vatandaş(first-class citizen)" denir.

# Aşağıdaki örnekte, önce iki sayıyı toplayan add fonksiyonunu oluşturuyoruz. Ardından fonksiyonun
# kendisini ve ismini (__name__ özelliğinde tutulur), parametre verip çalıştırarak sonucunu ve veri
# tipini yazdırıyoruz. Sonra parametre olarak fonksiyon alan bir fonksiyon alıp, verilen diğer parametreleri
# bu fonksiyona göndererek çalıştırıp, sonucunu döndürüyoruz. Son olarak bu işlemin de sonucunu yazdırarak fonksiyonu hafızadan siliyoruz.

def add(x, y):
    return x + y

print('add: {}'.format(add))
print('add.__name__: {}'.format(add.__name__))
print('add(2, 3): {}'.format(add(2, 3)))
print('type(add): {}'.format(type(add)))


def call_function(func, *args):
    return func(*args)

print('call_function(add, 2, 3): {}'.format(call_function(add, 2, 3)))

del add