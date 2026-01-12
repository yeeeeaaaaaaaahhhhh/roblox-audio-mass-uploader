import requests
import sys
import os
import json

def main():
    try:
        config_dosyasi = 'config.json'

        if not os.path.exists(config_dosyasi):
            print("config.json yokmuş aga, ben bi tane sallıyorum...")
            config_icerik = {
                "cookie": "Cookie koy buraya knk",
                "creator": {
                    "groupId": ""
                }
            }
            with open(config_dosyasi, 'w') as dosya:
                json.dump(config_icerik, dosya, indent=4)

            print("config.json hazır. Cookie’yi yapıştır gel.")
            sys.exit(1)

        with open(config_dosyasi, 'r') as dosya:
            config = json.load(dosya)
            cookie = config.get('cookie')
            grup_id = config.get('creator', {}).get('groupId')

            if not cookie or cookie.strip() == "":
                print("Cookie yok, böyle olmaz. Düzelt gel.")
                sys.exit(1)

        cevap = requests.get(
            'https://users.roblox.com/v1/users/authenticated',
            cookies={'.ROBLOSECURITY': cookie}
        )

        if cevap.status_code != 200:
            print("Roblox seni tanımadı, cookie çöp olabilir.")
            sys.exit(1)

        kullanici_bilgisi = cevap.json()
        kullanici_id = kullanici_bilgisi["id"]

        def xsrf_kap():
            r = requests.post(
                "https://auth.roblox.com/v2/login",
                headers={"X-CSRF-TOKEN": ""},
                cookies={'.ROBLOSECURITY': cookie}
            )
            return r.headers.get('x-csrf-token')

        xsrf_token = xsrf_kap()

        headerlar = {
            'user-agent': 'Mozilla/5.0',
            'x-csrf-token': xsrf_token,
            'cookie': f'.ROBLOSECURITY={cookie}'
        }

        for dosya_yolu in sys.argv[1:]:
            dosya_adi = os.path.basename(dosya_yolu)
            gorunen_isim = os.path.splitext(dosya_adi)[0]

            if grup_id:
                creator_info = f'"creator":{{"groupId":{grup_id}}}'
            else:
                creator_info = f'"creator":{{"userId":{kullanici_id}}}'

            payload = {
                'fileContent': (dosya_adi, open(dosya_yolu, 'rb'), 'audio/mpeg'),
                'request': (
                    None,
                    f'{{"displayName":"{gorunen_isim}","description":"","assetType":"Audio","creationContext":{{{creator_info},"expectedPrice":0}}}}'
                ),
            }

            yukleme = requests.post(
                'https://apis.roblox.com/assets/user-auth/v1/assets',
                headers=headerlar,
                files=payload
            )

            print(f"{dosya_adi} attım gitti → status: {yukleme.status_code}")

            try:
                print(yukleme.json())
            except:
                print("Roblox saçma sapan bi şey döndürdü, JSON falan yok.")

    except Exception as hata:
        print(f"Bir şeyler ters gitti: {hata}")

    finally:
        input("devam için entera bas")

if __name__ == "__main__":
    main()
