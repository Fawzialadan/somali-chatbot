jawaabo = {
    "Wan Ku Salaamay": "Waan Kaa qaaday! Sideed tahay?",
    "Sidee tahay": "Fiican, mahadsanid. Adna?",
    "Waan Fiicanahy": "Waan ku farxay! Maxaan kuu qaban karaa?",
    "Magacaaga": "Magacaygu waa Somali Bot.",
    "xaggee joogtaa": "Waxaan ku nool ahay kombiyuutarka.",
    "Cuntada Noce Jeceshahy": "Baasto, bariis iyo hilib ayaan Jeclahay!",
    "Soomaaliya Waa Dal Nocee ah": "Soomaaliya waa dal quruxsan, dadkiisuna waa dad martisoorka Jecel.",
    "mahadsanid": "Adaa mahadsan!",
    "caawin": "Waxaad i weydiin kartaa Sualaha sida: Wan Ku salaamay, Sidee tahay, Cuntada Noce Jeceshahy, Soomaaliya Waa Dal Nocee ah, ama nabadgelyo.",
}

# Weydii magaca isticmaalaha
print("Somali Bot: Soo dhawoow! Magacaaga Iisheeg Si aan Kuugu Woco?")
magac = input("Adiga: ").strip()
print(f"Somali Bot: Waan ku faraxsanahay inaan ku arko, {magac}! Qor 'caawin' si aad u aragto waxaan sameyn karo.")

while True:
    qoraal = input(f"{magac}: ").lower().strip()

    # Hadduu qoro nabadgelyo, xir
    if qoraal == "nabadgelyo":
        print(f"Somali Bot: Nabadgelyo, {magac}! Maalin wanaagsan.")
        break

    # Raadi jawaab
    la_helay = False
    for erey in jawaabo:
        if erey in qoraal:
            print("Somali Bot:", jawaabo[erey])
            la_helay = True
            break

    # Haddii aan jawaab la helin
    if not la_helay:
        print("Somali Bot: Waan ka xumahay, ma fahmin. Qor 'caawin'.")