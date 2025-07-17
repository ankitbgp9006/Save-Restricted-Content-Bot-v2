# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""
img_url = getenv("img_url","https://i.ibb.co/fYw4SkBB/x.jpg")
Credit = getenv("Credit","ᗰ𝓸𝓃ķ ᗰ𝓸𝒹𝒆")
c_url = getenv("c_url","https://t.me/TgXMonk")
API_ID = int(getenv("API_ID", "22132723"))
API_HASH = getenv("API_HASH", "40b7845461f72cd1af711e723f50424c")
BOT_TOKEN = getenv("BOT_TOKEN", "7506301443:AAEy5FS3ntcaBxDYhpNRUV6UOVYhwjIwF6M")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7457841794").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://kiranbgp1984:YVMTECqkUDSa1gvX@cluster0.nwgjbuf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002801133901")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002646253703"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "10000"))
WEBSITE_URL = getenv("WEBSITE_URL", "indianshortner.com")
AD_API = getenv("AD_API", "2c1a1a8b45d35782b595c0a645b4d03694b937d0")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
