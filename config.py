# Pokémon Center Canada Tracker

BASE_URL = "https://www.pokemoncenter.com/en-ca"

# Discord
import os

DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")

# Mots-clés importants
KEYWORDS = [
    "151",
    "Prismatic",
    "Black Bolt",
    "White Flare",
    "Team Rocket",
    "Elite Trainer Box",
    "ETB",
    "Ultra Premium Collection",
    "Booster Bundle"
]

# Temps d'attente entre les vérifications
CHECK_INTERVAL = 300
