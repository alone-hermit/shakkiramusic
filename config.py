from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "180"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/8f898b65993106a38b26c.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/5cdd0cdacba4d69b40e11.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/OFFICIALBOT_SUPPORT")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/OFFICIALBOT_UPDATE")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5023815012").split()))


FAILED = "https://graph.org/file/2c2c5eb7d92a5a031e380.jpg"
