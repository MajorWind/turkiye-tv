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
    # MPV ve IPTVnator hatasını önleyen parametreli format
    liste_icerigi = f"#EXTM3U\n#EXTINF:-1 tvg-name=\"Kanal D\" group-title=\"Ulusal\",Kanal D HD\n#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)\n{bulunan_link}|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    with open("liste.m3u", "w", encoding="utf-8") as dosya:
        dosya.write(liste_icerigi)
    print("Bağlantı başarıyla güncellendi.")
else:
    print("Bağlantı bulunamadı.")
