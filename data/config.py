from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
db_name = env.str("MONGO_INITDB_DATABASE")
db_user = env.str("MONGO_INITDB_ROOT_USERNAME")
db_password = env.str("MONGO_INITDB_ROOT_PASSWORD")
db_host = env.str("HOST")