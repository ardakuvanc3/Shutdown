# Otomatik Kapatma Uygulaması

Bu proje, belirli bir süre sonra bilgisayarınızı otomatik olarak kapatmanızı sağlayan bir Python uygulamasıdır. Uygulama, kullanıcının belirttiği saniye cinsinden süreyi alır ve bu süre sonunda bilgisayarı kapatır. Ayrıca, verilen kapatma komutunu iptal etme seçeneği de sunar.

## Özellikler

- **Süre Belirleme:** Kullanıcı, bilgisayarın ne kadar süre sonra kapatılacağını saniye cinsinden belirleyebilir.
- **Kapatma İşlemi:** Belirlenen süre sonunda bilgisayar otomatik olarak kapanır.
- **Kapatma İptali:** Kullanıcı, kapatma komutunu iptal edebilir.

## Gereksinimler

Bu uygulamayı çalıştırmak için aşağıdaki Python kütüphanelerine ihtiyacınız olacak:

- `customtkinter`
- `tkinter`
- `os`

## Kurulum

1. Projeyi yerel makinenize klonlayın:

    ```bash
    git clone https://github.com/kullaniciadi/otomatik-kapatma.git
    ```

2. Gerekli Python paketlerini yükleyin:

    ```bash
    pip install customtkinter
    ```

3. Uygulamayı çalıştırmak için aşağıdaki komutu kullanın:

    ```bash
    python otomatik_kapatma.py
    ```

## Kullanım

1. Uygulama açıldığında, "Süre (saniye)" alanına bilgisayarın ne kadar süre sonra kapanacağını saniye cinsinden girin.
2. "Kapat" butonuna tıklayarak kapatma emrini verin.
3. Eğer kapatma işlemini iptal etmek isterseniz, "İptal" butonuna tıklayın.

## Ekran Görüntüleri

![Uygulama Ekran Görüntüsü](screenshot.png)

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.
