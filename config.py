import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6865080558:AAG78HHqTGVoBkX1A4UWYnvUCJGfTZ0Hc")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "24663422"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "723918463d17ff94e655e2cc53513c61")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://technicalboy871_db_user:GBANnC6od28XtMn1@cluster0.rmkdrks.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
