import requests
from bs4 import BeautifulSoup
import time

print("""
-----------------------------------
BORSA TAKIP UYGULAMASINA HOSGELDINIZ
-----------------------------------
CIKMAK ICIN 'q' YA BASINIZ.


""")
url = "https://www.doviz.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"

}

response = requests.get(url,headers = headers)


if response.status_code == 200:
    soup = BeautifulSoup(response.content,"html.parser")

    dolar = soup.find("span",{"data-socket-key":"USD"}).text
    euro = soup.find("span",{"data-socket-key":"EUR"}).text
    altin = soup.find("span", {"data-socket-key": "gram-altin"}).text
    borsa = soup.find("span", {"data-socket-key": "XU100"}).text

    print(f"Dolar: {dolar}\t")
    print(f"Euro:  {euro}\t")
    print(f"Altin: {altin}\t")
    print(f"Borsa: {borsa}\n")
else:
    print(f"Web sayfası alınamadı.HTTP durum kodu: {response.status_code}")
while True:
    print("Çıkmak için 'q' ya basınız.\tc")
    print("Tekrar işlem yapmak için 'c' ye basınız.\n")
    islem = input("Yapmak istediğiniz işlemi seçiniz(q/c): ")


    if islem == 'q':
        print("Görüşmek üzere...")
        time.sleep(2)
        break
    elif islem == 'c':
        miktar = float(input("Miktarı giriniz: "))
        birim = input("Döviz birimini giriniz(USD/EUR):").upper()
        if birim == "USD":
            sonuc = miktar * float(dolar.replace(",", "."))
        elif birim == "EUR":
            sonuc = miktar * float(euro.replace(",", "."))
        else:
            sonuc = None

        if sonuc:
            print(f"{miktar} {birim},{sonuc:.2f}TL'ye eşittir\n")
        else:
            print("Geçersiz birim, lütfen geçerli bir birim seçin(EUR/USD).\n")
    else:
        print("Geçersiz işlem lütfen geçerli bir işlem seçiniz(q/c)")
        continue



