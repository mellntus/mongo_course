from flask import Flask
from flask_restful import Api

# INTERFACE
app = Flask(__name__, template_folder="views")
api = Api(app, prefix="/api")
web = Api(app)

# DATABASE
from app.db_manager import DatabaseManager
DatabaseManager.open_database()

from app import routes

