import os
import settings
from app import create_app


if os.environ['PROJECT_ENV'] == "prod":
    config = settings.ProdConfig
else:
    config = settings.DevConfig

application = create_app(config)
