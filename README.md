# Roblox Audio Uploader (Mass Upload Tool)

Bu tool, Roblox'a **audio (ses) dosyalarını toplu şekilde yüklemek** için yazılmış basit bir Python scriptidir.

Proje **2024 itibarıyla fixlenmiştir**

Tool public olarak paylaşılmıştır, **istediğiniz gibi modlayabilir, kurcalayabilirsiniz**.

---



## 📦 Gereksinimler (Requirements)

* Python **3.9+**
* `requests` kütüphanesi

### Kurulum

```bash
pip install requests
```

---

## ⚙️ Çalıştırma

1. Bu repoyu klonla veya ZIP olarak indir
2. Scripti ilk kez çalıştır

```bash
python uploader.py
```

3. Otomatik olarak `config.json` oluşturulur
4. Script durur ve senden config'i doldurmanı ister

---

## 📝 config.json Ayarları

```json
{
    "cookie": "Cookie koy buraya knk",
    "creator": {
        "groupId": "1337"
    }
}
```

### Alanların açıklaması

* **cookie**
  Tarayıcıdan aldığın `.ROBLOSECURITY` cookie’si

* **groupId**

  * Boş bırakırsan → audio **kendi hesabına** yüklenir
  * Bir grup ID’si girersen → audio **o grubun audio kısmına** yüklenir
  * Girdiğin grupta audio yükleme yetkin olmalı
---

## ▶️ Kullanım

Scripti audio dosyalarıyla birlikte çalıştır:

```bash
python uploader.py ses1.mp3 ses2.mp3 ses3.mp3
```

* Dosya adı → Roblox’ta **audio adı** olarak kullanılır
* Açıklama kısmı boş bırakılır

---

## 🧠 Bilinen Durumlar

* Roblox upload sırasında **random şekilde reddedebilir**
* Bazı dosyalar `200` dönerken bazıları red yiyebilir
* Bu normaldir, Roblox’un kendi moderasyonuyla alakalıdır

---
