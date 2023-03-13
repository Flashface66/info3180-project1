import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
app.config['UPLOAD_FOLDER'] = os.path.abspath('./uploads/')
db = SQLAlchemy(app)




from app import views
from app import models

migrate = Migrate(app, db)