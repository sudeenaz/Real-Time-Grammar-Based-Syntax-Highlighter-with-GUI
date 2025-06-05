# Gerçek Zamanlı Sözdizimi Vurgulayıcı (GUI Destekli)

Bu proje, kullanıcı tarafından girilen kodu gerçek zamanlı olarak analiz ederek sözdizimi öğelerini renklendiren bir uygulamadır. Tanımlı bir dil bilgisini (gramer) temel alarak çalışan lexer sayesinde kodun sözdizimsel öğeleri (anahtar kelimeler, sayılar, yorum satırları vb.) anlık olarak vurgulanır. Kullanıcı dostu bir grafik arayüz (GUI) ile desteklenmiştir.

---

## 📌 Proje Açıklaması

Bu araç, **Programlama Dilleri** dersi kapsamında dönem projesi olarak geliştirilmiştir. Projenin amacı, dilbilgisi tanımları ve sözcük analizine (lexer) dair teorik bilgileri gerçek zamanlı bir uygulama üzerinden pratiğe dökerek görsel hale getirmektir.

---

## 🚀 Özellikler

- ✅ Gerçek zamanlı sözdizimi vurgulama
- ✅ Gramer tabanlı token tanıma
- ✅ Anahtar kelime, sayı, string, yorum vb. için farklı renkler
- ✅ Kullanıcı dostu ve sezgisel arayüz
- ✅ Modüler ve geliştirilebilir yapı

---

## 🛠️ Kullanılan Teknolojiler

- **Python 3.x**
- **PyQt5** → Arayüz tasarımı için
- **Regex (Regular Expressions)** → Dilbilgisi kuralları için
- **Özel tanımlanmış gramer kuralları**

---

## 📁 Klasör Yapısı

syntax-highlighter/
├── gui/ # Arayüz dosyaları
│ └── main_window.py
├── lexer/ # Lexer (sözcük analizörü)
│ └── lexer.py
├── examples/ # Örnek kod dosyaları
│ └── ornek_kod.txt
├── README.md # Proje tanıtımı (bu dosya)
└── main.py # Ana çalışma dosyası


## ⚙️ Kurulum ve Çalıştırma

### 1. Depoyu klonlayın
git clone https://github.com/sudeenaz/Real-Time-Grammar-Based-Syntax-Highlighter-with-GUI
cd syntax-highlighter
2. Gerekli kütüphaneleri yükleyin

pip install -r requirements.txt
3. Uygulamayı başlatın

python main.py
🖼️ Ekran Görüntüsü


📘 Örnek Gramer Kuralı 
TOKEN_REGEX = [
    ('ANAHTAR_KELIME', r'\b(if|else|for|while|return)\b'),
    ('SAYI', r'\b\d+\b'),
    ('STRING', r'\".*?\"'),
    ('YORUM', r'//.*'),
    ...
]

👩‍💻 Nasıl Çalışır?
Kullanıcı kod giriş alanına yazı yazar.

Lexer, tanımlı dilbilgisi kurallarına göre bu girdiyi tarar.

Her bir sözdizimsel öğe tanımlanır ve vurgulama rengi atanır.

GUI, yazarken bu öğeleri anlık olarak renklendirir.

🤝 Katkıda Bulunmak
Katkılarınızı memnuniyetle karşılıyoruz! Yeni özellikler eklemek, gramer kurallarını genişletmek ya da performansı artırmak istiyorsanız:

Reponun bir kopyasını çatallayın.

Yeni bir dal oluşturun: git checkout -b ozellik-adi

Değişiklikleri yapın ve commit edin.

Bir pull request gönderin.


👤 Geliştirici
Ad Soyad: Sude Naz Doğdu
E-posta: Sudedogdu33@gmail.com
Ders: Programlama Dilleri
Üniversite: Bursa Teknik Üniversitesi
