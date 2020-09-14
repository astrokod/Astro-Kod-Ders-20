# Gerekli içe aktarmalar
import requests
import datetime
import numpy as np
from matplotlib import pyplot as plt

# Grafiği çizilecek ülkenin adı
country = "turkey"

# API adresi
url = f"https://api.covid19api.com/total/country/{country}"
# İsteğin gönderilmesi
res = requests.get(url=url)
# Yanıttan verinin JSON formatında alınması
json_data = res.json()

# Tüm veriyi saklamak için kullanılacak matris
data = []
# JSON verinin satır satır okynması
for line in json_data:
    # Her satırdan Date verisini datetime objesine çevirmek
    date_object = datetime.datetime.strptime(line['Date'], "%Y-%m-%dT%H:%M:%SZ")
    # datetime objesi ve JSON verinin geriye kalanlarını data'ya ekleme
    data.append([date_object, line['Confirmed'], line['Deaths'],
                 line['Recovered'], line['Active']])

# data'yı numpy veri formatına (ndarray) çevirme
data = np.array(data)

# Grafiğin başlığı
plt.title(f"{country} için Covid-19 İstatistiği")
# Siyah renkte Zamana bağlı Vaka sayısının grafiği
plt.plot(data[:, 0], data[:, 1], "k-", label="Vaka")
# SiyaKırmızıh renkte Zamana bağlı Ölüm sayısının grafiği
plt.plot(data[:, 0], data[:, 2], "r-", label="Ölüm")
# Yeşil renkte Zamana bağlı İyileşme sayısının grafiği
plt.plot(data[:, 0], data[:, 3], "g-", label="İyileşen")
# MAvi renkte Zamana bağlı Aktif Vaka sayısının grafiği
plt.plot(data[:, 0], data[:, 4], "b-", label="Aktif")
# X eksenine etiket ekleme
plt.xlabel("Tarih")
# Y eksenine etiket ekleme
plt.ylabel("Sayı")
# Grafik bilgilerini ekleme
plt.legend()
# Grafiği gösterme
plt.show()
