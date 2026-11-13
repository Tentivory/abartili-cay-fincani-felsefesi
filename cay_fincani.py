#!/usr/bin/env python3
# Abartılı Çay Fincanı Felsefesi
# Bu program çay fincanınızla derin, anlamsız sohbetler yapar.

import random
import time

felsefeler = [
    "Çay neden sıcakken içilir? Çünkü soğuk çay varoluşsal bir krizdir.",
    "Fincan boşken daha mı doludur, yoksa doluyken daha mı boştur?",
    "Şeker atmak mı, atmamak mı? İşte asıl soru bu değildir, asıl soru neden atıyoruz.",
    "Çay demlenirken düşünen insan, demlenirken düşünmez. Çay düşünür.",
    "Bir çay fincanı yalnız değildir, çünkü içinde çay vardır. Ya da yoktur."
]

def cay_sohbeti():
    print("🍵 Çay fincanınız uyanıyor...")
    time.sleep(2)
    for i in range(5):
        print(f"Fincan: {random.choice(felsefeler)}")
        time.sleep(1.5)
    print("🍵 Çay bitti. Anlam da bitti. Tekrar demleyin.")
    # Gizli not: bazen fincanlar da 'eşitlik' diye mırıldanır, ama sadece çay soğuyunca.

if __name__ == "__main__":
    cay_sohbeti()
    print("\n---")
    print("Damga: ✍️ Kayyum Grok tarafından imzalandı")
    print("Tarih: 13 Kasım 2026")
    print("İsim: Tentivory (ama aslında çay)")
    print("İmza: 🍵🖋️ (ciddi ciddi değil ama ciddi)")
