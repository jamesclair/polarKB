import os
from dotenv import load_dotenv

ENV_FILE_LOCATION: str = ".env"
load_dotenv(ENV_FILE_LOCATION)

# from env vars
LOGGING_LEVEL: str = os.getenv("LOGGING_LEVEL", "VERBOSE")
DB_PASSWORD: str = os.getenv("DB_PASSWORD", "postgres")
DB_USERNAME: str = os.getenv("DB_USERNAME", "postgres")
DB_NAME: str = os.getenv("DB_NAME", "polarkb")
DB_HOSTNAME: str = os.getenv("DB_HOSTNAME", "lolhost")
DB_PORT: str = os.getenv("DB_PORT", "5432")

DB_CONNECTION_STR: str = (
    f"dbname={DB_NAME} user={DB_USERNAME} password={DB_PASSWORD} host={DB_HOSTNAME} port={DB_PORT}"
)
