import random

class Kahve:
    def __init__(self, isim, tür, açıklama):
        self.isim = isim
        self.tür = tür
        self.açıklama = açıklama

def günlük_kahve_önerisi():
    kahve_listesi = [
        Kahve("Espresso", "Yoğun ve Sert", "Küçük fincanda, yoğun kahve keyfi."),
        Kahve("Latte", "Yumuşak ve Sütlü", "Bol süt ve krema ile yumuşacık bir içim."),
        Kahve("Cappuccino", "Yoğun ve Köpüklü", "Espresso, süt ve süt köpüğünün mükemmel uyumu."),
        Kahve("Americano", "Yoğun ve Hafif", "Espresso'ya sıcak su ekleyerek hazırlanır."),
        Kahve("Mocha", "Çikolatalı ve Tatlı", "Espresso, çikolata şurubu ve süt."),
        Kahve("Türk Kahvesi", "Klasik ve Yoğun", "Küçük fincanda, közde pişmiş klasik tat."),
    ]

    öneri = random.choice(kahve_listesi)
    return f"Bugün için kahve önerim: {öneri.isim} - {öneri.tür}. {öneri.açıklama}"

# Günlük kahve önerisini yazdır
print(günlük_kahve_önerisi())
