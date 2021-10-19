import os

from dotenv import load_dotenv

load_dotenv()
admins = [
    os.getenv("ADMIN_ID"),
]

ip = os.getenv("ip")
BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
PGUSER = str(os.getenv("PGUSER"))
PGPASSWORD = str(os.getenv("PGPASSWORD"))

DATABASE = os.getenv("DATABASE")



aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}
PICTURE_ROOT_PATH ='PHOTO\\'
BIN_FILES_ROOT_PATH ='BIN\\'
PICTURES_URL ='https://www.neoluxe.ru/photo/'
data_base_config ='''
dbname='dogs', user='postgres', password='IlonMask@Python', host='192.254.171.172'
'''