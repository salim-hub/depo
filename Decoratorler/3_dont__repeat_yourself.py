# Fonksiyonun içinde tekrar eden kod blokları varsa onları bir iç fonksiyon haline getirerek hem okunabilirliği
# artırmış hem de DRY prensibine uymuş olursunuz.
# Örnekte kullanmak üzere bir User sınıfı oluşturalım. Bu sınıfta kullanıcı adı için name, aktif kullanıcı olup 
# olmadığını tutmak üzere is_active ve izinlerin listesini tutmak üzere permissions özellikleri olsun.

class User(object):
    is_active = True

    def __init__(self, name, permissions):
        """
        :param name: string
        :param permissions: list
        """
        self.name = name
        self.permissions = permissions

# Şimdi, bir User nesnesinin özelliklerinin doğru veri tiplerine sahip olup olmadığını test eden bir fonksiyon yazalım.

    def validate_user(user):
        def check(value, necessary_type):
            if type(value) == necessary_type:
                print("- {value}'s type is OK".format(value=value))
            else:
                raise TypeError("{value}'s type should be {type}.".format(
                    value=value,
                    type=necessary_type
                ))

        check(user.name, str)
        check(user.is_active, bool)
        check(user.permissions, list)
        for permission in user.permissions:
            check(permission, str)

# Parametre olarak verilen değerin, yine parametre olarak verilen veri tipine sahip olup olmadığını kontrol
# eden bir check iç fonksiyonu var. Bu fonksiyonda eğer veri tipi geçerliyse ekrana bir bilgi satırı yazdırıyor,
# eğer geçerli değilse bir TypeError fırlatarak durumu bildiriyoruz.

        user = User('umutcoskun', ['can_view_dashboard'])
        validate_user(user)

# Eğer iç içe fonksiyon kullanmasaydık, check fonksiyonunu dışarı yazıp kalabalık oluşturacaktık.
# Ya da sınıfın kontrol etmek istediğimiz her özelliği için bilgi satırı yazdırma ve hata fırlatma işlemlerini tekrarlayacaktık.
# Fonksiyonu artık silebilirsiniz, ancak User sınıfını saklayın aşağıda tekrar lazım olacak.
