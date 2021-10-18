# Dekoratörler, temelde alınan parametreyi iç fonksiyona (wrapper) gönderen
# ve geriye de bu fonksiyonu döndüren fonksiyonlardır. İç fonksiyonları dekoratör 
# yazmadığınız durumlarda da kullanabilirsiniz.

# Kapsülleme (Encapsulation)
# Yazdığınız fonksiyonları, dışarıdan gelecek bir müdahaleden korumak için kullanabilirsiniz. 
# Herhangi bir iç fonksiyon global alandan erişilemeyecektir.

def factorial(n: int):
    assert type(n) == int
    assert n >= 0

    def fact(n):
        if n <= 1:
            return 1
        return n * fact(n - 1)

    return fact(n)

print(factorial(4))

# Yukarıda parametre olarak verilen sayının faktoriyelini alan bir fonksiyon var. Verilen parametre 
# iç fonksiyon ile 1 olana kadar azaltılarak, her adımda kendisi (n) ve kendisinin bir eksiği (n — 1)
# ile çarpılıyor. Hemen üzerinde ise parametrenin tam sayı olduğu ve sıfırdan yüksek olduğundan emin olunuyor.
# Tabii normalde bu kontrolleri assert kullanmak yerine exception fırlatarak yapmanızı öneririm.