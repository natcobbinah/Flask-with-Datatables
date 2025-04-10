from environs import Env

env = Env()
env.read_env()

# Override in .env for local development
DEBUG = env.bool("FLASK_DEBUG", default=False)
# SECRET_KEY is required
SECRET_KEY = env.str("SECRET_KEY")

# SQLITE CONFIG
SQLALCHEMY_DATABASE_URI = env.str("SQLALCHEMY_DATABASE_URI")
SQLALCHEMY_TRACK_MODIFICATIONS = env.bool("SQLALCHEMY_TRACK_MODIFICATIONS")
