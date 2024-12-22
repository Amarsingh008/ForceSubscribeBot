import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    DATABASE_URL = os.environ.get('DATABASE_URL', None)
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', None)
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = "26494161"
    API_HASH = "55da841f877d16a3a806169f3c5153d3"
    BOT_TOKEN = "7793828619:AAHnY60vTcElNV_Trmd_DE6pKi7y_RKqRO8"
    DATABASE_URL = "mongodb+srv://lokendrasaini9galaxy:f0TVDwu5pVrHn5i6@cluster0.zseht.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = "StarkBots"
    if MUST_JOIN.startswith("@af_cinemax"):
        MUST_JOIN = MUST_JOIN[1:]

DEVS = [1744109441, 1946995626]
