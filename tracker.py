import requests
import time
from config import BASE_URL, DISCORD_WEBHOOK, KEYWORDS, CHECK_INTERVAL


def send_discord(message):
    if DISCORD_WEBHOOK == "":
        print("Webhook Discord manquant")
        return

    data = {
        "content": message
    }

    try:
        requests.post(DISCORD_WEBHOOK, json=data)
    except Exception as e:
        print("Erreur Discord:", e)


def check_pokemon_center():

    try:
        response = requests.get(
            BASE_URL,
            timeout=15,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        page = response.text.lower()

        # Vérification queue virtuelle
        queue_words = [
            "queue-it",
            "waiting room",
            "virtual waiting room",
            "queue"
        ]

        for word in queue_words:
            if word in page:
                send_discord(
                    "🚨 QUEUE POKÉMON CENTER CANADA ACTIVE 🚨\n"
                    + BASE_URL
                )
                return


        # Vérification mots-clés produits
        found = []

        for keyword in KEYWORDS:
            if keyword.lower() in page:
                found.append(keyword)


        if found:
            send_discord(
                "🆕 Produit potentiel détecté Pokémon Center Canada\n\n"
                + ", ".join(found)
            )

        else:
            print("Aucun changement détecté")


    except Exception as e:
        print("Erreur:", e)



if __name__ == "__main__":

    print("🎴 Pokémon Center Canada Tracker lancé")

    check_pokemon_center()

    print("Scan terminé")
