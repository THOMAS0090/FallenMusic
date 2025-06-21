from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "28590877"))
API_HASH = getenv("API_HASH", "056666a4c5f136da9aac93269994f30b")

BOT_TOKEN = getenv("BOT_TOKEN", "7860005902:AAGUDG_Y73-nRXDNtvwBt4TG5F3GCZcs7IU")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "7390298763"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/c34fc9d62d93032868f02-ffd4f1f6e48434a23a.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/c34fc9d62d93032868f02-ffd4f1f6e48434a23a.jpg")

SESSION = getenv("SESSION", "BQG0Qx0AgiaWoahUWFFj9EUP4TcoDzQi7471cm3J1zcOSDF1Wzb1dUNGpQM0chDQlQGsfgsDTS5eoJRy8x8my35L2tGmY0r7LstrahkrKN7NnHg7Lctdff8EaSqFjb_i-ZTeyb4yBzraSK0gSz4mMWd59BEncqQ8L1fNSx1TR29E67HkiuxTbnIUa-LqUonjKsQzXCfGzuX8_2-X2g_67RFcdlhdV3ynSeZ-cg7sCRPbexfrBxemGLYKCe6CI8xS9mQV0QEw5-PJoBC8K4LwdGcy2hROfWlQHUP_ZE4L4AJ9AKfLic_SLxq8OupHEuChF0e3jpiKCD5eMmliGIQYBO0y5nwYxQAAAAHBhusAAA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/sigma_thomas8")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/sigma_thomas8")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7422544302").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
