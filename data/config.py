from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # We take the value of type str
channels = [-1001544365046]
ADMINS = env.list("ADMINS")  # list of admins
IP = env.str("ip")  # str, but for the IP address of the host

DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")
DB_NAME = env.str("DB_NAME")
DB_HOST = env.str("DB_HOST")
