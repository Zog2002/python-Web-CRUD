import logging
import os

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



# init SQLAlchemy
db = SQLAlchemy()
migrate = Migrate()
