import re
import urllib.request

kaynak_adres = "https://www.kanald.com.tr/canli-yayin"

istek = urllib.request.Request(
    kaynak_adres, headers={'User-Agent': 'Mozilla/5.0'}
)
sayfa_icerigi = urllib.request.urlopen(istek).read().decode('utf-8')

desen = re.search(r'https?://[^\s<>"]+?kanald[^\s<>"]*?\.m3u8[^\s<>"]*', sayfa_icerigi)

if desen:
    bulunan_link = desen.group(0)
    liste_icerigi = f"#EXTM3U\n#EXTINF:-1,Kanal D HD\n{bulunan_link}"
    with open("liste.m3u", "w", encoding="utf-8") as dosya:
        dosya.write(liste_icerigi)
    print("Bağlantı başarıyla güncellendi.")
else:
    print("Bağlantı bulunamadı.")
