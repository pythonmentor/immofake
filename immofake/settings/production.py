import logging.config

import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration
from sentry_sdk.integrations.django import DjangoIntegration

from immofake.settings import *


DEBUG = False
SECRET_KEY = os.environ.get(
    "SECRET_KEY", "xrxwegrxgermewnurbctzonyzUZOUNZIUzuzounOZUzouznoUZ"
)

sentry_sdk.init(
    dsn="https://f90c3bf3fc7643d2afc2c85b6688ae4c@sentry.io/1491457",
    integrations=[DjangoIntegration(), LoggingIntegration()]
)