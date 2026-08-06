import requests
import json
from config import BASE_URL, DISCORD_WEBHOOK


STATUS_FILE = "queue_status.json"


def send_discord(message):
    if not DISCORD_WEBHOOK:
        print("Webhook Discord manquant")
        return

    requests.post(
        DISCORD_WEBHOOK,
        json={
            "content": message
        }
    )


def load_status():
    try:
        with open(STATUS_FILE, "r") as file:
            return json.load(file)

    except:
        return {
            "queue_active": False
        }


def save_status(status):
    with open(STATUS_FILE, "w") as file:
        json.dump(status, file, indent=2)


def check_queue():

    status = load_status()

    try:
        response = requests.get(
            BASE_URL,
            headers={
                "User-Agent": "Mozilla/5.0"
            },
            timeout=15
        )

        page = response.text.lower()


        queue_indicators = [
            "queue-it",
            "waiting room",
            "virtual waiting room",
            "you are in line",
            "please wait"
        ]


        queue_found = any(
            indicator in page
            for indicator in queue_indicators
        )


        # Nouvelle queue détectée
        if queue_found and not status["queue_active"]:

            send_discord(
                "🚨 🍆 QUEUE POKÉMON CENTER LES PAPOUTES 🍆 🚨\n\n"
                + BASE_URL
            )

            status["queue_active"] = True


        # Queue fermée
        elif not queue_found and status["queue_active"]:

            send_discord(
                "✅ Queue Pokémon Center Canada fermée"
            )

            status["queue_active"] = False


        save_status(status)

        print("Queue active:", queue_found)


    except Exception as e:

        print(
            "Erreur:",
            e
        )


if __name__ == "__main__":

    print(
        "🎴 Pokémon Center Canada Queue Tracker"
    )

    check_queue()
