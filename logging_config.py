LOG_CONFIG = {
    "version": 1,
    "formatters": {
        "default": {
            "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
        }
    },
    "handlers": {
        "wsgi": {
            "class": "logging.StreamHandler",
            "stream": "ext://flask.logging.wsgi_errors_stream",
            "formatter": "default",
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": "flask-datatables.log",
            "formatter": "default",
            "level": "INFO"
        },
    },
    "loggers": {
        "root": {"level": "INFO", "handlers": ["wsgi", "file"]},
    },
}
