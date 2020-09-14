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

# xkcd formatında grafik
with plt.xkcd():
    # Grafik başlığı
    plt.title(f"{country} için Covid-19 İstatistiği")
    # Siyah renkte Toplam vaka sayısına göre yeni vaka sayısının grafiği
    plt.plot(data[:, 1][1:], np.diff(data[:, 1]), "k-")
    # X ekseni etiketi
    plt.xlabel("Vaka Sayısı")
    # Y ekseni etiketi
    plt.ylabel("Yeni Vaka Sayısı (Günlük)")
    # X ve Y eksenini logaritmik yap
    plt.xscale("log")
    plt.yscale("log")
    # Grafiği covid.pdf olarak kaydet
    plt.savefig("covid.pdf")
    # Grafiği göster
    plt.show()
