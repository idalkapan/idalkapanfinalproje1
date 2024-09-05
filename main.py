import islemler  #işlemler modülü eklenir.

def menu_goruntule():   #fonksiyon oluşturduk.
    print("1. Yeni katılımcı eklemek")
    print("2. Kayıtlı katılımcı bilgilerini görmek")
    print("3. Giriş kodu ve şifre oluşturmak")
    print("4. Çıkış yap")                          #ekrana yazıldı.

def main():   #main ana fonksiyonumuzu oluşturduk.
    while True:
        menu_goruntule()     #menu_goruntule() fonksiyonu buraya çağırılır.
        secim = input("İşlem seçin (1/2/3/4): ")  #kullanıcıdan yapmak istediği seçim alınır.

        if secim == "1":             # 1'e eşitse bu kısım çalışır.
            islemler.yeni_katilimci()  #islemlere giderek oradaki yeni_katılımcı() fonksiyonu çalıştırılır.
        elif secim == "2":         #seçimi 2'ye eşitse bu kısım çalışır.
            islemler.katilimci_getir()  #islemlere giderek oradaki katılımcı_getir() fonksiyonu çalıştırılır.
        elif secim == "3":              #seçimi 3'e eşitse bu kısım çalışır.
            islemler.girisKodu_sifre_uret()   #islemlere giderek oradaki girisKodu_sifre_uret() fonksiyonu çalıştırılır.
        elif secim == "4":               #seçimi 4'e eşitse bu kısım çalışır.
            print("Programdan çıkılıyor!!!")  #programdan çıkılıyor yazılır ve program sonlanır.
            break
        else:       #eğer kullanıcı seçimi istenilenlerden farklı ise bu kısım çalışır.
            print("Geçersiz seçim. Lütfen 1ile 4 arası seçim yapın.") #ekrana geçersiz işlem bilgisi verilir ve sorular tekrar sorulur.

if __name__ == "__main__":   #programın ana bloğu.
    main()
