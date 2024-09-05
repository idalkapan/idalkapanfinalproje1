def yeni_katilimci():   #yeni katılımcılar fonksiyonuoluşturduk.
    kayitDosyasi = "MuhendisFest2024-Katılımcılar.txt" #kayitDosyası tırnak içindeki değişkene atandı.
    
    try:   #bloğu hatalara karşı denetler.
        with open(kayitDosyasi, "a+") as dosya:   #dosya açıldı.
            katilimci_id_listesi = [] #id listesi oluşturduk.
            dosya.seek(0) #dosya imleci dosyanın başına getirilirokuma işlemini en baştan yapmak
            for satir in dosya:  #dosyanın her bir satırı okunur.
                id, _, _, _ = satir.strip().split(",")  #sadece id kısmı alınır. diğer kısımlar atılır.satir.strip()satırın başındaki ve sonundaki boşlukları, geçersiz karakterleri kaldırır.split(",")Virgüle göre satırı böler ve parçalara ayırır.
                katilimci_id_listesi.append(id) #girilen id katilimci_id_listesi ne eklenir.
            
            while True:
                katilimci_id = input("Katılımcı ID: ") #kullanıcıdan katılımcının idsi istenir.

                if katilimci_id in katilimci_id_listesi: #eğer girilen id katilimci_id_listesinde varsa bu kısım çalışır.
                    print("Bu ID zaten kullanılmış. Farklı bir ID seçin.") #ekrana başka id seçmesi ile ilgili bilgilendirmesi yapılır.
                else:    #değilse alt taraf çalışır.
                    break
                
            katilimci_ad = input("Katılımcı Adı: ")  #kullanıcıdan adı istenir.
            katilimci_soyad = input("Katılımcı Soyadı: ")  #kullanıcıdansoyadı istenir.

            while True:
                try:
                    katilimci_dogum_ayi = int(input("Katılımcı Doğum Ayı (1-12): ")) #kullanıcıdandoğum ayıistenir.(1-12 arasında)
                    if katilimci_dogum_ayi < 1 or katilimci_dogum_ayi > 12: #eğer girilen değer 1ve 12 dahil bu aralıkta değilse bu kısım çalşır.
                        raise ValueError  
                    break
                except ValueError:
                    print("Geçersiz doğum ayı. 1 ile 12 arası değer giriniz.") # geçersiz değer girdiği,1 ile 12 arası değer girmesi istenir.

            dosya.write(f"{katilimci_id},{katilimci_ad},{katilimci_soyad},{katilimci_dogum_ayi}\n") #dosyaya katilimci id,ad,soyad,doğum ayı yazılır.
            
            print("Yeni katılımcı başarıyla eklendi.") #katılımcının başarıyla eklendiği ekrana yazılır.

    except FileNotFoundError: #dosya kontrolü yapılır.
        print(f"{kayitDosyasi} dosyası bulunamadı.") #kayıtdosyasi yoksa dosyanın bulunamadığı yazar.
    except Exception as hata: #genel hata olup olmadığına bakılır.
        print("Bir hata oluştu:", hata) #hata varsa ekrana yazılır.


def katilimci_getir():
    dosya_adi = "MuhendisFest2024-Katılımcılar.txt"
    
    try:
        katilimci_id = input("Görmekistediğiniz katılımcının ID'si: ")

        with open(dosya_adi, "r") as dosya:
            for satir in dosya:   
                id, ad, soyad, dogum_ayi = satir.strip().split(",")
                if id == katilimci_id:      #girilen id katılımcı idsine eşit mi bakılır.
                    print(f"Katılımcı Adı: {ad}")
                    print(f"Katılımcı Soyadı: {soyad}")
                    print(f"Katılımcı Doğum Ayı: {dogum_ayi}")
                    break
            else:   #eşit değilse bu kısım çalışır.
                print("Girilen ID'ye sahip katılımcı bulunamadı.")

    except FileNotFoundError:      #dosya kontrolü yapılır.
        print(f"{dosya_adi} dosyası bulunamadı.")    #kayıtdosyasi yoksa dosyanın bulunmadığı yazar.
    except Exception as hata:     #genel hata kontrolü yapılır.
        print("Bir hata oluştu:", hata)  





def girisKodu_sifre_uret(): #girisKodu_sifre_uret() fonksiyonu oluşturduk.
    katilimci_bilgileri = input("Katılımcının bilgilerini (Ad, Soyad, ID, Doğum Ayı): ").lower().split(", ") #kullanıcıdan katılımcı bilgieri istenir.
    katilimci_ad, katilimci_soyad, katilimci_id, katilimci_dogum_ayi = katilimci_bilgileri      #katılıcı bilgileri değişkeninden gelnler bunlara atanır.
    
    # Giriş kodu oluşturma adımları
    adim1 = f"{katilimci_ad[0]}{katilimci_soyad[-1]}" #katılımcı adının ilk karakteri soyadın son karakteri alınır.
    adim2 = str(int(katilimci_id) * int(katilimci_dogum_ayi))#değerler inte çevrilip çarpılıyor. sonra stringe dönüştürülüyor.
    adim3 = adim1 + adim2 #adım1'e adım2 eklenir.
    guvenlik_sifre = adim3[::-1]  # Adım3'ü ters çevirerek gecici  güvenlik sifresi oluşturur.

    with open("girisKodu_sifre.txt", "a") as dosya: #girisKodu_sifre.txt dosyası açar.
        dosya.write(f"{katilimci_id}, {adim3}, {guvenlik_sifre}\n") # dosyaya  katılımcı idsi, adım3(adım1+adıım2) ve güvenlik şifresi yazılır.

    print(f"Oluşturulan Giriş Kodu: {adim3}") #oluşturulan giriş kodu ekrana yazılır.
    print(f"Oluşturulan Güvenlik Şifresi: {guvenlik_sifre}") #oluşturulan güvenlik şifresi ekrana yazılır.

