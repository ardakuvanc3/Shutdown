import customtkinter as ctk

# Tkinter pencere oluşturulması
pencere = ctk.CTk()
pencere.title("Otomatik Kapatma")
pencere.geometry("400x300")
ctk.set_appearance_mode("dark")
pencere.resizable(False, False)  # Pencereyi yeniden boyutlandırmayı devre dışı bırakma

# Başlık
baslik = ctk.CTkLabel(pencere, text="Otomatik Kapatma", font=("Arial", 18))
baslik.pack(pady=20)

# Süre etiket ve giriş
etiket = ctk.CTkLabel(pencere, text="Süre (saniye):", font=("Arial", 14))
etiket.pack(pady=10)

time_input = ctk.CTkEntry(pencere, placeholder_text="Giriş yapınız", width=200)
time_input.pack(pady=10)

# Kapatma emrinin verilip verilmediğini takip etmek için bir değişken
kapatma_emri_verildi = False

def shutdown():
    global kapatma_emri_verildi
    süre = time_input.get()  # Kullanıcının girdiği süreyi al
    if süre.isdigit():  # Girişin bir sayı olup olmadığını kontrol et
        import os  # Lazy loading: os modülünü sadece burada yüklüyoruz
        os.system(f"shutdown -s -f -t {süre}")
        kapatma_emri_verildi = True
    else:
        import tkinter.messagebox as messagebox  # Lazy loading: tkinter.messagebox sadece burada yüklüyoruz
        messagebox.showwarning("Uyarı", "Lütfen geçerli bir sayı girin.")

def iptal():
    global kapatma_emri_verildi
    if kapatma_emri_verildi:
        import os  # Lazy loading: os modülünü sadece burada yüklüyoruz
        os.system("shutdown -a")
        kapatma_emri_verildi = False
    else:
        import tkinter.messagebox as messagebox  # Lazy loading: tkinter.messagebox sadece burada yüklüyoruz
        messagebox.showinfo("Uyarı", "Kapatma emri verilmedi!")

# Butonlar
ok_button = ctk.CTkButton(pencere, text="Kapat", command=shutdown, width=120)
ok_button.pack(pady=10)

iptal_button = ctk.CTkButton(pencere, text="İptal", command=iptal, width=120)
iptal_button.pack(pady=10)

# Pencerenin çalıştırılması
pencere.mainloop()
